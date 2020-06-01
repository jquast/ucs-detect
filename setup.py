#!/usr/bin/env python
"""
Setup.py distribution file for ucs-detect.

https://github.com/jquast/ucs-detect
"""
# std imports
import os
import codecs

# 3rd party
import setuptools


def _get_here(fname):
    return os.path.join(os.path.dirname(__file__), fname)


def _get_version(fname, key='package'):
    import json
    return json.load(open(fname, 'r'))[key]


class _SetupUpdate(setuptools.Command):
    # This is a compatibility, some downstream distributions might
    # still call "setup.py update".
    #
    # New entry point is tox, 'tox -eupdate'.
    description = "Fetch and update unicode code tables"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        retcode = subprocess.Popen([
            sys.executable,
            _get_here(os.path.join('bin', 'update-tables.py'))]).wait()
        assert retcode == 0, ('non-zero exit code', retcode)


def main():
    """Setup.py entry point."""
    setuptools.setup(
        name='ucs-detect',
        version='0.0.1',
        description=(
            "Detects the Unicode Version of an interactive terminal for export"),
        long_description=codecs.open(
            _get_here('README.rst'), 'rb', 'utf8').read(),
        author='Jeff Quast',
        author_email='contact@jeffquast.com',
        install_requires=('blessed>=1.17.6<2'),
        license='MIT',
        packages=['ucs_detect'],
        url='https://github.com/jquast/ucs-detect',
        package_data={
            '': ['LICENSE.txt', '*.rst'],
        },
        zip_safe=True,
        classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Development Status :: 5 - Production/Stable'
            'Environment :: Console',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Localization',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Terminals'
        ],
        entry_points={
            'console_scripts': ['ucs-detect=ucs_detect:main'],
        },

        keywords=[
            'cjk',
            'combining',
            'console',
            'eastasian',
            'emoji'
            'emulator',
            'terminal',
            'unicode',
            'wcswidth',
            'wcwidth',
            'xterm',
        ],
        cmdclass={'update': _SetupUpdate},
    )


if __name__ == '__main__':
    main()