# Agrupamento de Pessoas por Perfis Compatíveis

## Descrição do Projeto

Este projeto utiliza técnicas de **Machine Learning** para agrupar pessoas com perfis compatíveis em mesas. A ideia é otimizar a disposição das pessoas em grupos, considerando características pessoais e preferências, para promover interações mais harmoniosas e produtivas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada para implementar o algoritmo e processar os dados.
- **NumPy**: Biblioteca para manipulação de arrays e operações matemáticas.
- **Pandas**: Biblioteca utilizada para análise e manipulação de dados tabulares.
- **Scikit-learn**: Biblioteca que fornece ferramentas simples e eficientes para análise preditiva e machine learning, incluindo algoritmos de clustering.
- **SciPy**: Biblioteca para computação científica que inclui a função `linear_sum_assignment` para resolver problemas de otimização combinatória.
- **Pickle**: Módulo em Python para serialização de objetos, utilizado para armazenar e carregar parâmetros de treinamento.
- **OpenPyXL**: Biblioteca para ler e escrever arquivos Excel, usada para avaliar os agrupamentos anteriores.

## Conceitos Aplicados

### Clustering

O projeto utiliza o algoritmo **K-Means** para a clusterização das pessoas com base em características categóricas e numéricas. O K-Means é um método popular de agrupamento que tenta dividir um conjunto de dados em `k` grupos, onde cada ponto de dados pertence ao grupo cujo centroide é mais próximo.

### Pré-processamento de Dados

Os dados de entrada passam por um processo de pré-processamento que inclui:
- **Codificação One-Hot**: Converte variáveis categóricas em uma forma que pode ser fornecida ao modelo de machine learning.
- **Normalização**: Escala os dados numéricos para garantir que todas as características contribuam igualmente para a análise.

### Atribuição de Grupos

Após a clusterização, o algoritmo utiliza a **atribuição de custo** para organizar as pessoas nos grupos de forma a minimizar a distância entre os perfis e os grupos, assegurando que as interações sejam otimizadas.

### Balanceamento de Grupos

Uma função específica garante que a composição dos grupos mantenha um equilíbrio entre introvertidos e extrovertidos, promovendo uma dinâmica de grupo saudável.

## Justificativa da Escolha das Tecnologias

As tecnologias escolhidas foram selecionadas com base na facilidade de uso, eficiência e popularidade na comunidade de ciência de dados. Python, com suas bibliotecas robustas, permite a implementação rápida de algoritmos de machine learning e manipulação de dados, facilitando a prototipagem e a iteração do projeto.
