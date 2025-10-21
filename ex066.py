total = totmil = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('preço do produto: '))
    cont += 1
    total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total da compra deu {total} ')
print(f'temos {totmil} produtos de mais de R$1000 ')
print(f'o produto mais barato custa R$ {menor:.2f}')
print('fim do programa')
