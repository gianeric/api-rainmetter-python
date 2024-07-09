# API-Rainmetter-python

Skins for Rainmeter app

## Encoding of .lua Files

The .lua files are encoded in UTF-16 LE (Little Endian) for compatibility and readability.

## File Types

This repository contains three main types of files:

- **.lua**: Files read by Rainmeter to configure skins and functionalities.
- **.py**: Python scripts called by .lua files to perform operations such as writing and reading .txt files.
- **.ini**: Rainmeter configuration files to adjust skin settings.

## Setting up VSCode for .lua Files

If you are using VSCode, add the following code to your settings.json file to correctly configure the encoding of .lua files as UTF-16 LE:

```json
  "files.associations": {
    "*.lua": "lua"
  },
  "[lua]": {
    "files.autoGuessEncoding": false,
    "files.encoding": "utf16le"
  }
```
