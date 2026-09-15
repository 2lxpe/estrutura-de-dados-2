# Atividade Prática - Análise de Algoritmos de Ordenação
 alunos: Jorge Luis Soares Dos Santos e Felipe Falcão Campelo | turma:d2
 
Trabalho da disciplina comparando Bubble Sort, Insertion Sort, Selection Sort e Quick Sort, contando comparações e trocas/movimentações para vetores de 10, 20 e 1.000 elementos.

## Estrutura do projeto

```
bubble_sort.py     -> função bubble_sort()
insertion_sort.py  -> função insertion_sort()
selection_sort.py  -> função selection_sort()
quick_sort.py       -> função quick_sort() (usa particiona() como auxiliar)
main.py             -> Etapa 3: gera os vetores aleatórios, roda os 4 algoritmos e imprime a tabela de resultados
desafio.py          -> Desafio adicional: roda os 4 algoritmos em vetor aleatório, ordenado e invertido, pros 3 tamanhos
```

Pra rodar:
```
python3 main.py
python3 desafio.py
```

## Etapa 1 e 2 - como os dados foram gerados e o que conta como operação

Pra cada tamanho de vetor eu gero um vetor aleatório uma única vez e faço uma cópia pra cada algoritmo (`.copy()`), assim todos recebem exatamente os mesmos números pra ordenar.

O que eu contei como comparação e como troca/movimentação em cada algoritmo:

- **Bubble Sort**: comparação = toda vez que compara `vetor[j] > vetor[j+1]`; troca = toda vez que troca dois elementos vizinhos de lugar.
- **Insertion Sort**: comparação = toda vez que compara `vetor[j] > chave` pra decidir se empurra o elemento pra direita; movimentação = cada vez que um elemento é deslocado uma posição (não contei a última linha que coloca a chave no lugar final, porque ali não tem comparação nem deslocamento, só a inserção).
- **Selection Sort**: comparação = toda vez que compara `vetor[j] < vetor[menor]` procurando o menor elemento restante; troca = a troca no fim de cada volta do laço externo (no máximo uma por volta).
- **Quick Sort**: usei o último elemento do sub-vetor como pivô (particionamento de Lomuto, do jeito que vimos em aula). Comparação = toda vez que compara um elemento com o pivô; troca = toda troca feita dentro da função `particiona`, incluindo a troca final que coloca o pivô no lugar certo.

Não implementei nenhuma otimização de parada antecipada em nenhum dos algoritmos - são as versões "normais" mesmo, pra poder comparar de forma mais direta com o que foi visto em aula.

## Etapa 3 - Resultados

| Tamanho | Bubble Comp. | Bubble Troc. | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Troc. | Quick Comp. | Quick Mov. |
|---|---|---|---|---|---|---|---|---|
| 10 | 45 | 23 | 30 | 23 | 45 | 7 | 21 | 17 |
| 20 | 190 | 110 | 125 | 110 | 190 | 16 | 60 | 52 |
| 1.000 | 499.500 | 247.537 | 248.530 | 247.537 | 499.500 | 995 | 10.440 | 5.870 |

## Etapa 4 - Análise

**a) Qual algoritmo fez menos comparações com 10 elementos?**
O Quick Sort, com 21. Depois vem o Insertion com 30, e Bubble/Selection empatados em 45.

**b) Qual fez menos trocas?**
Selection Sort, só 7. Faz sentido porque ele só troca uma vez por volta do laço de fora, no máximo.

**c) O padrão de 10 elementos se repetiu com 20?**
Sim, meio que igual: Quick continuou tendo menos comparações (60) e Selection continuou tendo menos trocas (16). E uma coisa que eu não esperava: Bubble e Selection deram exatamente o mesmo número de comparações tanto em 10 (45=45) quanto em 20 (190=190).

**d) O que aconteceu quando o vetor foi pra 1.000 elementos?**
Bubble, Insertion e Selection deram um salto enorme, foram pra casa das centenas de milhares (499.500, 248.530 e 499.500 respectivamente). O Quick Sort ficou bem menor, só 10.440. A diferença fica gigante nesse tamanho.

**e) Bubble, Insertion e Selection são todos O(n²). Deram o mesmo número de operações?**
Não exatamente. Reparando direito nos números: Bubble e Selection tiveram o número de comparações **idêntico** nos três tamanhos (45/45, 190/190, 499.500/499.500). Acho que isso acontece porque nenhum dos dois tem algum jeito de parar mais cedo - os dois sempre rodam o laço inteiro do mesmo jeito, então sempre fazem n(n-1)/2 comparações, não importa se o vetor já tá quase ordenado ou não. Já o Insertion deu um número bem menor de comparações (30, 125, 248.530) porque ele para de comparar assim que encontra a posição certa pro elemento - ele "sente" a ordem dos dados, os outros dois não. E nas trocas, aí sim os três são bem diferentes: Bubble troca muito mais (247.537 em n=1000) do que Selection (só 995), porque Bubble troca toda vez que dois vizinhos estão fora de ordem, e Selection só troca uma vez por volta do laço.

**f) Qual teve o maior crescimento?**
Bubble e Selection cresceram igual (já que dão sempre o mesmo número), e foi o maior crescimento dos quatro: de 20 pra 1.000 elementos (50x mais dados) as comparações deles multiplicaram por quase 2.630x. O Insertion cresceu um pouco menos (quase 1.990x) porque ele não faz sempre o máximo de comparações. O Quick Sort cresceu bem menos que todos, só 174x, o que mostra que ele não é O(n²) que nem os outros.

**g) Como o Quick Sort se diferenciou?**
No experimento principal (vetor aleatório) ele foi de longe o melhor, crescendo bem mais devagar que os outros conforme o vetor cresce. Mas no desafio abaixo dá pra ver que ele também tem um lado ruim que os outros não têm do mesmo jeito: quando o vetor já está ordenado, ele vira o pior de todos.

**h) Os resultados batem com a teoria?**
No geral sim. Bubble e Selection bateram certinho com a fórmula teórica de O(n²) (n(n-1)/2 comparações, sem exceção). Insertion também é O(n²) mas na prática fica abaixo disso porque ele se adapta aos dados. Quick Sort no caso aleatório ficou bem próximo do O(n log n) que a teoria promete. A parte que eu acho que a teoria "esconde" um pouco, se só falar do caso médio, é o pior caso do Quick Sort - que apareceu bem forte no desafio adicional.

**i) Qual eu escolheria pra central de distribuição?**
Quick Sort, pelos números: com 1.000 pedidos ele fez 10.440 comparações contra quase 500 mil do Bubble/Selection, uma diferença enorme que só tende a crescer com mais pedidos ainda. Mas eu colocaria uma ressalva: como usei sempre o último elemento como pivô, o desafio abaixo mostrou que isso é um problema sério se os dados já chegarem mais ou menos ordenados (o que pode até acontecer numa central de pedidos, dependendo de como os códigos são gerados). Então na prática eu tentaria usar uma escolha de pivô melhor (aleatório, ou pegar a mediana de três valores), pra não correr o risco de cair no pior caso.

## Desafio adicional

Repeti o teste em três situações (aleatório, já ordenado, ordem inversa) pros três tamanhos do experimento principal, não só pra 1.000 - assim dá pra ver se o comportamento muda com a escala ou não.

### n = 10

| Vetor | Bubble Comp. | Bubble Troc. | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Troc. | Quick Comp. | Quick Mov. |
|---|---|---|---|---|---|---|---|---|
| Aleatório | 45 | 23 | 30 | 23 | 45 | 7 | 21 | 17 |
| Ordenado | 45 | 0 | 9 | 0 | 45 | 0 | 45 | 54 |
| Invertido | 45 | 45 | 45 | 45 | 45 | 5 | 45 | 29 |

### n = 20

| Vetor | Bubble Comp. | Bubble Troc. | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Troc. | Quick Comp. | Quick Mov. |
|---|---|---|---|---|---|---|---|---|
| Aleatório | 190 | 110 | 125 | 110 | 190 | 16 | 60 | 52 |
| Ordenado | 190 | 0 | 19 | 0 | 190 | 0 | 190 | 209 |
| Invertido | 190 | 190 | 190 | 190 | 190 | 10 | 190 | 109 |

### n = 1.000

| Vetor | Bubble Comp. | Bubble Troc. | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Troc. | Quick Comp. | Quick Mov. |
|---|---|---|---|---|---|---|---|---|
| Aleatório | 499.500 | 247.537 | 248.530 | 247.537 | 499.500 | 995 | 10.440 | 5.870 |
| Ordenado | 499.500 | 0 | 999 | 0 | 499.500 | 0 | 499.500 | 500.499 |
| Invertido | 499.500 | 499.497 | 499.500 | 499.497 | 499.500 | 503 | 497.850 | 249.668 |

**A ordem inicial dos dados afeta todos os algoritmos do mesmo jeito?**

Não, e o padrão se repete nos três tamanhos, então dá pra dizer que não é coincidência de um caso só:

- Bubble e Selection nem percebem a diferença nas comparações em nenhum dos três tamanhos - ficam sempre no mesmo número (45/45, 190/190, 499.500/499.500), seja o vetor aleatório, ordenado ou invertido. Faz sentido, porque nenhum dos dois tem algum mecanismo pra aproveitar que o vetor já está arrumado. Só as trocas mudam com a organização dos dados (por exemplo Bubble: 23 trocas no aleatório de n=10, 0 no ordenado, 45 no invertido).
- Insertion é o que mais aproveita quando o vetor já está ordenado, nos três tamanhos: 9 comparações em n=10 (contra 45 do aleatório), 19 em n=20 (contra 125), 999 em n=1.000 (contra 248.530). Mas se o vetor tá invertido ele vira O(n²) completo, igual aos outros dois (45, 190, 499.500 - os mesmos números de Bubble e Selection).
- Quick Sort é o único que se comporta diferente dependendo do tamanho, no seguinte sentido: no vetor aleatório ele sempre é o melhor de longe, mas no vetor **já ordenado** ele empata com o pior caso teórico dos outros (45, 190 e 499.500 comparações, exatamente o mesmo número de Bubble/Selection) e ainda faz mais movimentações que qualquer outro algoritmo naquele tamanho (54, 209 e 500.499). Isso já aparece em n=10 e só fica mais evidente em n=1.000. É o pior caso clássico de Quick Sort com pivô fixo no último elemento: um vetor já ordenado faz as partições ficarem sempre bem desbalanceadas (uma parte vazia, a outra com quase tudo), e aí ele degrada pra O(n²) igual aos algoritmos mais simples.

Então dá pra concluir que não dá pra confiar cegamente que "Quick Sort é sempre o mais rápido" - depende muito de como os dados chegam e de qual elemento é escolhido como pivô, e isso vale tanto pra vetor pequeno quanto grande.
