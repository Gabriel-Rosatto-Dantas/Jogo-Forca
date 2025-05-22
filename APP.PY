import random

def carregar_palavras():
    with open('palavras.txt', 'r', encoding='utf-8') as file:
        palavras = [linha.strip().upper() for linha in file]
    return palavras

def escolher_palavra(palavras):
    return random.choice(palavras)

def inicializar_jogo(palavra):
    letras_descobertas = ['_' for _ in palavra]
    letras_erradas = []
    tentativas = 6
    return letras_descobertas, letras_erradas, tentativas

def mostrar_status(letras_descobertas, letras_erradas, tentativas):
    print("\nPalavra: " + " ".join(letras_descobertas))
    print("Letras erradas: " + ", ".join(letras_erradas))
    print(f"Tentativas restantes: {tentativas}")

def desenhar_forca(erros):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    print(estagios[erros])

def jogar():
    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)
    letras_descobertas, letras_erradas, tentativas = inicializar_jogo(palavra_secreta)
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while True:
        mostrar_status(letras_descobertas, letras_erradas, tentativas)
        desenhar_forca(len(letras_erradas))
        
        if "_" not in letras_descobertas:
            print("\nParabéns! Você venceu!")
            break
            
        if tentativas == 0:
            print("\nGame Over! Você perdeu.")
            print(f"A palavra era: {palavra_secreta}")
            break
            
        palpite = input("Digite uma letra: ").upper()
        
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
            
        if palpite in letras_descobertas or palpite in letras_erradas:
            print("Você já tentou esta letra. Tente outra.")
            continue
            
        if palpite in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_descobertas[i] = palpite
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

if __name__ == "__main__":
    jogar()
