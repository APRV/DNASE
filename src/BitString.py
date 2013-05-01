#! /usr/bin/env python

class BitString():
    def __init__(self):
        pass
    def compress(self,fasta):
        input_data = open(fasta,"r+")
        output_data = ""
        for line in input_data:
            for base in line:
                if base == "" or base == " " or base == '\n':
                    continue
                if base not in ["a","c","g","t","A","C","G","T"]:
                    print "Error: Malformed input"
                    exit()
                else:
                    if base == "a" or base == "A":
                        output_data += "00"
                    elif base == "c" or base == "C":
                        output_data += "01"
                    elif base == "g" or base == "G":
                        output_data += "10"
                    else:
                        output_data += "11"
        lasthas = 8 - len(output_data)%8
        lasthas = str(bin(lasthas))[2:]
        while(len(lasthas) != 8):
            lasthas = "0"+lasthas
        return lasthas+output_data
        
    def decompress(self,fasta):
        input_data = open(fasta,"rb+")
        output_data = ""
        decompressed = ""
        ba = bytearray(input_data.read())
        for byte in ba:
            outbin = bin(byte)[2:]
            while(len(outbin) != 8):
                outbin = "0"+outbin
            output_data += outbin
        lasthas = int(output_data[:8],2)
        output_data = output_data[8:]
        i = 0
        while(i < len(output_data)):
            if(i+1 < len(output_data) and output_data[i] == "0" and output_data[i+1] == "0"):
                decompressed += "a"
                i+=2
            elif(i+1 < len(output_data) and output_data[i] == "0" and output_data[i+1] == "1"):
                decompressed += "c"
                i+=2    
            elif(i+1 < len(output_data) and output_data[i] == "1" and output_data[i+1] == "0"):
                decompressed += "g"
                i+=2    
            elif(i+1 < len(output_data) and output_data[i] == "1" and output_data[i+1] == "1"):
                decompressed += "t"
                i+=2    
            else:
                break
        decompressed = decompressed[:len(decompressed)-lasthas/2]
        return decompressed
