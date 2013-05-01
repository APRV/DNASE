#! /usr/bin/env python

import operator

class NewBitString():
    def __init__(self):
        pass
    def krepeats(self,data,k):
        pw = []
        cw = []
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
                if(cw == pw):
                    repeatcount += 1
                    if(repeatcount > 3):
                        repeatstr = ("").join(cw)+str(repeatlocation)
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

    def findtop(self,data,k):
        i = 0
        seqlist = {}
        while(i < len(data)):
            currentseq = data[i:i+k]
            if(currentseq not in seqlist):
                seqlist[currentseq] = 1
            else:
                seqlist[currentseq] += 1
            i+=k
        print seqlist
        return seqlist

    def compress(self,fasta):
        input_data = open(fasta,"r+")
        output_data = ""
        dstr = ""
        for line in input_data:
            for base in line:
                if base == "" or base == " " or base == '\n':
                    continue
                if base not in ["a","c","g","t","A","C","G","T"]:
                    print "Error: Malformed input"
                    exit()
                else:
                    dstr += base
        top2 = self.findtop(dstr,2)
        sortedTop2 = sorted(top2.iteritems(),key=operator.itemgetter(1),reverse=True)
        top3 = self.findtop(dstr,3)
        sortedTop3 = sorted(top3.iteritems(),key=operator.itemgetter(1),reverse=True)
        i = 0
        bases2 = [x[0] for x in sortedTop2][0:4]
        bases3 = [x[0] for x in sortedTop3][0:8]
        print bases2
        print bases3
        bases1 = ['a','c','g','t']
        print sortedTop2
        i = 0
        threecounter = 0
        twocounter = 0
        onecounter = 0
        top2 = {}
        while(i < len(dstr)):
            if(dstr[i:i+3] in bases3):
                i+=3
            else:
                if(dstr[i:i+2] not in top2):
                    top2[dstr[i:i+2]] = 1
                else:
                    top2[dstr[i:i+2]] += 1
                i+=2
        sortedTop2 = sorted(top2.iteritems(),key=operator.itemgetter(1),reverse=True) 
        bases2 = [x[0] for x in sortedTop2][0:4]
        print bases2
        i = 0
        while(i < len(dstr)):
            if(dstr[i:i+3] in bases3):
                binm = str(bin(bases3.index(dstr[i:i+3])))[2:].zfill(4)
                i+=3
                threecounter+=1
            elif(dstr[i:i+2] in bases2):
                binm = str(bin(bases2.index(dstr[i:i+2])+4))[2:].zfill(4)
                i+=2
                twocounter += 1
            else:
                binm = str(bin(bases1.index(dstr[i])+8))[2:].zfill(4)
                i+=1
                onecounter += 1
            output_data += binm
            #print binm
        print threecounter
        print twocounter
        print onecounter
        lasthas = 8 - len(output_data)%8
        lasthas = str(bin(lasthas))[2:]
        while(len(lasthas) != 8):
            lasthas = "0"+lasthas
        self.krepeats(dstr,4)
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
