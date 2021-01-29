# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:58:30 2021

@author: Joana
"""

import gzip
import numpy as np
import pandas as pd


"""
Ler o file SOFT e exportar os seguintes dados:

GID : lista de identificadores de genes
SID : lista de identificadores de amostras
STP : lista of descrição das amostras
X   : array de valores de expressão de genes
"""

## Path
fname = "C:\\GSE157103_series_matrix.txt.gz"

## Aceder aos dados directamente do file gzip
with gzip.open(fname, "rt") as fid:

    SIF = {}
    list_samples=[]
    list_states=[]
    for line in fid:

        if line.startswith("!Series_sample_id"):
        #if line.startswith("!Sample_geo_accession"):
        #if line.startswith("!Sample_description	\"C1"):
            temp = line.split(" ")
            for i in range(1,len(temp)-1):
                sample=temp[i]
                list_samples.append(sample)
        
        if line.startswith("!Sample_characteristics_ch1	\"disease state"):
            temp2= line.split("\t")
            for i in range(1,len(temp2)):
                state=temp2[i].strip("\"")
                list_states.append(state)
        zip_iterator = zip(list_samples, list_states)
        SIF = dict(zip_iterator)
            
    #print(SIF)
    
    # lista nomes das amostras
    SID = list_samples
    #print(SID)
    
    ## sample state
    STP = list_states
    #print(STP)
    
rna_seq = pd.read_csv("GSE157103_genes.ec.tsv", sep='\t', index_col = 0)
#print(rna_seq.values)
X=rna_seq
GID=list(rna_seq.index)
#print(GID)

    ## The indices of samples for the COVID group
C = [i for i,x in enumerate(STP) if x == 'disease state: COVID-19']
print(len(C))
nC=len(C) ## Number of COVID samples
## The indices of samples for the non-COVID group
nC = [i for i,x in enumerate(STP) if x == 'disease state: non-COVID-19']
print(len(nC))
nnC=len(nC) ## Number of non-COVID samples

## Convert X to log scale
XL_temp = np.log(X) / np.log(2)
XL=XL_temp.values
#print(XL[0:3,C])

## Z-test statistics
MC = XL[:,C].mean(1) ## Mean of COVID samples
print(len(MC))

MnC = XL[:,nC].mean(1) ## Mean of non-COVID samples
print(len(MnC))
VC = XL[:,C].var(1)  ## Variance of COVID samples
print(len(VC))
VnC = XL[:,nC].var(1)  ## Variance of non-COVID samples
print(len(VnC))

Z = (MC - MnC) / np.sqrt(VC/nC + VnC/nnC)
print(Z)

