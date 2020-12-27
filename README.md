# 1. Análise de datasets de expressão relacionados com Covid19

## 1.1. Objetivos principais/ questões motivadoras

### 1.1.1. COVID-19 molecular landscape and factors associated with higher severity

### 1.1.2. Gain biological insight into the host’s response to SARSCoV-2 and pathways influencing its severity

### 1.1.3. Biological Processes Dysregulated in COVID-19 Patients

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
    - PCA; grouping of patient samples based on severity (HFD-45); grouping based on status (COVID-19 versus non-COVID-19)
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
