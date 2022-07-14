# -*- coding: utf-8 -*-
import argparse
import pathlib
import sys
import logging
import pyedm.__main__ as common

log = logging.getLogger(__name__)



def get_csv(topath, docid, tabid = 0):
    # example  https://docs.google.com/spreadsheets/d/1mEi4Bd2YR63WD0j54FQ6QkzcUw_As9Wilue9kaXO2DE/export?format=csv&id=1mEi4Bd2YR63WD0j54FQ6QkzcUw_As9Wilue9kaXO2DE&gid=15718907
    # there is also https://docs.google.com/spreadsheet/ccc?key=0ArM5yzzCw9IZdEdLWlpHT1FCcUpYQ2RjWmZYWmNwbXc&output=csv'  (possibly also takes a gid)
    prms = dict(id = docid, gid = tabid, format='csv') 
    ggts = 'https://docs.google.com/spreadsheets/d/{id}/export{?format,id,gid}

    # todo expand the urit
    # get and save the content 
    pass


def get_arg_parser():
    """ Defines the arguments to this script by using Python's [argparse](https://docs.python.org/3/library/argparse.html)
    """
    parser = argparse.ArgumentParser(description='tool for getting google-doc contents',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-l',
        '--logconf',
        type=str,
        action='store',
        help='location of the logging config (yml) to use',
    )

    # yaml file containing the google-cdocument ids
    parser.add_argument(
        '-g',
        '--googleconfig',
        type=str,
        action='store',
        help='Path to yml file describing the google documents',
        default=pathlib.Path().resolve(),
    )
    return parser


def main():
    """ The main entry point to this module.
    """
    args = get_arg_parser().parse_args()
    common.enable_logging(args)

    log.info("The args passed to %s are: %s." % (sys.argv[0], args))
    log.debug("Some Logging")


if __name__ == '__main__':
    main()
