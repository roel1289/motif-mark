# OOP Motif Mark   

The goal of this python script is to use object-oriented code to visualize motifs on sequences. I will receive a text file containing the motifs as well as a fasta file to use. Additionally, I will use a program called pycairo to visualize motifs.  

The script is able to receive as many motifs as needed and can handle up to 10 sequences. For each FASTA file provided, the script will output a .png file with the same pre-fix. So for example, if the inputted fasta is called `Figure_1.fasta`, the output will be `Figure_1.png`.

## How to run script:   
In order to run the script, it is necessary to have `python 3` as well as `pycairo` downloaded. Here is how I generated a conda environiment to do this:  
```
conda create -n bgmp-pycairo python=3
conda activate bgmp-pycairo
conda install -c conda-forge pycairo
```  
To run the script, there are two options.  
    * `-f`: designated fasta file
    * `-m`: designated file containing the motifs  

Here is how to run the script from the commandline:   
```./motif-mark-oop.py -f <fasta file> -m <motif file>```
