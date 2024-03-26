# Importando-bibliotecas
 Projeto que eu fiz quando estava aprendendo a usar bibliotecas em python

Este código faz o seguinte:

1. `from random import randint as rd`: Este comando importa a função `randint` do módulo `random` do Python. A função `randint` retorna um número inteiro aleatório dentro do intervalo especificado (inclusive). O `as rd` é um alias para `randint`, o que significa que você pode usar `rd` em vez de `randint` no restante do seu código.

2. `aleatorio = rd(1, 100)`: Aqui, a função `rd` (que é um alias para `randint`) é chamada com os argumentos `1` e `100`. Isso retorna um número inteiro aleatório entre `1` e `100` (inclusive) e atribui esse número à variável `aleatorio`.

3. `print(aleatorio)`: Finalmente, este comando imprime o valor da variável `aleatorio`. Como `aleatorio` é definido como um número aleatório entre `1` e `100`, cada vez que você executa o programa, ele imprimirá um número diferente nesse intervalo.