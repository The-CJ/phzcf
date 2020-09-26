# -*- coding: utf-8 -*-

"""
##################
Phaaze Config File
##################

:copyright: (c) 2020 The_CJ
:license: MIT License
"""

__title__ = 'phzcf'
__author__ = 'The_CJ'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 The_CJ'
__version__ = "1.0.0"

from .loader import (
	load,
	loadFilePath,
	loadReader,
	loadBytes,
	loadString
)

from .dumper import (
	dumpAsString,
	dumpInFile
)
