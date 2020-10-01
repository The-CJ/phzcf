from typing import Any, Dict, IO

import os
import re
import json

ClearedLine:re.Pattern = re.compile(r"^(?:\t| )*(.*?)(?:\t| )*$")
LineNameAndValue:re.Pattern = re.compile(r"^\[(.+)\](?:\t| )*=(?:\t| )*(.*)$")

def load(source:Any, **options:dict) -> Dict[str, Any]:
	"""
	Tryed to detect the given input as a valid load function, will return the config file data
	source might be:
	* path to config file
	* file contents as string
	* file contents as bytes
	* IO Object with .read() like open('path', 'r')

	Options:
	* encoding : (Default: "UTF-8")
	* abort_on_garbage : (Default: False)
	* abort_on_overwrite : (Default: False)
	* comment_re : (Default: "(#|//).*")
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

def loadFilePath(source:str, **options:dict) -> Dict[str, Any]:
	return loadReader(open(source, "rb"), **options)

def loadReader(source:IO, **options:dict) -> Dict[str, Any]:
	contents:str or bytes = source.read()
	if type(contents) is bytes:
		return loadBytes(contents, **options)
	elif type(contents) is str:
		return loadString(contents, **options)
	else:
		raise RuntimeError(f"Unknown return type {type(contents)} after reading file")

def loadBytes(source:bytes, **options:dict) -> Dict[str, Any]:
	encoding:str = options.get("encoding", "UTF-8")
	return loadString(source.decode(encoding), **options)

def loadString(source:str, **options:dict) -> Dict[str, Any]:
	abort_on_garbage:bool = bool( options.get("abort_on_garbage", False) )
	abort_on_overwrite:bool = bool( options.get("abort_on_overwrite", False) )
	comment_re:str = str( options.get("comment_re", r"^(#|//).*") )

	final_return:Dict[str, Any] = {}

	line:str
	for line in source.splitlines():

		# ignore empty
		if not line: continue

		# remove space and tab in front and end
		CleanUp:re.Match = re.search(ClearedLine, line)
		if not CleanUp: continue # that here should never happen

		line = CleanUp.group(1)

		# look for comment line
		if re.search(comment_re, line): continue

		ValidLine:re.Match = re.search(LineNameAndValue, line)
		if not ValidLine and abort_on_garbage: raise InvalidLine(f"could not validate name and value from: {line}")

		var_name:str = ValidLine.group(1)
		var_value:str = ValidLine.group(2)

		if (final_return.get(var_name, object) != object) and (abort_on_overwrite): raise ValueOverwrite(f"a key has would have been overwritten, key: {var_name}")

		try:
			final_return[var_name] = json.loads(var_value)
		except json.decoder.JSONDecodeError:
			raise JsonDecodeError(f"Can't decode line value: {line=} {var_value=}")

	return final_return

class InvalidLine(Exception): pass
class ValueOverwrite(Exception): pass
class JsonDecodeError(Exception): pass
