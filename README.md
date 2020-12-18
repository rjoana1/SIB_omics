# SIB_omics
Análise de datasets de expressão relacionados com Covid19

## Package pandas, download dos files directamente da página do NCBI
- tabelas de counts (19472 rows × 126 columns):

rna_seq_tmp = pd.read_csv("GSE157103_genes.tpm.tsv", sep='\t', index_col = 0)

- leitura do ficheiro soft com informação sobre o dataset:

soft = pd.read_csv("GSE157103_family.soft", sep='\t', index_col = 0)

- upload dos metadados (SraRunTable.txt; 252 rows × 37 columns):

metadados = pd.read_csv("SraRunTable.txt", sep=',', index_col = 0)

Aqui estavamos à espera de 126 amostras, temos 252 SRR samples e 37 colunas de metadados.

## Package GEOparse

- GEO objects; class GEOparse.BaseGEO
- main attributes: name and metadata
- metadata is a dictionary of useful information about samples which occurs in the SOFT file with bang (!) in the beginning.
  - each value of this dictionary id a list (even with one element).

gse157103 = GEOparse.get_GEO("GSE157103")

- metadados referentes às 126 amostras:

gse157103.phenotype_data (126 rows × 61 columns)

- matrizes de contagens: gsm.table vazia:

for gsm_name, gsm in gse157103.gsms.items():
  print(gsm_name,"--", gsm)
  print("metadata: \n",gsm.metadata)
  for key, value in gsm.metadata.items():
   print("gsm.metadata.items \n",key, value)
   print("Table data:",gsm)
   print(gsm.columns)

## R, library GEOquery

- metadados (126x83)

Surpreendentemente obtivemos mais metadados, 83.
