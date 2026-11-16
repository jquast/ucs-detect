"""
Deferred CPU work for the screenshot and spillover stages.

Image work that only produces a file, or only reads one, is submitted here instead of running
between two terminal pages.  A second terminal can then paint while the first one's capture is
measured, and a failure is recorded rather than raised, because the page it belongs to has already
scrolled away.
"""

# std imports
import os
import sys
import collections
from concurrent.futures import Future, ProcessPoolExecutor

#: A deferred task that failed, named by the output it was producing.
TaskError = collections.namedtuple('TaskError', ('label', 'message'))


def default_workers(cpus=None, maximum=8):
    """Return how many worker processes to run."""
    total = cpus or os.cpu_count() or 2
    return max(1, min(total - 2, maximum))


class TaskPool:
    """Run image work inline or in worker processes, recording every failure."""

    def __init__(self, workers=1):
        self.workers = max(1, int(workers))
        self.errors = []
        self._executor = (ProcessPoolExecutor(max_workers=self.workers)
                          if self.workers > 1 else None)
        self._pending = []

    def __enter__(self):
        return self

    def __exit__(self, *_exc):
        self.close()

    def submit(self, function, *args, label=''):
        """Run *function* with *args*, in a worker when one is available."""
        if self._executor is None:
            future = Future()
            try:
                future.set_result(function(*args))
            except Exception as error:  # pylint: disable=broad-except
                future.set_exception(error)
        else:
            future = self._executor.submit(function, *args)
        self._pending.append((future, label))
        return future

    def result(self, future, label=''):
        """Return ``(value, error)`` for a submitted task."""
        try:
            return future.result(), None
        except Exception as error:  # pylint: disable=broad-except
            message = str(error) or error.__class__.__name__
            self.errors.append(TaskError(label, message))
            print(f'Error: {label}: {message}', file=sys.stderr)
            return None, message

    def collect(self):
        """Wait for every submitted task, recording the failures."""
        for future, label in self._pending:
            self.result(future, label)
        self._pending = []

    def close(self):
        """Wait for the outstanding tasks and shut the worker processes down."""
        self.collect()
        if self._executor is not None:
            self._executor.shutdown(wait=True)
            self._executor = None
