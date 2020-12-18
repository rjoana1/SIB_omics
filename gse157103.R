library(GEOquery)
gse_F <- getGEO("GSE157103",GSEMatrix=FALSE)
#gse_F
Meta(gse_F)

names(GSMList(gse_F))
GSMList(gse_F)[[1]]
names(GPLList(gse_F))


gse157103 <- getGEO('GSE157103',GSEMatrix=TRUE)
gse157103

table=as.data.frame(gse157103)
dim(table)
show(pData(phenoData(gse157103[[1]]))[1:5,c(1,6,8)])
show(pData(phenoData(gse157103[[1]]))[1:5,1:37])
show(pData(phenoData(gse157103[[1]]))[1:5,6:10])
show(pData(phenoData(gse157103[[1]]))[1:5,81:83])