# 1. Análise de datasets de expressão relacionados com Covid19

## 1.1. Objetivos principais/ questões motivadoras

A apresentação clínica da infecção por COVID-19 é muito diversa, podendo variar de um estado assimtomático para uma condição letal (ref). Dados recentes indicam que a severidade da doença depende, para além de factores virais, de factores associados ao hospedeiro (ref). Diferentes assinaturas genéticas, patologicas e clínicas parecem conseguir diferenciar doentes com diagnóstico de COVID-19 e doentes sem esta condição (ref).
O objectivo deste trabalho consiste em tentar compreender melhor respostas individuais, a nível molecular, que possam explicar estas diferenças clínicas observadas. Adicionalmente, pretende-se criar um modelo de machine learning que permita prever a severidade da infecção COVID-19 com base em dados omicos, fisiológicos e clínicos.
Para tal, recorreu-se a um dataset composto por diversos dados clínicos pertencentes a 128 doentes, com e sem diagnóstico de COVID-19. Adicionalmente, foram utilizados dados de RNA-sequencing e dados laboratoriais provenientes de amostras de sangue recolhidas destes doentes.
Pretende-se, neste trabalho, responder concretamente às seguintes questões:
- Dterminar a existência de associação entre biomarcadores ou perfil molecular com diagnóstico de COVD-19 e severidade da apresentação clínica por forma a compreender que factores estão associados a uma maior severidade da apresentação clínivca desta doença;
- Perceber que biological pathways se encontram associados à resposta do hospediro ao SARSCoV-2 e à severidade da doença no sentido de eludidar potenciais targets terapêuticos;
- Prever a severidade da doença e outcome dos pacientes com diagnóstico de COVID-19 com base em dados omicos, clínicos e laboratoriais disponíveis por forma a priorizar doentes e seus tratamentos.

## 1.2. Dataset
O dataset utilizado consiste dados clínicos recolhidos de 102 doentes com diagnóstico COVID-19 e 26 doentes com dificuldades respiratórias sem diagnóstico COVID-19. Fazem parte deste conjunto de dados, medições provenientes de análises laboratoriais e genómicas realizadas a amostras de sangue recolhidas destes doentes.
Dos dados clínicos disponíveis fazem parte as seguintes variaveis:
- internamento em unidade de cuidados intensivos;
- necessidade de ventilador;
- scores de severidade da apresentação clínica da doença:
    - hospital-free days at day 45 (HDF-45), em que é atribuido um score com valor zero a doentes que permaneceram internados mais de 45 dias ou morreram durante a sua estadia no hospital, e valores de score mais elevados a doentes com internamentos hospitalares de menor duração e severidade da doença menor.
    
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
