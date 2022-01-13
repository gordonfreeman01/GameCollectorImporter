import json2xml
import argparse
import logging

#Declare argument parser
parser = argparse.ArgumentParser(description="A utility to convert a JSON to Game Collector XML format")
parser.add_argument("-i","--input", help="Input JSON file", required=True)
parser.add_argument("-o","--output", help="Output XML file", required=True)
parser.add_argument("-lf", "--logfile", help="Log file path", default="./log.txt")
parser.add_argument("-ll", "--loglevel", help="Set logging level. Example --loglevel debug, default=INFO'", default="info")

#Parse arguments
args = parser.parse_args()
logFilePath = args.logfile
logLevel = args.loglevel.upper()
inputFile = args.input
outputFile = args.output

#Declare logger
logger = logging.getLogger(__name__)
logger.setLevel(logLevel)

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
#rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(logFilePath)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

#Convert JSON to XML
logger.info("JSON import started with file: {0}.".format(inputFile))
logger.debug("args: {0}".format(args))

from json2xml import json2xml
from json2xml.utils import readfromjson

with open(outputFile, 'w') as outputDataFile:
    jsonDataFile = readfromjson(inputFile)
    outputDataFile.writelines(json2xml.Json2xml(jsonDataFile).to_xml())

logger.info("XML output to file: {0}".format(outputFile))

#TODO XSLT to GC XML format

logger.info("XML export completed.")