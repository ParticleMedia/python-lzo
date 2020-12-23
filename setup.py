#from setuptools import setup, Extension
from __future__ import print_function

import os, sys
import distutils
from distutils.cmd import Command
from distutils.core import setup
from distutils.extension import Extension
from distutils.util import split_quoted

include_dirs = []
define_macros = []
library_dirs = []
libraries = []
runtime_library_dirs = []
extra_objects = []
extra_compile_args = []
extra_link_args = []
libraries = ["lzo2"]
include_dirs.append(os.environ.get("PREFIX", "/usr")+"/include")
ext = Extension(
    name="_lzo",
    sources=["lzomodule.c", "minilzo.c"],
    include_dirs=include_dirs,
    define_macros=define_macros,
    library_dirs=library_dirs,
    libraries=libraries,
    runtime_library_dirs=runtime_library_dirs,
    extra_objects=extra_objects,
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

setup(name='python-lzo',
      version='1.0',
      description='This is a demo package',
      py_modules=['lzo'],
      ext_modules=[ext])
