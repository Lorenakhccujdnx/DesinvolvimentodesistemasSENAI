NOME_USUARIO = 'Lorena'
SENHA_USUARIO = '1234'

nome = input('Digite o seu nome:')
senha = input('Digite a sua senha:')

# AND, TRUE TRUE
# OR, BASTA UM TRUE
# NOT, EXCLUSÃO
if NOME_USUARIO == nome or SENHA_USUARIO == senha :
    print ('Você entrou na plataforma!')
else: 
    print ('Sua senha ou usuario está incorreta')