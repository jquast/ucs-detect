"""Tests for the deferred task pool."""

import os

from ucs_detect import tasks


def _explode(message):
    raise ValueError(message)


def test_default_workers_leaves_two_cores():
    assert tasks.default_workers(cpus=16, maximum=8) == 8
    assert tasks.default_workers(cpus=6) == 4


def test_default_workers_never_returns_zero():
    assert tasks.default_workers(cpus=1) == 1
    assert tasks.default_workers(cpus=2) == 1


def test_inline_task_returns_its_value():
    pool = tasks.TaskPool()
    future = pool.submit(os.path.basename, '/tmp/shot.png', label='shot')
    assert pool.result(future, 'shot') == ('shot.png', None)
    assert pool.errors == []


def test_inline_task_records_a_failure(capsys):
    pool = tasks.TaskPool()
    future = pool.submit(_explode, 'boom', label='shot.png')
    assert pool.result(future, 'shot.png') == (None, 'boom')
    assert pool.errors == [tasks.TaskError('shot.png', 'boom')]
    assert 'Error: shot.png: boom' in capsys.readouterr().err


def test_collect_reports_every_failure(capsys):
    pool = tasks.TaskPool()
    pool.submit(_explode, 'first', label='one')
    pool.submit(os.path.basename, 'two', label='two')
    pool.submit(_explode, 'third', label='three')
    pool.collect()
    assert [error.label for error in pool.errors] == ['one', 'three']
    capsys.readouterr()


def test_worker_process_runs_the_task():
    with tasks.TaskPool(workers=2) as pool:
        future = pool.submit(os.getpid, label='pid')
        value, error = pool.result(future, 'pid')
    assert error is None
    assert value != os.getpid()


def test_worker_process_reports_a_failure():
    with tasks.TaskPool(workers=2) as pool:
        future = pool.submit(int, 'not a number', label='page 3')
        value, error = pool.result(future, 'page 3')
    assert value is None
    assert error
    assert pool.errors[0].label == 'page 3'


def test_close_shuts_the_executor_down():
    pool = tasks.TaskPool(workers=2)
    pool.submit(os.getpid, label='pid')
    pool.close()
    assert pool._executor is None
    assert pool._pending == []
