#author Timothy Lee
#last modified: 14/7/2016

from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files' : 3, 'compressed' : True}},
    windows = [{'script' : "main.py"}],
    zipfile = None,
)
