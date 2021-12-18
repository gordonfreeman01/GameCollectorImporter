# GameCollectorImporter
A tool to batch import entries into CLZ Game Collector

## Usage

### Convert JSON File to XML

The json2xml utility converts any JSON to a corresponding XML file without any schema transformations applied.

```bash
python .\gcimporter.py --file <input JSON file path> --output <output XML file path> --logfile <optional log file custom path>
```

For example, in the following test.json is converted into test.xml with both files being stored one folder above the script's. This command also overrides the path for the log file to be stored one folder up (by default it is stored in the script's folder) and sets log level to debug.

```bash
python .\gcimporter.py --input ../test.json --output ../test.xml --logfile ../log.txt --loglevel debug
```