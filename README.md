# Strassen-Algorithm

Atividade da disciplina Estrutura de Dados e Complexidade de Algoritmos.

### Descrição

Para esta atividade foram implementadas dois algoritmos de multiplicação de matrizes, um algoritmo ingênuo, mais conhecido como naive, e o algoritmo de Strassen em duas versões, a primeira considera como condição de parada da recursividade uma matriz nxn com n <= 2, usando a equação de multiplicações de matrizes 2x2 para calcular o caso base, e uma versão híbrida que chama o algoritmo naive para executar multiplicações de matrizes de ordem menor que 2⁵.

### Execução

O projeto tem como entrada um arquivo de texto chamado input.txt contendo as informações:

k_max -> Define a maior order de matrizes que será executada. A ordem é dada por 2^k_max

r -> Define o número de multiplicações que será executada em cada ordem

[min, max] -> Define o intervalo dos valores que irão conter na matriz

Exemplo:

```
10
10
0 100
```

Para executar o código adicione o caminho para o arquivo input ao final do comando de execução. Exemplo:

```
python /home/user/documentos/Strassen-Algorithm/main.py ./input.txt
```

## Observações

Numa tentativa de otimizar o tempo de execução do código na `branch` `hotfix/using-list-comprehensions` alguns loops e construções de matrizes foram substituidas por listas de compressão ou *list comprehensions*. Porém depois de alguns testes nenhuma melhora significativa foi observada.