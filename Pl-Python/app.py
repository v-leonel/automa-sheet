import pandas as pd

data = {
    'Produtos': ['Tablet', 'Pós Graduação', 'Celular', 'Passagem Aérea', 'Computador', 'SPA', 'Corte Cabelo'],
    'Preço Base Original': [999.99, 4500, 899.99, 799, 3000, 480.48, 50],
    'Tipo': ['Produto', 'Serviço', 'Produto', 'Serviço', 'Produto', 'Serviço', 'Serviço'],
    'Multiplicador Imposto': [1.1, 1.5, 1.1, 1.3, 1.3, 1.3, 1.3],
}

tabela = pd.DataFrame(data)

produtos = 'Produtos.xlsx'
tabela.to_excel(produtos, index=False)

tabela_lido = pd.read_excel(produtos)

print(tabela_lido)

tabela = pd.read_excel("")