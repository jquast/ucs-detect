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


def main():
    """Setup.py entry point."""
    setuptools.setup(
        name='ucs_detect',
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
            '': ['LICENSE', '*.rst'],
        },
        zip_safe=True,
        classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Development Status :: 5 - Production/Stable',
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
    )


if __name__ == '__main__':
    main()
