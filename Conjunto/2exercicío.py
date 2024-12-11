"""
2)Duas lojas possuem estoques diferentes de produtos. Encontre os produtos disponíveis em ambas e os exclusivos de cada loja.

"""
loja1 = ['produtoA', 'produtoB', 'produtoC', 'produtoD']
loja2 = ['produtoC', 'produtoD', 'produtoE', 'produtoF']

# Produtos em ambas as lojas
produtos_comuns = set(loja1) & set(loja2)

# Produtos exclusivos de cada loja
exclusivos_loja1 = set(loja1) - set(loja2)
exclusivos_loja2 = set(loja2) - set(loja1)

print('Produtos em ambas as lojas:', list(produtos_comuns))
print('Produtos exclusivos da loja 1:', list(exclusivos_loja1))
print('Produtos exclusivos da loja 2:', list(exclusivos_loja2))
