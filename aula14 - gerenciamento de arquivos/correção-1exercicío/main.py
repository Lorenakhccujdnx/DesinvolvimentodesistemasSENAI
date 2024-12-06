from login import loginUsuario as l_suario
# para fazer login l_usuario
from cadastro import cadastrarUsuario as c_usuario 
# para  fazer cadastro c_usuario

while True:
    try:
        print(f"1- cadastrar \n 2- login \n")
        opcao = (int("O que deseja fazer?"))

# em *case* se usa match para mostar opções.
        match opcao:
            case "1":
            # nesse caso o 1 pode ou não ter parênteses. ex: ("1") ou "1".
               c_usuario()
            case "2":
               l_usuario()
            case _:
                print("Opção inválida!")
    except ValueError:
        print("Digite um valor válido!")
    except Exception:
       print ("Aconteceu um erro!Tente novamente!") 
       break
