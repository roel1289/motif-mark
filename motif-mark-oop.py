#!/usr/bin/env python

import argparse
import re
import cairo
import math


def get_args():
    parser = argparse.ArgumentParser(description="A program to hold input + output file name")
    parser.add_argument("-f", "--fasta", help="designates absolute file path to fasta file", type = str)
    parser.add_argument("-m", "--motifs", help="designates absolute file motifs file", type = str)
    return parser.parse_args()
    
args = get_args()

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

#draw a rectangle
context.rectangle(100,100,150,350)        #(x0,y0,x1,y1)
context.fill()

#write out drawing
surface.finish()