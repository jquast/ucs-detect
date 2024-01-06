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
        version='1.0.7',
        description=(
            "Detects Unicode support of an interactive terminal"),
        long_description=codecs.open(
            _get_here('README.rst'), 'rb', 'utf8').read(),
        author='Jeff Quast',
        author_email='contact@jeffquast.com',
        install_requires=('blessed<2', 'wcwidth<1,>=0.2.13', 'PyYaml<7'),
        license='MIT',
        packages=['ucs_detect'],
        url='https://github.com/jquast/ucs-detect',
        package_data={
            '': ['LICENSE', '*.rst', '*.txt'],
        },
        include_package_data=True,
        zip_safe=True,
        classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Localization',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Terminals',
            'Topic :: Text Processing :: General',
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
            'zwj',
        ],
    )


if __name__ == '__main__':
    main()
