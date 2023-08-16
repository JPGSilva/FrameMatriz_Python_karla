<h1 align="center">Aplicação de MatrizFrame em Python</h1>


__Fiz algumas pequenas alteraões__

<p align="center"></p>

Importação de bibliotecas:
A biblioteca numpy é importada como np.

Definição da função print_matrix:
Essa função recebe um título e uma matriz como entrada.
Converte a matriz em uma string formatada usando np.array2string.
Imprime o título seguido da representação da matriz.

Definição da função generate_actual_frame:
Essa função recebe um frame anterior como entrada.
Cria um novo frame atual a partir do frame anterior.
Gera uma quantidade aleatória de mudanças em posições aleatórias do frame atual.
Retorna o frame atualizado.

Definição da função compare_matrix:
Essa função recebe duas matrizes como entrada.
Cria uma matriz binária onde cada elemento é 1 se as matrizes tiverem valores diferentes na mesma posição, senão é 0.
Retorna a matriz binária.

Definição da função find_max_value_submatrix:
Essa função recebe uma matriz binária como entrada.
Define o tamanho da submatriz para procurar.
Percorre a matriz usando loops para encontrar as coordenadas da submatriz de tamanho definido com a maior soma de elementos iguais a 1.

Definição da função mark_max_difference_region:
Essa função recebe uma matriz binária, as coordenadas da submatriz de maior diferença e o tamanho da submatriz.
Marca a região da matriz binária com a maior diferença com o valor 1.

Loop While:
Um loop while é usado para executar uma série de testes (10 no total).
A cada iteração do loop, são gerados frames de imagem aleatórios: um frame anterior e um frame atual com alterações aleatórias.
São impressos os frames anteriores e atuais, bem como a matriz de diferenças entre eles.
As coordenadas da submatriz de maior diferença são encontradas.
A matriz de resultados é inicializada como uma matriz de zeros do mesmo tamanho da matriz de diferenças.
A região da matriz de resultados correspondente à submatriz de maior diferença é marcada com o valor 1.
Os resultados são impressos na saída.
O código gera uma série de testes, onde matrizes de frame aleatórios são comparadas e a região com a maior diferença é marcada com 1 na matriz de resultados. Cada teste exibe os resultados na saída.

</p>


<h4 align="center"> 
     🚀 Em construção...  🚧
</h4>
