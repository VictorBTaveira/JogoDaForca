"""Main hangman game.

Use Python 3.
"""

#from string import ascii_lowercase
from getpass import getpass
from subprocess import call
import os 
from time import sleep

def clear():
    # faz a chamade do os para derterminar qual comando de limpar o terminal
    _ = call('clear' if os.name =='posix' else 'cls')




def mostra_palavra(word, idxs):

    """ Pega a palvra resposta e coloca pelo user e esconde as letras da string word
    e conforme o vetor idxs tem true em cada posição, as letras se revelam
    """
    if len(word) != len(idxs):
        raise ValueError('Tamanho da palavra e dos indices não são iguais')
    displayed_word = ''.join(
        [letter if idxs[i] else '#' for i, letter in enumerate(word)])
    return displayed_word.strip()


def pegaProxLetra(remaining_letters,ascii_lowercase):

    """ Pega a próxima letra inputado pelo usuário e o jogo acaba se """

    if len(remaining_letters) == 0:
        raise ValueError('Não tem mais letra no alfabeto latino para usar')
        
    while True:
        next_letter = input('Escolha a próxima letra: ').lower()
        if len(next_letter) != 1:
            print('\n\t{0} não é caractere único'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('\t{0} não é uma letra'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('\n\t{0} já foi usado'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter

def drawGuy(qtdErro):
    print('\n')
                            
    if qtdErro == 3:
            print( '+-------+')
            print('|       ')
            print('|       ')
            print('|       ')
            print('|________\n\r')
            
    
    if qtdErro == 2:
            print('+-------+')
            print('|       O')
            print('|       ')
            print('|       ')
            print('|________\n\r')
            

    if qtdErro == 1:
            print('+-------+')
            print('|       O')
            print('|      /|\\')
            print('|       ')
            print('|________\n\r')
               

    if qtdErro == 0:
            print('+-------+')
            print('|       O')
            print('|      /|\\')
            print('|       |')
            print('|      / \\')
            print('|________\n\r')
              

def jogarForca():
    
    # Interage com o jogador
    print('O jogador terá 3 chances de errar')
    print('Digite somente letras do alfabeto romano')


    print('Começa o Jogo, Amigo ')
  

    # coloque a palavra que vai ser trabalhada 
    palavra = str(getpass('Escreva a palavara a ser testada, jogador 1 ')).lower()
    while palavra.isalpha() != True  :
        palavra = str(getpass('Escreva uma palavra de verdade a ser testada  ')).lower()


    
    # Inicialização das variáveis necessárias para começar o jogo
    ascii_lowercase =  [chr(x) for x in range(ord('a'), ord('z') + 1)] 
    idxs = [letra not in ascii_lowercase for letra in palavra] 
    letrasSobrando = list(ascii_lowercase)
    letraErrada= []
    letrasCertas=[]
    resolvido = False
    tentativas = 3
    
    clear()
    
    # o loop principal do jogo, é aqui que imagem acontece
    while tentativas >  0 and not resolvido:
        # limpa a tela e Printa o atual estado do jogo: placar, as tentativas e chances 
        sleep(1.0)
        clear()
        print('Palavra: {0}'.format(mostra_palavra(palavra, idxs)))
        print('Tentativas remanescentes: {0}'.format(tentativas))
        print('Palpites certos: {0}'.format(' '.join(letrasCertas)))
        print('Outros Palpites: {0}\n'.format(' '.join(letraErrada)))
        drawGuy(tentativas)

        # Pega a próxima letra 
        next_letter = pegaProxLetra(letrasSobrando,ascii_lowercase)

        # Checa se a letra digitada está na palavra a ser descoberta
        if next_letter in palavra:
            # Guessed correctly
            print('{0} está na palavra!'.format(next_letter))

            # Revela as letras, muda os valores do vetor idxs 
            for i in range(len(palavra)):
                if palavra[i] == next_letter:
                    idxs[i] = True
                    letrasCertas.append(next_letter)

        else:
            # quando o chute da letra foi errado 
            print('\n\t{0} não está na palavra!'.format(next_letter))

            # Decrement num of attempts left and append guess to wrong guesses
            tentativas -= 1
            letraErrada.append(next_letter)


        # Check if word is completely solved
        if False not in idxs:
            resolvido = True
        

    # revela a palavra 
    clear()
    print(' A palavra é {0}'.format(palavra.capitalize()))

    # Avisa o jogador de sua vitória ou derrota
    if resolvido:
        print('Congratulations! Wunderbach, vc venceu! \n')
        print('  __  ')
        print(' /  \\')
        print('<    >')
        print(' |  | ')
        print(' \\  /') 
        print('  | | ')
        print('------')

    else:
        print('Tente outra vez!')
        drawGuy(0)

    # Pergunta se quer jogar de novo
    try_again = input('Gostaria de jogar de novo? [y/Y] ')
    return try_again.lower() == 'y'


if __name__ == '__main__':
    while jogarForca():
        clear()
        print('RRRRRRecomeça o jogo')
        
        
