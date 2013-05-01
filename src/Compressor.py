#! /usr/bin/env python

from ModBitString import *
from NewBitString import *
from DNASE import *
from BitString import *
from default import *
from os import sep 
import time
import datetime

class Compressor():
    def __init__(self,algorithm="default",fasta=".."+sep+"samples"+sep+"default"):
        self.algorithm = algorithm
        self.fasta = fasta
                                                                                                           
    def setalgorithm(self,algorithm):                                                                                                   
        self.algorithm = algorithm                                                                                                      
                                                                                                                                        
    def setfasta(self,fasta):                                                                                                            
        self.fasta = fasta                                                                                                              
                             
    def compress(self):
        constructor = globals()[self.algorithm]
        instance = constructor()
        compressedData = instance.compress(self.fasta)
        ts = time.time()                                                                                                                
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H:%M:%S')                                                          
        if(self.algorithm == "default"):
            output_file = open(self.fasta+"_compressed_default_"+st,"w")                                                                         
            for line in compressedData:                                                                                                        
                output_file.write(line)                                                                                                     
            output_file.close()
        else:
            while(len(compressedData)%8 != 0):
                compressedData += "0"
            output_file = open(self.fasta+"_compressed_"+self.algorithm+"_"+st,"wb+")
            b = bytearray([int(compressedData[x:x+8], 2) for x in range(0, len(compressedData), 8)])
            output_file.write(b)
            output_file.close()

if __name__ == "__main__":
    c = Compressor()
    c.compress()
