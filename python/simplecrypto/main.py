import string

class OpcaoInvalidaError(Exception):
    """Exceção lançada quando o usuário digita algo diferente de 1 ou 2."""
    pass

LETTERS = string.ascii_lowercase
QTD_LETTERS = 26

def display_intro():

    """Exibe a introdução do programa"""

    print("""A criptografia de Caesar se refere ao método romano de ocultar mensagem.
    Havia dois circulos com as letras do alfabeto. Girava-se o aro externo para buscar
    a equivalência das letras. Por exemplo:
    A é o numero 1 por ser a primeira letra. Se letra equivalente fosse 3 casas adiante,
    a cada letra a, seriam escrito uma letra d e assim por diante. Vamos testar?""")
    word = input("Digite ou cole uma palavra").lower()
    while True:
        try:
            move = input("Digite  1 para criptografar ou 2 para descriptografar:")

            if move not in ['1', '2']:
                raise OpcaoInvalidaError("Você deve digitar apenas 1 ou 2!")
            shift = int(input("Digite o degrau de criptografia"))

            return word, shift, move

        except OpcaoInvalidaError as erro:
        # Capturamos a nossa exceção específica e mostramos a mensagem
            print(erro)
        except ValueError:
            print("Comando inválido. Tente de novo")

        except ValueError:
            print("Numero inválido. Tente de novo")




def encrypt(word: str,shift: int, move:int) -> str:
    """
        Criptografa um texto usando a Cifra de César.

        Args:
            word (str): A palavra a ser criptografada.
            shift (int): O número de casas para deslocar no alfabeto.

        Returns:
            str: O texto resultante da criptografia.
        """
    if move == '2':
        shift = shift * -1

    new_word = []

    for char in word:
        if char in LETTERS:
            actual_index = LETTERS.index(char)
            new_index = (actual_index + shift)%QTD_LETTERS
            new_word.append(LETTERS[new_index])
        else:
            new_word.append(char)
    return "".join(new_word)


def main():
    word, your_index, move = display_intro()
    result = encrypt(word, your_index, move)
    print( f"Aqui {word} se tornou {result}")

if __name__ == "__main__":
    main()
