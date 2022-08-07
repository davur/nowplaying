#!/usr/bin/env python3

"""Advent of Code Day 14 Part II

Usage:
  nowplaying.py --metadata-path=<path> <command>

Options:
  -h, --help            Show this screen.
  --version             Show version.
  --metadata-path=<path>  Path to data source

"""
from docopt import docopt
import json
import yaml
from pprint import pprint as pp


from flask import Flask
app = Flask(__name__)

metadata_path = ""
metadata = None

@app.route("/meta.json")
def meta():
    load_metadata()
    return json.dumps(metadata)

@app.route("/index.html")
def index():
    return app.send_static_file("index.html")


def load_metadata():
    global metadata_path
    global metadata
    metadata = {}
    with open(metadata_path, 'r', encoding='UTF-8') as file:
        while (line := file.readline().strip()):
            key = line.strip("{}:")
            value = file.readline().strip()
            metadata[key] = value

    parts = metadata['name'].split(' - ')
    if 'title' not in metadata and 'name' in metadata:
        title = parts[-1]
        title = '.'.join(title.split('.')[:-1])
        metadata['title'] = title

    if 'artist' not in metadata and 'name' in metadata:
        metadata['artist'] = " - ".join(parts[:-1])

def main(command):

    load_metadata()

    if command == "json":
        pp(json.dumps(metadata))
    elif command == "yaml":
        print(yaml.dump(metadata))
    elif command == "runserver":
        app.run()


if __name__ == '__main__':
    arguments = docopt(str(__doc__), version="0.0.1")

    metadata_path = arguments['--metadata-path']
    main(command=arguments['<command>'])
