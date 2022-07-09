import argparse
import os


class Options():

    def __init__(self):
        self.initialized = False

    def initialize(self, parser):
        # directory
        parser.add_argument('-url', '--url', type=str, help='Radiopadia case URL',
                            default='https://radiopaedia.org/cases/medulloblastoma-55')
        parser.add_argument('-name', '--directory-name', type=str,
                            help='Name of main directory', default='Medulloblastoma')

        self.initialized = True
        return parser

    def parse(self):
        if not self.initialized:
            parser = argparse.ArgumentParser(
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
            parser = self.initialize(parser)
        opt = parser.parse_args()
        return opt
