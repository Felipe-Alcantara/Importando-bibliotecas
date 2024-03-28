# Importando-bibliotecas
 Alguns projetos que eu fiz quando estava aprendendo a usar bibliotecas em python

# Aprendendo a usar uma biblioteca com random

Este código faz o seguinte:

1. `from random import randint as rd`: Este comando importa a função `randint` do módulo `random` do Python. A função `randint` retorna um número inteiro aleatório dentro do intervalo especificado (inclusive). O `as rd` é um alias para `randint`, o que significa que você pode usar `rd` em vez de `randint` no restante do seu código.

2. `aleatorio = rd(1, 100)`: Aqui, a função `rd` (que é um alias para `randint`) é chamada com os argumentos `1` e `100`. Isso retorna um número inteiro aleatório entre `1` e `100` (inclusive) e atribui esse número à variável `aleatorio`.

3. `print(aleatorio)`: Finalmente, este comando imprime o valor da variável `aleatorio`. Como `aleatorio` é definido como um número aleatório entre `1` e `100`, cada vez que você executa o programa, ele imprimirá um número diferente nesse intervalo.

# Datetime saudações

Este é um código Python que faz o seguinte:

1. Importa o módulo `datetime` que fornece classes para manipular datas e horas.

2. Obtém a data e hora atuais usando `datetime.datetime.now()` e armazena o resultado na variável `agora`.

3. Extrai a hora atual do objeto `agora` e armazena na variável `hora`.

4. Verifica se a hora está entre 0 e 23. Se não estiver, imprime "Horario invalido!".

5. Se a hora estiver dentro do intervalo válido, verifica a hora atual e imprime uma saudação apropriada:
    - Se a hora for maior ou igual a 12 e menor que 18, imprime "Boa tarde amigo!".
    - Se a hora for menor que 12, imprime "Bom dia amigo!".
    - Se a hora for maior ou igual a 18, imprime "Boa noite amigo!".

6. Em seguida, o código imprime a data e hora atuais, a hora atual, os minutos atuais e os segundos atuais.

Este código é basicamente um programa de saudação que cumprimenta o usuário com base na hora atual do dia e também exibe a data e hora atuais, a hora, os minutos e os segundos atuais.