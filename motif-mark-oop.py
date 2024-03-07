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

#############
## Globals ##
#############

motifDict = dict()

motifRegDict = dict()
motifRegDict = {
    "A": "[aA]",
    "T": "[tT]",
    "G": "[gG]",
    "C": "[cC]",
    "U": "[tuTU]",
    "W": "[atAT]",
    "S": "[cgCG]",
    "M": "[acAC]",
    "K": "[gtGT]",
    "R": "[agAG]",
    "Y": "[ctCT]",
    "B": "[cgtCGT]",
    "D": "[agtAGT]",
    "H": "[actACT]",
    "V": "[acgACG]",
    "N": "[acgtACGT]"
}

#image dimensions:
width, height = 1000, 1000
#setting up pycairo image dimensions:
surface = cairo.PDFSurface("Figure_1.pdf", width, height)
context = cairo.Context(surface)

#counter to increment the different RGBA colors: 
color_counter = 0


###############
## Functions ##
###############

#turn fasta into only a one line fasta:
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

#Add motifs to a dictionary
def convert_motif(string):
    string = string.upper()
    motif = ""
    for x in string:
        motif += motifRegDict[x]
    return(motif)


#############
## Classes ##
#############
# This is where I define my classes (yes, including both attributes and methods).

######## class gene ##########
class Gene:
    def __init__(self, name: str, length: int ) -> None:
        self.name = name
        self.length = length

    #methods
    def draw_gene(self, x: int, y: int, name: str, gene_length: int):
        '''This behavior draws the gene as a black line. The line will be proportionally as long as the gene.'''
        context.set_line_width(3)
        print(f'debug 123 {x=}, {y=}, {x+gene_length=}')
        context.set_source_rgba(0, 0, 0, 1)
        context.move_to(x,y)        #(x,y)
        context.line_to(x + gene_length,y)
        context.stroke()

        #print gene name
        context.move_to(x, y-10) 
        context.show_text(name)
        context.stroke()

########## class exon ################
class Exon:
    def __init__(self, start: int, end: int, color: str, gene: str) -> str:
        self.start = start
        self.end = end
        self.color = color
        self.gene = gene

    #methods
    def draw_exon(self, x: int, y: int, exon_len: int):
        '''This behavior draws the exon.'''
        print(f'debug EXON: {x=}, {y=}, {x+exon_len=}')
        context.set_source_rgba(0, 0, 0, 1)
        context.set_line_width(30)
        context.move_to(x,y)        #(x,y)
        context.line_to(x + exon_len, y)
        context.stroke()

############### class motif ##############

class Motif: 
    def __init__(self, motif_seq: str, gene: str, start: int, length: int, color: str) -> str:
    #attributes:
        self.motif_seq = motif_seq
        self.gene = gene
        self.start = start
        self.length = length
        self.color = color

    def __str__(self) -> str:
        return f"{self.gene}, {self.start}, {self.length}, {self.color}"
    
    #methods:
    def draw_motif(self, x: int, y: int, motif_len: int):
        '''draw the motif'''
    
        # graphing motif:
        context.set_source_rgba(colorTuple[0], colorTuple[1], colorTuple[2])
        
        context.set_line_width(17)
        context.move_to(x,y)        #(x,y)
        context.line_to(x + motif_len, y)
        context.stroke()

        #making key
        context.set_source_rgba(0, 0, 0, 1)
        context.move_to(20, 435) 
        context.show_text("Key")
        context.stroke()

        #add name into legend
        context.set_source_rgba(colorTuple[0], colorTuple[1], colorTuple[2], .8)
        context.move_to(20, 445 + (z)) 
        context.show_text(f"{motif}")
        #making box for line
        context.set_line_width(17)
        context.move_to(len(motif)+100, 445 + (z))        #(x,y)
        context.line_to((100+len(motif))+len(motif), 445 + (z))
        context.stroke()
        context.stroke()


##########
## Main ##
##########
# The "main" section. Basically, what gets run goes here (and obviously uses
# directly or indirectly everything above it).
    

#maybe will make a function that takes a oneline fasta and gives a list of genes:
def build_genes(oneline_fasta_filename: str) -> list[Gene]:
    pass 

#getting the motifs:
with open(args.motifs, "r") as input_motifs:
    dictCounter = 0
    while True:
        line = input_motifs.readline().strip()
        if(line == ""):
            break
        dictCounter += 1
        print(f'--->motifs:{dictCounter=}')
        # match_gene_name = re.findall(r'>([A-Za-z0-9]+)', line)
        # match_motif = re.search(r'(([c|t]gc[c|t])', line)



        # motifDict[line] = ((len(line)*20/255),(len(line)*25)/255,40/255,.5)
        # motifDict[line] = (((len(line)/2)**5)/255,(((len(line)/2)**3)/255),((len(line)/2)**5)/255,.5)
        motifDict[line] = ((dictCounter*100)/255, (dictCounter*60)/255, (dictCounter*40)/255)

    print(motifDict.values())
        




# Turning fasta file so that it only has one line of
oneline_fasta(f)

with open(args.oneLine, "r") as input_fasta:
    ### genes ###
    i=0
    exon_counter = 0
    while True:
        
        header = input_fasta.readline().split()
        sequence = input_fasta.readline().split()

        if(header == []):
            break

        # print(header)
        #print(header[0])
        #print(sequence)

        gene_name = header[0][1:]
        print(f'--------------{gene_name=}----------------------')

        gene_len = len(sequence[0])
        gene = Gene(header[0][1:], gene_len)
        gene.draw_gene(20, 50+i, header[0][1:], gene_len)
        
        print(f'{gene_len=}')


        ### exons ###
        #extracting only capital letters (exons)
        p = re.compile("[A-Z]+")
        for m in p.finditer(sequence[0]):
            #print(m.span())
            exon_x = m.span()[0]
            exon_y = m.span()[1]
        
        # print(exon_x)
        # print(exon_y)


        exon_len = exon_y - exon_x #exon len = end - start
        print(f'{exon_len=}')
        


        exon1 = Exon(0, exon_len, "red", gene_name)
        # x: int, y: int, exon_len: int
        exon1.draw_exon(20+exon_x, 50+i, exon_len)

        ### Motifs ###
        z = 0
        for motif in motifDict:
            print(f'{motif=}')
            print(f'RGBA = {motifDict[motif]}')
            colorTuple = motifDict[motif]
            motif_re = re.compile(convert_motif(f"{motif}"))
            z += 19
            for m in motif_re.finditer(sequence[0]):
                #print(m.span())
                motif_len = m.span()[1] - m.span()[0]
                motif4 = Motif(f"{motif}", "gene", 1,2,"green")
                motif4.draw_motif(20 + m.span()[0], 50+i, motif_len)
            
        


        i += 100
        print(f'i={i}')



context.fill()
surface.finish()





motifDict = dict()



# ./motif-mark-oop.py -f Figure_1.fasta -m Fig_1_motifs.txt -w oneline.fa -ol oneline.fa