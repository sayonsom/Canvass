""" Usage: ui_setup.py <filename>

Options:
- o  Help function

"""

import docopt
import time, sys


def callThis(filename):
    sys.ps1 = "Sayon > "
    print "Opening ... " + filename


if __name__ == '__main__':
    try:
        arguments = docopt.docopt(__doc__)

        filename = arguments['<filename>']
        sys.ps1 = "Sayon > "
        callThis(filename)
    except:
        sys.ps1 = "Sorry Yaar"
