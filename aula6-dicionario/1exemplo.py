# DICIONARIO
# CHAVE E VALOR

usuario = { 
    # chave - valor
    'nome': 'Lorena',
    'idade': 19,
    'email': 'lorena@gmail.com',
    'senha': 'lorovs2324',
    'cpf': 00000000,
    'vip' : True,
   
   
    'endereco': [
        {
        'rua': 'Rua dos Bobos',
        'numero': 123,
        'cidade': 'São Paulo' 
        }
    ]
}

print(usuario['nome'], ['idade'])
print(usuario, type (usuario))

# arquitetura de dic (dados) facilita o gerenciamento de dados
# e a busca por eles (Obs: Até mesmo a crud)
# CRUD - C: CREATE - CRIAR
# R: READ - LER 
# U: UPDATE - ATUALIZAR
# D: DELETE - DELETAR

pesquisa = input('Digite o que você quer achar:')
print(usuario[pesquisa])

# METODO PARA DICIONÁRIO
# len - QUANTAS CHAVES EXISTEM NO DICIONÁRIO
# keys - RETORNA AS CHAVES
# values - RETORNA OS VALORES
# items - RETORNA CHAVES E VALORES 
# setdefault - ADICIONA VALOR SE A CHAVE NÃO EXISTE
# get - BUSCA CHAVE
# pop - APAGA UMA CHAVE ESPECÍFICA
# popitem - APAGA A ÚLTIMA CHAVE 
# update - ATUALIZA UM DICIONÁRIO

print(len(usuario))
print(list (usuario.keys()))
print(list (usuario.values()))
print(list (usuario.items()))

usuario.setdefault("saldo", 0)
print(usuario)

print(usuario.get('idade'))

usuario.pop('idade')
print(usuario)

usuario.popitem()
print(usuario)