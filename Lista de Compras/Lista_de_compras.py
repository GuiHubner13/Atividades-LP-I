lista_compras = [
    ["Arroz 1kg", 5.50, 2],
    ["Feijão 1kg", 8.00, 2],
    ["Patinho 500g", 21.50, 1]
]

print(f"{'Item':<12} {'Preço':>8} {'Qtd':>5} {'Total':>10}")
print("-" * 37)

total = 0
subtotal = 0
for item, preco, quantidade in lista_compras:
    subtotal = preco*quantidade
    total += subtotal
    print(f"{item:<12} R$ {preco:>6.2f} {quantidade:>5} R${subtotal:>8.2f}")

print("-" * 37)
print(f"{'TOTAL GERAL':<12} {'':>8} {'':>5} R$ {total:>8.2f}")
