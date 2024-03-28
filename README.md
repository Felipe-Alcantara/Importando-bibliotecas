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

# Manipulando Excel com xlwings

Este é um código Python que faz o seguinte:

1. Importa a biblioteca `xlwings`, que é usada para automação e manipulação de dados do Excel.

2. Cria um novo arquivo Excel chamado 'relatorio_excel.xlsx'.

3. Verifica se uma planilha chamada 'Planilha1' existe no arquivo. Se não existir, ele cria uma nova planilha com esse nome. Se já existir, ele simplesmente seleciona essa planilha.

4. Seleciona a célula 'A1' na planilha 'Planilha1'.

5. Obtém a cor de fundo da célula 'A1' usando a propriedade `Interior.Color` do objeto `api` da célula.

6. Converte a cor, que é retornada como um número único, para o formato RGB. O formato RGB é uma representação de cores usando três números, cada um representando a intensidade de vermelho, verde e azul, respectivamente.

7. Imprime a cor da célula 'A1' no formato RGB.

Este código é útil para aprender como manipular arquivos Excel em Python usando a biblioteca `xlwings`. Ele mostra como criar e salvar arquivos Excel, como adicionar e selecionar planilhas, como selecionar células e como obter e converter a cor de fundo de uma célula.

# Criando uma Interface Gráfica com Tkinter

Este é um código Python que faz o seguinte:

1. Importa a biblioteca `Tkinter`, que é usada para criar interfaces gráficas.

2. Cria uma nova janela usando `Tk()`. A janela é configurada com o título "Janelinha" e um tamanho de 500x500 pixels.

3. Cria um `Frame` interno com fundo cinza. O `Frame` é posicionado no centro da janela.

4. Define uma variável `equation_text` com o valor "Linha de texto".

5. Cria um rótulo (`Label`) que contém o texto da variável `equation_text`. O rótulo tem uma fonte Helvetica de tamanho 30, texto preto e fundo cinza. O rótulo é adicionado ao `Frame` interno.

6. Inicia o loop principal da janela com `window.mainloop()`. Isso faz com que a janela seja exibida na tela e comece a responder aos eventos do usuário.

Este código é útil para aprender como criar interfaces gráficas em Python usando a biblioteca `Tkinter`. Ele mostra como criar e configurar janelas, como adicionar e posicionar frames, como criar rótulos com texto personalizado e como iniciar o loop principal da janela. Além disso, ele demonstra como usar cores de fundo para destacar elementos da interface gráfica.