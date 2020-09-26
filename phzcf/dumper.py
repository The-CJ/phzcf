from typing import List, Dict, Any

import json

def dumpAsString(data:Dict[str, Any], **options:dict) -> str:
	"""
	Returns a python dict as a Phaaze Config File Text Format
	"""
	to_dumb:List[str] = []

	var_name:str
	for var_name in data:
		json_save_value:str = json.dumps(data[var_name])
		to_dumb.append(f"[{var_name}] = {json_save_value}")

	return "\n".join(to_dumb)

def dumpInFile(data:dict, filetarget:str, **options:dict) -> None:
	"""
	Stores a python dict as a Phaaze Config File Text Format in a file

	Options:
	* encoding : (Default: "UTF-8")
	"""
	encoding:str = options.get("encoding", "UTF-8")

	formated_data:str = dumpAsString(data, **options)

	TargetFile:str = open(filetarget, "wb")
	TargetFile.write(formated_data.encode(encoding))
	TargetFile.close()
