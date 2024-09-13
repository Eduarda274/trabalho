# Lista de produtos vendidos
# Cada produto é representado por um dicionário com 'quantidade' e 'preço_unitário'
produtos = [
    {'quantidade': 10, 'preço_unitário': 5.0},
    {'quantidade': 7, 'preço_unitário': 8.0},
    {'quantidade': 3, 'preço_unitário': 12.0},
    # Adicione mais produtos conforme necessário
]

# Inicialize variáveis para calcular os totais
total_quantidade = 0
total_valor_vendas = 0.0

# Calcular o total de produtos vendidos e o valor total de vendas
for produto in produtos:
    total_quantidade += produto['quantidade']
    total_valor_vendas += produto['quantidade'] * produto['preço_unitário']

# Calcular a média da quantidade de produtos vendidos
num_produtos = len(produtos)
média_quantidade = total_quantidade / num_produtos if num_produtos > 0 else 0

# Exibir resultados
print(f"Total de produtos vendidos: {total_quantidade}")
print(f"Média da quantidade de produtos vendidos: {média_quantidade:.2f}")
print(f"Valor total de vendas: R${total_valor_vendas:.2f}")
