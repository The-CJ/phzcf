from typing import Any, Dict, IO

import os
import re

FileMatch:re.Pattern = re.compile(r"")

def load(source:Any, **options) -> Dict[str, Any]:
	"""
	Tryed to detect the given input as a valid load function, will return the config file data
	source might be:
	* path to config file
	* file contents as string
	* file contents as bytes
	* IO Object with .read() like open('path', 'r')
	"""

	if os.path.isfile(source):
		return loadFilePath(source, **options)

	elif hasattr(source, "read"):
		if callable(source.read):
			return loadReader(source, options)

	elif type(source) is bytes:
		return loadBytes(source, **options)

	elif type(source) is str:
		return loadString(source, **options)

	else:
		raise AttributeError(f"Could not detect source type {type(source)}, as valid input type")

def loadFilePath(source:str, **options) -> Dict[str, Any]:
	return loadReader(open(source, "rb"), **options)

def loadReader(source:IO, **options) -> Dict[str, Any]:
	return loadBytes(source.read(), **options)

def loadBytes(source:bytes, **options) -> Dict[str, Any]:
	encoding:str = options.get("encoding", "UTF-8")
	return loadString(source.decode(encoding), **options)

def loadString(source:str, **options) -> Dict[str, Any]:















	pass
