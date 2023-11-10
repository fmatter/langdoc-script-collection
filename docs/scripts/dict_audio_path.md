---
tags:
    - flex
---
# Add prefix to audio path (`.lift`)
This script iterates a `.lift` export and modifies the `href` attribute of every `media` tag.
This is where paths to audio files are stored.

## Setup
The modification consists of adding a prefix to the path.
Edit the variables `PREFIX` and `TARGET` in the script.
It is very easy to implement other modifications using this as a basis (modifying attributes of entities).

Requirements:

```shell
pip install beautifulsoup4
```

## Execution
```shell
python fix_audio_path.py

Changing file-1.wav to:
/home/audio/file-1.wav
...
```

## Source
```python
{%
   include-markdown '../../dict_audio_path.py'
   rewrite-relative-urls=false
   comments=false
%}
```