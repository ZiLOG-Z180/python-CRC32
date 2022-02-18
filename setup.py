#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name='sse4.2 CRC32',
    version="1.0.0",
    description='Python CRC32',
    author="Wojciech Lawren",
    license="LGPLv3",
    ext_modules=cythonize([
        Extension(
            "_crc32",
            ["crc32.pyx", "crc32/crc32.c", ],
            include_dirs=[],
            library_dirs=[],
            libraries=[],
            extra_compile_args=[],
            language="C",
        ),
    ]),
    setup_requires=[
        "cython >= 0.29.1",
    ],
    zip_safe=False,
)
