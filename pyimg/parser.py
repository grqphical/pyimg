"""Handles argument parsing and the loading of plugins"""
import argparse
from .transform import *
from .filters import *
from .adjustments import *
from plugins import BasePlugin

# Create a list of all active classes that our program can use
valid_classes = {"transform" : Transform, "filters" : Filters, "adjustments" : Adjustments}

# Setup our parser
parser = argparse.ArgumentParser(prog="pyimg")
parser.add_argument("image_file")
parser.add_argument("-s", "--stats", action="store_true", help="Whether or not to show image stats when running")
parser.add_argument("-o", "--output", help="Optional file to output to")
subparsers = parser.add_subparsers(dest='target_class')

# Load all plugins
for plugin in BasePlugin.plugins:
    valid_classes[plugin.__name__.lower()] = plugin

# Generate subparsers for all of the internal/external plugins
for name, obj in valid_classes.items():
    # Generates subparser
    subparser = subparsers.add_parser(name)
    subparser.add_argument("action", choices=[func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")], 
                        help="What method you wish to use")
    subparser.add_argument("args", nargs="*", help="arguments for the function. Check the docs for more info")
