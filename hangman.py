"""Main hangman game.

Use Python 3.
"""

from string import ascii_lowercase

from  getpass import getpass



def pegaMostraPalavra(word, idxs):
    """Pega a palavra que é mostrado ao Usuários como está prenchida """
    if len(word) != len(idxs): # somente precuação
        raise ValueError('Palavra e tamnnho do vetor de indices não batem')
    displayed_word = ''.join(
        [letter if word[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()


def pegaProxLetra(remaining_letters):
    """Pega a proxima a letra inserida pelo usuário e verificando se 
    não está repetida e se não tem mais letras possíveis para ser usada."""
    if len(remaining_letters) == 0:
        raise ValueError('Não tem mais possibilidade de chutes')
    while True:
        next_letter = input('Escolha a próxima letra: ').lower()
        if len(next_letter) != 1:
            print('{0} tem mais de uma letra'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} não é uma letra'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} já foi chutado '.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter



"""
    Inicialização das variáveis necessárias para jogar a forca  e 
    as regras do jogo
"""






print('Começando o Game: Forca')
qtdChutes = 3   
# Randomly select a word
print('Escreva a palavra a ser advinhada')
word = str(getpass('Escreva a palavara a ser testada \t')).lower()
print()

# Initialize game state variables
vetorResposta = [letter not in ascii_lowercase for letter in word]
remaining_letters = list(ascii_lowercase)
wrong_letters = []
word_solved = False


# Main game loop
while qtdChutes > 0 and not word_solved:
    # Print current game state
    print('Palavra: {0}'.format(pegaMostraPalavra(word, vetorResposta)))
    print('Tentavas que ainda tem-se: {0}'.format(qtdChutes))
    print('Palpites anteriores: {0}'.format(' '.join(wrong_letters)))

    # Get player's next letter guess
    next_letter = pegaProxLetra(remaining_letters)

    # Check if letter guess is in word
    if next_letter in word:
        # Guessed correctly
        print('{0} is in the word!'.format(next_letter))

        # Reveal matching letters
        for i in range(len(word)):
            if word[i] == next_letter:
                vetorResposta[i] = True
    else:
        # Guessed incorrectly
        print('{0} is NOT in the word!'.format(next_letter))

        # Decrement num of attempts left and append guess to wrong guesses
        qtdChutes -= 1
        wrong_letters.append(next_letter)

    # Check if word is completely solved
    if False not in vetorResposta:
        word_solved = True
    print()

# The game is over: reveal the word
print('The word is {0}'.format(word))

# Notify player of victory or defeat
if word_solved:
    print('Congratulations! You won!')
else:
    print('Try again next time!')

# Ask player if he/she wants to try again
tentarDeNovo = input('Would you like to try again? [y/Y] ')

    
print()
