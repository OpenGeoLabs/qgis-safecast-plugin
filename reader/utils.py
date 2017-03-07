"""SafeCast Importer Library

(C) 2015 by OpenGeoLabs s.r.o.

Read the file LICENCE.md for details.

.. sectionauthor:: Martin Landa <martin.landa opengeolabs.cz>
"""

import argparse

def parse_arguments(desc, positional=(), required=(), optional=()):
    """Parse command line arguments.

    :param desc: command description
    :param positionnal: tuple of positional arguments
    :param required: tuple of required arguments
    :param optional: tuple of optional arguments

    :return: list of parsed arguments
    """
    parser = argparse.ArgumentParser(description=desc)
    for key, meta, desc in positional:
        args = {}
        if meta is None:
            args['nargs'] = '?'
        parser.add_argument(key, metavar=meta, type=str,
                            help=desc, **args)
    requiredNamed = parser.add_argument_group('required named arguments')

    for key, meta, desc in required:
        requiredNamed.add_argument(key,
                                   metavar=meta,
                                   type=str,
                                   required=True,
                                   help=desc)

    for key, meta, desc in optional:
        args = {}
        if meta and type(meta) is str:
            if meta[-1] == '?':
                args['nargs'] = '?'
                meta = meta[:-1]
                args['const'] = True
            args['metavar'] = meta
            args['type'] = str
            args['action'] = 'store'
        else:
            args['action'] = 'store_true'
            args['default'] = meta

        parser.add_argument(key,
                            help=desc, **args)

    return parser.parse_args()
