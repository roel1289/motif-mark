# Lab Notebook for Motif-mark assignment  


## 2/19/24  
Making conda environment to hold pycairo:   
```
# create conda environment with python 3:
conda create -n bgmp-pycairo python=3

# activate pycairo environment  
conda activate bgmp-pycairo

# install pycairo program  
conda install -c conda-forge pycairo
```  

Followed example pycairo code to create a rectangle and line

## 2/29/24  

testing code using this command:  

```
rm -f example2.pdf ; ./motif-mark-oop.py -f Figure_1.fasta -m Fig_1_motifs.txt -w test.fa -ol test.fa
```