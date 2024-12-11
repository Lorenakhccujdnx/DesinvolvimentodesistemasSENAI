"""
2)Faça um algoritmo que avalie se o usuario e senha cadastrados e 
se não tiver, printe uma falha
senao printe que deu tudo certo
(considerar que usuario e senha sejam ''ADM')
"""
def verificar_login(usuario, senha):
    usuario_correto = 'ADM'
    senha_correta = 'ADM'

    if usuario == usuario_correto and senha == senha_correta:
        print('Login bem-sucedido!')
    else:
        print('Falha no login. Usuário ou senha incorretos.')

# Solicitando entrada do usuário
usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

# Verificando login
verificar_login(usuario, senha)
