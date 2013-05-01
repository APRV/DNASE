#! /usr/bin/env python
import time
import datetime

class default():
    def __init__(self):
        pass
    def compress(self,fasta):
        input_data = open(fasta,"r+")
        output_data = ""
        for line in input_data:
            output_data += line
        input_data.close()
        return output_data
    def decompress(self,fasta):
        input_data = open(fasta,"r+")
        output_data = ""
        for line in input_data:
            output_data += line
        input_data.close()
        return output_data

