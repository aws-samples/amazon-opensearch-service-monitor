"""
b64 - print out base64 encoded file plus resource type identifier for packing as uri data in html.


Usage:
  b64 FILE

Arguments:
  FILE     Any file that might be included as a resource in html src attributes (.svg, .png, etc)

Options:
  -h --help                    Show this screen.

"""

import base64
import mimetypes
import sys

from docopt import docopt

def main(out, filename, fp=None):
    resource_type = mimetypes.guess_type(filename)[0]
    if not fp:
        fp = open(filename)
    data = base64.encodestring(fp.read()).replace("\n", "")
    out.write('"data:{resource_type};base64,{data}"'.format(**locals()))

def run():
    args = docopt(__doc__)
    if args['FILE']:
        main(sys.stdout, args['FILE'])
    else:
        exit("Please provide a path to a file to encode")
    
if __name__ == '__main__':
    run()
          

