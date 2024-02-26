#!/usr/bin/env python

import argparse
import re
import cairo
import math


def get_args():
    parser = argparse.ArgumentParser(description="A program to hold input + output file name")
    parser.add_argument("-f", "--fasta", help="designates absolute file path to fasta file", type = str)
    parser.add_argument("-m", "--motifs", help="designates absolute file motifs file", type = str)
    parser.add_argument("-w", "--write", help="write", type = str)
    parser.add_argument("-ol", "--oneLine", help="One line fasta file", type = str)
    return parser.parse_args()
    
args = get_args()
f = args.fasta
############################ example of line and rectangle #########################################
#### drawign a line and rectangle
width, height = 256, 256

#create the coordinates to display your graphic, desginate output
surface = cairo.PDFSurface("example.pdf",width, height)

#create the coordinates you will be drawing on (like a transparency) - you can create a transformation matrix
context = cairo.Context(surface)

#Need to tell cairo where to put the brush, the color and width, and the shape you want it to draw
#draw a line
context.set_line_width(1)
context.move_to(50,25)        #(x,y)
context.line_to(450,25)
context.stroke()

#set color
context.set_source_rgb(0.4, 0.9, 0.4)

#draw a rectangle
context.rectangle(100,100,150,350)        #(x0,y0,x1,y1)
context.fill()

#write out drawing
surface.finish()

########################################################################



### assinging classes and objects
# create class Motif
class Motif: 
    def __init__(self, motif_seq, gene, start, length, color) -> str:
    #methods
        self.motif_seq = motif_seq
        self.gene = gene
        self.start = start
        self.length = length
        self.color = color

    def __str__(self) -> str:
        return f"{self.gene}, {self.start}, {self.length}, {self.color}"
    

#m1 = Motif("INSR", 100, 10, "red" )
#print(m1)



# motif_ygcy = Motif("ygcy")
# motif_GCAUG = Motif("GCAUG")
# motif_catag = Motif("catag")
# motif_YYYYYYYYYY = Motif("YYYYYYYYYY")


class Exon:
    def __init__(self, start, end, direction, color) -> str:
        pass


class Intron:
    def __init__(self) -> str:
        pass


class Gene:
    def __init__(self, name ) -> None:
        pass
    def counter(self, name):
        pass


def oneline_fasta(f):
    '''Turn seq of fasta file into one line.'''
    with open(f, "r") as rf, open(args.write,"w") as wf:
        seq = ''
        while True:
            line = rf.readline().strip()
            if not line:
                break
            if line.startswith(">"):
                if seq != "":
                    wf.write(seq + "\n") 
                seq = ''
                wf.write(line + "\n") 
            else:
                seq += line 
        wf.write(seq)

oneline_fasta(f)



with open(args.oneLine, "r") as input_fasta:
    while True:
        line = input_fasta.readline().strip()
        if(line == ""):
            break
        match_gene_len = re.findall(r'^>.+?\n([agtcyAGTCY0-9]+)', line) #^>.+?\n([agtcyAGTCY0-9]+)  #^>.+([\s\S]+)
        print(match_gene_len)















#####making motif dictionary where key = motif, and value and color
#ygcy = yellow
#GCAUG = green
#catag = red
#YYYYYYYYYY = white

# Note: Y = T/C


motifDict = dict()

# with open(args.motifs, "r") as input_motifs:
#     while True:
#         line = input_motifs.readline().strip()
#         if(line == ""):
#             break
        
#         match_gene_name = re.findall(r'>([A-Za-z0-9]+)', line)
#         match_motif = re.search(r'(([c|t]gc[c|t])', line)



#         motifDict[line] = len(line)

#     print(motifDict)
        


