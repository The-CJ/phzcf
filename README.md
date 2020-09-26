# Phaaze Config File

A Yaml file style with JSON support.
I just made this because i wanted my config files to look like i want them, soooo yeah... duh

It suppose to be an easy to read syllable file, which contents can be easily imported into a python program,
Together with full JSON support in variable values.  
In it's core it's meant to be one-dimensional, but you might use JSON objects or list to got as deep as you want.

## Background info
I actually just made this, because you can not add comments into JSON files, which i used a long time to store my configs.  
Or when i add temporal test values without deleting the others, restoring the "real" name might sometime gets confusing,
at least for me, maybe because Im dumdum? Who knows. But yeah that the reason.

## Example
```py
import phzcf

# yeah, thats all
config_data = phzcf.load("example_config.phzcf")

print(type(config_data))
print("-----")
print(config_data)
print("+++++")
print(make_stuff_readable(config_data))
```

## Output
```
<class 'dict'>
-----
{'Version': '1.0.0', 'some_bool': True, 'some_str': 'eqwe1t23qw', 'some_int': 69, 'some_float': 2.8, 'some_other_bool': False, 'some_other_str': 'qweterzhzt', 'some_other_int': 420, 'some_other_float': 6.9, 'shifted once with space': 'Hello', 'shifted twice with both': 'there', 'we going deeper': 1, 'we going even deeper': 2, 'we going even deeper, but not actually deeper': 3, 'something overwritten': 'There is nothing', 'a good ol list': [1, '2', 3.5], 'a entire object, sure': {'A': '1', 'B': 2, 'C': {'A': 3.1, 'B': '3,5', 'C': 4}}}
+++++
{
	'Version': '1.0.0',
	'some_bool': True,
	'some_str': 'eqwe1t23qw',
	'some_int': 69,
	'some_float': 2.8,
	'some_other_bool': False,
	'some_other_str': 'qweterzhzt',
	'some_other_int': 420,
	'some_other_float': 6.9,
	'shifted once with space': 'Hello',
	'shifted twice with both': 'there',
	'we going deeper': 1,
	'we going even deeper': 2,
	'we going even deeper, but not actually deeper': 3,
	'something overwritten': 'There is nothing',
	'a good ol list': [
		1,
		'2',
		3.5
	],
	'a entire object, sure': {
		'A': '1',
		'B': 2,
		'C': {
			'A': 3.1,
			'B': '3,5',
			'C': 4
		}
	}
}
```
