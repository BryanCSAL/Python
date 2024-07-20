import os

word = 'Margarida'
numCharacter = len(word)
character = ...
secretWord = numCharacter*'*'
attemptWord = secretWord
word_list = list(word)
word_attlist = list(attemptWord)
tentativas = 1

print(f'Descubra a palavra de {len(word)} letras, {secretWord}')
character = input(f'Tente uma letra:')

# Loop que se mantém enquanto há "*" na palavra.
while '*' in attemptWord:
    os.system("cls")
    # O uso do .lower() serve para tonar tudo minúsculo e evitar o case sensitivy.
    if character.lower() in word.lower():    
        # Itera sobre os índices da palavra
        for i in range(len(word_list)):
            # Verifica se o caractere atual é o que queremos substituir
            if word_list[i].lower() == character.lower():
                word_attlist[i] = character

        # Junta a lista de volta em uma string
        attemptWord = ''.join(word_attlist)

        print(f"Você encontrou o {character}, a palavra ficou: {attemptWord}")

    else:
        print(f"A letra {character} não está na palavra, a palavra contiua: {attemptWord}")

    # Força a saída do laço quando a palavra é descoberta
    if (attemptWord == word.lower()):
        break

    character = input(f'Tente uma letra:')

    # Contabilisa mais uma tentativa
    tentativas += 1

    
os.system("cls")
print(f"Você descobriu a palavra {attemptWord}, levou {tentativas} tentativas!")
