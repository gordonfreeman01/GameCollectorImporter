# GameCollectorImporter

>**This repo is still heavily WIP and the core features are being built.**

A tool to batch import entries into CLZ Game Collector.

## Usage

Run the script with the -h parameter to check help.

```bash
python .\gcimporter.py -h
```

This produces the following
```bash
usage: gcimporter.py [-h] -i INPUT -o OUTPUT [-lf LOGFILE] [-ll LOGLEVEL]

A utility to convert a JSON to Game Collector XML format

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input JSON file
  -o OUTPUT, --output OUTPUT
                        Output JSON file
  -lf LOGFILE, --logfile LOGFILE
                        Log file path
  -ll LOGLEVEL, --loglevel LOGLEVEL
                        Set logging level. Example --loglevel debug, default=INFO'
```

### Convert JSON File to XML

The json2xml utility converts any JSON to a corresponding XML file without any schema transformations applied.

```bash
python .\gcimporter.py --file <input JSON file path> --output <output XML file path> --logfile <optional log file custom path>
```

For example, in the following command "test.json" is converted into "test.xml" with both files being stored one folder above the script's. This command also overrides the path for the log file for it to be stored one folder up as well (by default it is stored in the script's folder). This command also sets the log level to debug.

```bash
python .\gcimporter.py --input ../test.json --output ../test.xml --logfile ../log.txt --loglevel debug
```