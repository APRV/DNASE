#! /usr/bin/env python
import sys

from Decompressor import *
from Compressor import *

if __name__ == "__main__":
    if(len(sys.argv) != 5):
        print "Usage: "+sys.argv[0]+" [OPTION] [FILE]\n\nOptions:\n-c\tCompress\n-d\tDecompress\n-a [ALGORITHM]\tAlgorithm to be used for compression/decompression\n\nList of Available Algorithms:\ndefault\tNo Compression\nBitString\t2-Bit Binary Algorithm\n"
        exit()
    else:
        if(sys.argv[1] == "-d"):
            c = Decompressor()
        else:
            c = Compressor()
        c.setalgorithm(sys.argv[3])
        c.setfasta(sys.argv[4])
        if(sys.argv[1] == "-d"):
            c.decompress()
        else:
            c.compress()
