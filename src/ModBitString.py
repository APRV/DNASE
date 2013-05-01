#! /usr/bin/env python

import heapq

class ModBitString():
    def __init__(self):
        pass
    def makeHuffTree(self,symbolTupleList):                                                                               
        trees = list(symbolTupleList)                                                                                 
        heapq.heapify(trees)                                                                                          
        while len(trees) > 1:                                                                                         
            childR, childL = heapq.heappop(trees), heapq.heappop(trees)                                                
            parent = (childL[0] + childR[0], childL, childR)                                                           
            heapq.heappush(trees, parent)                                                                              
        return trees[0]  
                                                                                             
    def onechange(self,data1,data2):
        if(len(data1) != len(data2)):
            return 0
        n = len(data1)
        change = 0
        changepos = 0
        changechar = 0
        for i in range(0,n):
            if(data1[i] != data2[i]):
                change += 1
                changepos = i
                changechar = data2[i]
            if(change > 1):
                return 0
        return [changepos,changechar]

    def krepeats(self,data,k):
        pw = []
        cw = []
        m = 3
        kwords = {}
        dstr = ""
        for line in data:
            for base in line:
                dstr += base
        for i in range(0,k):
            pw.append(data[i])
        i = k
        counter = 0
        repeatcount = 0
        repeatlocation = 0
        while(i < len(data) - k):
            if(counter < k):
                cw.append(data[i])
                counter+=1
            i+=1
            if(counter == k):
                counter = 0
                if(cw == pw or self.onechange(cw,pw) != 0):
                    repeatcount += 1
                    if(repeatcount > 2):
                        repeatstr = ("").join(pw)+str(repeatlocation)
                        if(repeatstr not in kwords):
                            kwords[repeatstr] = repeatcount 
                        else:
                             kwords[repeatstr] += 1
                else:
                    pw = cw
                    repeatcount = 0
                    repeatlocation = i-k
                cw = []
        print kwords
        return kwords

    def makeHuffTable(self,huffTree,huffTab,prefix = ''):
        if(len(huffTree) == 2):
            huffTab[huffTree[1]] = prefix
        else:
            self.makeHuffTable(huffTree[1], huffTab,prefix + '0')
            self.makeHuffTable(huffTree[2], huffTab,prefix + '1')
    def compress(self,fasta):
        input_data = open(fasta,"r+")
        output_data = ""
        dstr = ""
        acount = 0
        ccount = 0
        gcount = 0
        tcount = 0
        prevchar = "z"
        dinucleotide = {}
        dinucleotide["aa"] = 0
        dinucleotide["ac"] = 0
        dinucleotide["ag"] = 0
        dinucleotide["at"] = 0
        dinucleotide["ga"] = 0
        dinucleotide["gc"] = 0
        dinucleotide["gg"] = 0
        dinucleotide["gt"] = 0
        dinucleotide["ca"] = 0
        dinucleotide["cc"] = 0
        dinucleotide["cg"] = 0
        dinucleotide["ct"] = 0
        dinucleotide["ta"] = 0
        dinucleotide["tc"] = 0
        dinucleotide["tg"] = 0
        dinucleotide["tt"] = 0

        huffTable = {}                                                                                                                                      
        huffTable["aa"] = 0                                                                                                                                 
        huffTable["ac"] = 0                                                                                                                                 
        huffTable["ag"] = 0                                                                                                                   
        huffTable["at"] = 0                                                                                                                                 
        huffTable["ga"] = 0                                     
        huffTable["gc"] = 0                                                                                                                                 
        huffTable["gg"] = 0     
        huffTable["gt"] = 0                                                                                                                                         
        huffTable["ca"] = 0                                                                                                                                 
        huffTable["cc"] = 0                                                                                                                                         
        huffTable["cg"] = 0                                                                                                                                     
        huffTable["ct"] = 0                                                                                                                                 
        huffTable["ta"] = 0                                                                                                                                 
        huffTable["tc"] = 0                                                                                                                                 
        huffTable["tg"] = 0                                                                                                                                 
        huffTable["tt"] = 0     


        totalcount = 0
        skip = True
        for line in input_data:
            for base in line:
                if base == "" or base == " " or base == '\n':
                    continue
                if base not in ["a","c","g","t","A","C","G","T"]:
                    print "Error: Malformed input"
                    exit()
                else:
                    dstr += base
                    if base == "a" or base == "A":
                        #output_data += "00"
                        if(not skip):
                            dinucleotide[prevchar+"a"] += 1
                            skip = True
                        else:
                            skip = False
                        prevchar = "a"
                        acount += 1
                    elif base == "c" or base == "C":
                        #output_data += "01"
                        if(not skip):
                            dinucleotide[prevchar+"c"] += 1
                            skip = True
                        else:
                            skip = False
                        prevchar = "c"
                        ccount += 1
                    elif base == "g" or base == "G":
                        #output_data += "10"
                        if(not skip):
                            dinucleotide[prevchar+"g"] += 1
                            skip = True
                        else:
                            skip = False
                        prevchar = "g"
                        gcount += 1
                    else:
                        #output_data += "11"
                        tcount += 1
                        if(prevchar != "z" and not skip):
                            dinucleotide[prevchar+"t"] += 1
                            skip = True
                        else:
                            skip = False
                        prevchar = "t"
                    totalcount += 1

        total = sum(dinucleotide.values())
        print dinucleotide
        probList = [x/float(total) for x in dinucleotide.values()]
        huffmanData = []
        for i in range(0,len(probList)):
            huffmanData.append((probList[i],dinucleotide.keys()[i]))
        huffTree = self.makeHuffTree(huffmanData)
        self.makeHuffTable(huffTree,huffTable,'')
        print output_data
        prevchar = 'z'
        skip = True
        for base in dstr:
            if base == "a" or base == "A":
                if(not skip):
                    output_data += huffTable[prevchar+"a"]
                    skip = True
                else:
                    skip = False
                prevchar = "a"
            elif base == "c" or base == "C":
                if(not skip):
                    output_data += huffTable[prevchar+"c"]
                    skip = True
                else:
                    skip = False
                prevchar = "c"
            elif base == "g" or base == "G":
                if(not skip):
                    output_data += huffTable[prevchar+"c"]
                    skip = True
                else:
                    skip = False
                prevchar = "g"
            else:
                if(not skip):
                    output_data += huffTable[prevchar+"t"]
                    skip = True
                else:
                    skip = False
                prevchar = "t" 
        
        lasthas = 8 - len(output_data)%8
        lasthas = str(bin(lasthas))[2:]
        while(len(lasthas) != 8):
            lasthas = "0"+lasthas
        self.krepeats(dstr,4)
        #exit()
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
