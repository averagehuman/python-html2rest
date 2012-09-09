# -*- coding: utf-8 -*-
import os
from os.path import join as pathjoin, exists as pathexists, dirname, basename, abspath
from distutils.core import setup

import re
version_rx = r"^__version__ = '(.*)'$"
version_pattern = re.compile(version_rx)


fd = open('html2rest.py')
try:
    for line in fd:
        m = version_pattern.match(line)
        if m:
            break
    else:
        raise Exception("couldn't find __version__")
finally:
    fd.close()

__version__ = m.group(1)

srcdir = dirname(abspath(__file__))

print "running setup for html2rest version %s" % __version__



setup(
        name="html2rest",
        version=__version__,
        description="Convert HTML to restructuredText",
        author="Gerard Flanagan",
        author_email = "grflanagan@gmail.com",
        classifiers=["Development Status :: 4 - Beta",
                    "Intended Audience :: Developers",
                    "License :: OSI Approved :: BSD License",
                    "Programming Language :: Python",
                    "Topic :: Software Development :: Libraries",
                    "Topic :: Software Development :: Libraries :: Python Modules",
                    ],
        url="https://github.com/podados/python-html2rest",
        license="BSD",
        download_url="http://pypi.python.org/packages/source/h/html2rest/html2rest-%s.tar.gz" % __version__,
        py_modules=['html2rest'],
        scripts = [
            pathjoin(srcdir, 'bin', 'html2rest'),
        ],
)
    
