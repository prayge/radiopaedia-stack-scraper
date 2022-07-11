import argparse
class Options():

    def __init__(self):
        self.initialized = False

    def initialize(self, parser):
        # directory
        parser.add_argument('-url', '--url', type=str, help='Radiopadia case URL',
                            default='https://radiopaedia.org/cases/medulloblastoma-55')
        parser.add_argument('-name', '--name', type=str,
                            help='Name of main directory', default='Medulloblastoma')

        parser.add_argument('-test', '--test', type=bool, help="test",
                            default=False)
        parser.add_argument('-dicom', '--dicom', type=bool, help="To DICOM",
                            default=False)
        parser.add_argument('-nifti', '--nifti', type=bool, help="To NiFTi",
                            default=False)
        parser.add_argument('-npy', '--npy', type=bool, help="To npy bin file",
                            default=False)

        self.initialized = True
        return parser

    def parse(self):
        if not self.initialized:
            parser = argparse.ArgumentParser(
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
            parser = self.initialize(parser)
        opt = parser.parse_args()
        return opt
