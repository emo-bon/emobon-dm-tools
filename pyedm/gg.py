# -*- coding: utf-8 -*-
import argparse
import pathlib
import os
import yaml
import logging
import pyedm.__main__ as common
from uritemplate import expand
import requests

log = logging.getLogger(__name__)

def get_xlsx(xlsxpath, docid):
    try:
        prms = dict(id=docid, format="xlsx")
        ggut = "https://docs.google.com/spreadsheets/d/{id}/export{?format,id}"
        url = expand(ggut, prms)

        # get and save the content 
        log.info(f"  get content for {xlsxpath} from {url}")
        resp = requests.get(url, allow_redirects=True)
        log.debug(f"    final url at {resp.url}")
        log.debug(f"    final content-type is {resp.headers.get('Content-Type')}")
        log.debug(f"    final status-code is {resp.status_code}")

        # todo save content to file and allow overwrite
        resp.raise_for_status() # ensure we notice bad responses
        with open(xlsxpath, "wb") as xlsxf:
            xlsxf.write(resp.content)
    except Exception as e:
        log.error(f"failure saving to {xlsxpath}")
        log.exception(e)


def get_csv(csvpath, docid, tabid = 0):
    try: 
        prms = dict(id = docid, gid = tabid, format='csv') 
        ggut = 'https://docs.google.com/spreadsheets/d/{id}/export{?format,id,gid}'
        url = expand(ggut, prms) 

        # get and save the content 
        log.info(f"  get content for {csvpath} from {url}")
        resp = requests.get(url, allow_redirects=True)
        log.debug(f"    final url at {resp.url}")
        log.debug(f"    final content-type is {resp.headers.get('Content-Type')}")
        log.debug(f"    final status-code is {resp.status_code}")

        # todo save content to file and allow overwrite
        resp.raise_for_status() # ensure we notice bad responses
        mimetype = resp.headers.get('Content-Type')
        assert mimetype.startswith("text/csv"), "not correct response mime-type: {mimetype} should be text/csv"
        with open(csvpath, "wb") as csvf:
            csvf.write(resp.content)
    except Exception as e:
        log.error(f"failure saving to {csvpath}")
        log.exception(e)


def do_get_documents(location):
    if location.is_dir():
        location = location / 'config' / 'google-docs.yml'
    assert location.exists() and location.is_file(), f"config file {location} does not exist"

    with open(location, 'r') as yml_gdocs:
        gdocs = yaml.load(yml_gdocs, Loader=yaml.SafeLoader)

    topath = (location / '..' / '..' / 'downloads' / 'gdoc-csv').resolve()
    os.makedirs(topath, exist_ok=True)

    log.info(f"get csv from {location} to {topath} as defined through {gdocs}")

    for habitat, hconf in gdocs['habitat'].items(): 
        log.info(f"  processing {habitat} = {hconf} ")
        if {'docid','tabid'}.issubset(hconf):  # both docid and tabid should be in the habitat-conf
            docid = hconf['docid'] 
            for label, tabid in hconf['tabid'].items():
                if tabid is not None:
                     csvpath = topath / f"{habitat}_{label}.csv"
                     get_csv(csvpath, docid, tabid)
     


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


    do_get_documents(pathlib.Path(args.googleconfig).resolve())



if __name__ == '__main__':
    main()
