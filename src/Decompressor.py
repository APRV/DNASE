#! /usr/bin/env python

from BitString import *
from default import *
from os import sep 
import time
import datetime

class Decompressor():
    def __init__(self,algorithm="default",fasta=".."+sep+"samples"+sep+"default"):
        self.algorithm = algorithm
        self.fasta = fasta

    def setalgorithm(self,algorithm):
        self.algorithm = algorithm

    def setfasta(self,fasta):
        self.fasta = fasta

    def decompress(self):
        constructor = globals()[self.algorithm]
        instance = constructor()
        decompressedData = instance.decompress(self.fasta)
        ts = time.time()                                                                                                                
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H:%M:%S')                                                          
        output_file = open(self.fasta+"_decompressed_default_"+st,"w")                                                                         
        for line in decompressedData:                                                                                                        
            output_file.write(line)                                                                                                     
        output_file.close()  

if __name__ == "__main__":
    c = Decompressor()
    c.decompress()
