#!/usr/bin/env python

####################
## Future Imports ##
####################

from __future__ import annotations

#############
## Imports ##
#############

import argparse
import re
import cairo
import math

###############
## Arguments ##
###############

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
#width, height = 256, 256
width, height = 1000, 1000

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


#############
## Globals ##
#############

motifDict = dict()

###############
## Functions ##
###############

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


#############
## Classes ##
#############
# This is where I define my classes (yes, including both attributes and methods).

class Motif: 
    def __init__(self, motif_seq, gene, start, length, color) -> str:
    #attributes:
        self.motif_seq = motif_seq
        self.gene = gene
        self.start = start
        self.length = length
        self.color = color

    def __str__(self) -> str:
        return f"{self.gene}, {self.start}, {self.length}, {self.color}"
    
    #methods:
    #def draw(self):




#m1 = Motif("INSR", 100, 10, "red" )
#print(m1)



# motif_ygcy = Motif("ygcy")
# motif_GCAUG = Motif("GCAUG")
# motif_catag = Motif("catag")
# motif_YYYYYYYYYY = Motif("YYYYYYYYYY")


class Exon:
    def __init__(self, start, end, color, gene) -> str:
        self.start = start
        self.end = end
        self.color = color


class Gene:
    def __init__(self, name, length ) -> None:
        self.name = name
        self.length = length

    #methods
    def draw_gene(self, x, y, name, gene_length):
        surface = cairo.PDFSurface("example2.pdf",width, height)
        context = cairo.Context(surface)
        context.set_line_width(1)
        context.move_to(x,y)        #(x,y)
        context.line_to(x + gene_length,y)
        context.move_to(20, 40) 
        context.show_text(name)
        context.stroke()
        context.fill()


        
    #instances:
gene1 = Gene("INSR", 548)
gene1.draw_gene(100,200,"test", 100)

    
    # def counter(self, name):
    #     pass


##########
## Main ##
##########
# The "main" section. Basically, what gets run goes here (and obviously uses
# directly or indirectly everything above it).
    


with open(args.oneLine, "r") as input_fasta:
    i=0
    while True:
        
        header = input_fasta.readline().split()
        sequence = input_fasta.readline().split()

        if(header == []):
            break

        print(header)
        # print(sequence)

        gene_len = len(sequence[0])
        gene2 = Gene(header[0][1:], gene_len)
        gene2.draw_gene(20,50, header[0][1:],gene_len)
        
        print(gene_len)




        # match_gene_len = re.findall(r'^>.+?\n([agtcyAGTCY0-9]+)', line) #^>.+?\n([agtcyAGTCY0-9]+)  #^>.+([\s\S]+)
        # print(match_gene_len)

#NOTES: make a class of gene in the main part, and then use the draw_gene function to draw the gene












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
        


# ./motif-mark-oop.py -f Figure_1.fasta -m Fig_1_motifs.txt -w test.fa -ol test.fa
