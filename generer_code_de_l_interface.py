# −∗− coding: utf−8 −∗−
"""Le module uic de PyQt5 convertit les fichiers ui (code XML) en fichier (code Python)"""
from PyQt5 import uic

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(allow_abbrev=True)

    parser.add_argument(
        'input_file',
        type=str,
        help='path to the .ui file to convert to a .py file',
    )

    parser.add_argument(
        'output_file',
        type=str,
        help=(
            'path to the converted .py file'
        ),
    )

    args = parser.parse_args()

    uic.compileUi(
        open(args.input_file, 'r'),
        open(args.output_file, 'w'),
        execute=True
    )
