# 1. Análise de datasets de expressão relacionados com Covid19

## 1.1. Objetivos principais/ questões motivadoras

A apresentação clínica da infecção por COVID-19 é muito diversa, podendo variar de um estado assimtomático para uma condição letal. Dados recentes indicam que a severidade da doença depende, para além de factores virais, de factores associados ao hospedeiro. Diferentes assinaturas genéticas, patologicas e clínicas parecem conseguir diferenciar doentes com diagnóstico de COVID-19 e doentes sem esta condição.
O objectivo deste trabalho consiste em tentar compreender melhor respostas individuais, a nível molecular, que possam explicar estas diferenças clínicas observadas.
Para tal, recorreu-se a um dataset composto por dados clínicos de 128 doentes com e sem diagnóstico de COVID-19. Adicionalmente, dados de RNA-sequencing provenientes de amostras de sangue recolhidas destes doentes foram usados para criar profiles moleculares de cada doente. 
Pretende-se, neste trabalho, responder concretamente às seguintes questões:
- Caracterização do fenótipo de hipercoagulação caracteristicos de doentes com diagnóstico COVID-19 (D-dimer, marcador da degradação do fibrinogénio)
- Correlação entre a abundândia de biomarcadores com dados clínicos e outcome de pacientes com diagnóstico de COVD-19
- Severidade da apresentação clínica e sua associação com um perfil molecular COVID
- Biological pathways associados à resposta do hospediro ao SARSCoV-2 e à severidade da doença
- Análise dos processo biologicos desregulados em doentes COVID-19
- modelo preditivo da severidade e outcome de pacientes com diagnóstico de COVID-19 baseado em dados omicos

## 1.2. Dataset
- Groups:
    - 102 COVID-19 and 26 non-COVID-19 patient samples
    - Intensive Care Unit (ICU) and Non-ICU patients

### 1.2.1. Leukocyte mRNA expression dataset: GEO: GSE157103
    - RNA-seq
    - 13263 transcripts

## 1.3. Pipeline

## 1.4. Methods


### 1.4.1. COVID-19 molecular landscape and factors associated with higher severity
    - PCA; agrupamento de amostras de doentes baseado na severidade da doença (score HFD-45) e estado (COVID-19 versus non-COVID-19)
### 1.4.2. Gain biological insight into the host’s response to SARSCoV-2 and pathways influencing its severity
    - supervised analysis: univariate and multivariate regression to identify features that associate with
    (1) COVID-19 status
    (2) HFD-45
    - Significant changes in biomarkers ferritin (ng/ml),crp (mg/l),ddimer (mg/l_feu), procalcitonin (ng/ml), lactate (mmol/l)', fibrinogen associated with COVID-19.
        - determined by ANOVA and log-likelihood ratio tests, incorporation of potentially confounding variables, such as sex, age, and ICU status
    - GO and molecular class enrichment analysis
### 1.4.3. Biological Processes Dysregulated in COVID-19 Patients
    - mean fold-change in abundance of GO-associated transcripts, plotted against adjusted p values of significance with COVID-19

## 1.5. Preliminary results

## 1.6. Next steps

## 1.7. References
