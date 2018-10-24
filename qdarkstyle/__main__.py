#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))

from example import example
from qdarkstyle import qt_bindings, qt_abstractions, information, __version__


def print_list_md(info):
    """Print a list of information, line by line."""
    for item in info:
        print('  - ' + item)


def main():
    """Execute QDarkStyle example."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--information', action='store_true',
                        help="Show information about environment (important for bug report)")
    parser.add_argument('--bindings', action='store_true',
                        help="Show available bindings for Qt.")
    parser.add_argument('--abstractions', action='store_true',
                        help="Show available abstraction layers for Qt bindings")
    parser.add_argument('--all', action='store_true',
                        help="Show all previous options at once")
    parser.add_argument('--example', action='store_true',
                        help="Show qdarkstyle example")
    parser.add_argument('--version', action='store_true',
                        help="Show qdarkstyle version")

    # parsing arguments from command line
    args = parser.parse_args()

    if args.information or args.all:
        info = information()
        print('Information about your environment:')
        print_list_md(info)

    if args.bindings or args.all:
        info = qt_bindings()
        print('Qt bindings available:')
        print_list_md(info)

    if args.abstractions or args.all:
        info = qt_abstractions()
        print('Qt abstraction layers available:')
        print_list_md(info)

    if args.version:
        info = __version__
        print('Version: %s' % info)

    if args.example:
        example.main()


if __name__ == "__main__":
    sys.exit(main())