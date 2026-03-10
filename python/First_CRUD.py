import csv
from pathlib import Path

password_file_path = Path('picked_numbers.csv')
max_password = int(100)
max_range = max_password + 1
def checking_files():
    if not password_file_path.exists():
        with open(password_file_path, mode='w', newline='', encoding='utf-8') as p_file:
            w_pass = csv.writer(p_file)
            w_pass.writerow(['Passwords in use'])
    print('Tudo pronto para o uso')

def there_is_passwords():
    with open(password_file_path, mode='r', newline='') as pass_files:
            pass_reader = csv.reader(pass_files)
            next(pass_reader)
            used = {int(row[0]) for row in pass_reader if row}
            total = set(range(1, max_range ))
            avaliable_list = sorted(list(total - used))
    return  avaliable_list


def pick_password(is_avaliable):
    # Pega o primeiro da lista que a there_is_passwords retornou
    this_pass = is_avaliable.pop(0)
    with open(password_file_path, mode='a', newline='', encoding='utf-8') as open_file:
        w_new_pass = csv.writer(open_file)
        w_new_pass.writerow([this_pass])
    return this_pass


def return_password(returned):
    with open(password_file_path, mode='r', newline='', encoding='utf-8') as open_file:
        reader = csv.reader(open_file)
        header = next(reader)
        # Filtro com list comprehension
        rows = [row for row in reader if row and int(row[0]) != returned]

    with open(password_file_path, mode='w', newline='', encoding='utf-8') as p_file:
        w_pass = csv.writer(p_file)
        w_pass.writerow(header)
        w_pass.writerows(rows)


def main():
    checking_files()
    is_avaliable = there_is_passwords()

    while True:

        if not is_avaliable:
            print("\n⚠️ Não há mais senhas disponíveis!")
        else:
            comand = input("Digite P para pegar uma senha, D para devolver ou S para sair: ").upper()

            if comand == 'P':
                    that_password = pick_password(is_avaliable)
                    print(f"Sua senha é: {that_password}")

            elif comand == 'D':
                try:
                        #testando para ver se a lógica funciona
                        given_password = int(input("Digite qual password gostaria de retornar?: "))
                        return_password(given_password)
                        print(f"Senha {given_password} devolvida com sucesso!")
                except ValueError:
                        print("Erro: Digite apenas números.")

            elif comand == 'S':
                    break


if __name__ == "__main__":
    main()
