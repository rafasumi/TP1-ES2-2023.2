# Trabalho Prático 1

## Grupo
- Rafael Fontes Sumitani (2020006957)
- Isis Ferreira Carvalho (2020006663)
 
## Sistema
O sistema consiste na implementação de um jogo de adivinhação de palavras similar
ao famoso [Wordle](https://www.nytimes.com/games/wordle/index.html) (ou
[Termo](https://term.ooo/), a versão em português), porém inteiramente na linha
de comando. Dentro do jogo, o jogador deve adivinhar palavras de 5, 6 ou 7
letras. Ele deve dar palpites e o sistema aponta se cada uma das letras do
palpite faz parte da palavra e, se sim, indica também se ela está no lugar
certo.

Diferentemente do jogo original, a nossa implementação conta com diferentes
dificuldades e modos de jogo, como o modo de palavras temáticas.

O código do jogo foi modularizado em 4 arquivos:
- `constants.py`: Contém todas as constantes do jogo, como paths para arquivos
importantes, codificação ANSI para cores de caracteres do terminal, e opções de
jogo.
- `display.py`: Responsável por toda a parte visual do programa. Por exemplo,
inclui funções para apresentação do título e regras, além da implementação
visual e interativa do menu.
- `game.py`: Responsável por toda a lógica do jogo, desde o loop principal do
jogo até a definição de cores de cada letra que consiste um palpite.
- `main.py`: Controladora do fluxo do jogo. Responsável por chamar as funções
que implementam o jogo, na ordem adequada. Além disso, inicia o jogo de acordo
com as configurações escolhidas pelo usuário no menu.
 
## Tecnologias
O sistema foi implementado inteiramente em Python. Tentamos ao máximo utilizar
apenas módulos disponíveis na
[biblioteca padrão](https://docs.python.org/3/library/index.html) da linguagem,
para obter uma implementação "minimalista". Entretanto, foi necessário utilizar
algumas bibliotecas externas para algumas funcionaldades específicas. Essas
bibliotecas e as suas versões utilizadas estão disponíveis no arquivo
[requirements.txt](./requirements.txt). São elas:
- `pandas`: Biblioteca usada para leitura e manipulação de dados tabulares e,
mais especificamente, CSV.
- `playsound`: Biblioteca usada para tocar arquivos de som. No caso, trata-se
da trilha sonora do jogo.
- `pyenchant`: Biblioteca usada para realizar o *spell checking* dos palpites
feitos pelo usuário.
- `PyDictionary`: Biblioteca usada para obter diferentes significados de uma
determinada palavra.

## Instruções de execução
Primeiramente, é preciso instalar as dependências do sistema. Você pode fazer
isso com o seguinte comando:

```
pip install -r requirements.txt
```

Para começar a jogar, basta usar o comando `./pydle` no diretório raiz do
projeto.