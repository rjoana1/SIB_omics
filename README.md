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
O dataset utilizado encontra-se disponível na base de dados GEO com o número de acesso GSE157103. Consiste em dados clínicos recolhidos de 102 doentes com diagnóstico COVID-19 e 26 doentes com dificuldades respiratórias sem diagnóstico COVID-19. Fazem parte deste conjunto de dados, medições provenientes de análises laboratoriais e genómicas realizadas a amostras de sangue recolhidas destes doentes.

Dos dados clínicos disponíveis fazem parte as seguintes variáveis:

- necessida de internamento em unidade de cuidados intensivos (IUC);
- 4 scores de severidade da apresentação clínica da doença:
    - hospital-free days at day 45 (HDF-45), em que é atribuido um score com valor zero a doentes que permaneceram internados mais de 45 dias ou morreram durante a sua estadia no hospital, e valores de score mais elevados a doentes com internamentos hospitalares de menor duração e severidade da doença menor;
    - acute psysiologic assessment and chronic health evaluation (APACHE II);
    - sequential organ failure assessment (SOFA);
    - Charlson comorbidity index;
- número de dias ligado a ventilação mecânica;

Medições provenientes de análises laboratoriais: (verificar se estão todos e descrever sumariamente importancia)
- C-reactive protein (CRP), xxx ;
- D-dimer, um marcador da degradação do fibrinogénio;
- ferritina, xxx;
- lactato, xxx;
- procalcitonina, xxx;
- fibrinogénio, xxx.

O acesso a estes dados foi conseguido através do package em pyhton GEOparse (https://pypi.org/project/GEOparse/).

Dados de expressão normalizados (TPM) provenientes de RNA-sequencing (Illumina NovaSeq6000) de amostras de sangue destes doentes. A existência de um número de amostras inferior ao número de doentes (124) deve-se, provavelmente, à exclusão de duas amostras por falta de qualidade.
A matrix de contagem de genes por amostra foi downloaded directamente do site GEO (ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE157nnn/GSE157103/suppl/GSE157103%5Fgenes%2Etpm%2Etsv%2Egz).

## 1.3. Pipeline

## 1.4. Methods

## 1.5. Preliminary results

## 1.6. Next steps

## 1.7. References
