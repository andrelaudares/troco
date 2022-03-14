valor = int(input('valor do produto'))
pago = int(input('valor pago'))
menos = valor - pago
menos1 = -(menos)
print('valor do troco', menos1)
if valor == pago:
        print("SEM TROCO")
elif valor < pago:
    vinte = int(menos1 / 20)
    vinte_r = menos1 %20

    dez = int(vinte_r / 10)
    dez_r = vinte_r % 10

    cinco = int(dez_r / 5)
    cinco_r = dez_r % 5

    um = int(cinco_r / 1)
    um_r = cinco_r % 1
    print('')
    if vinte > 0 :
        print('sao,',vinte, 'notas de 20')
    if dez >0:
        print('sao,',dez, 'notas de 10')
    if cinco > 0:
        print('sao,',cinco, 'notas de 5')
    if um > 0 :
        print('sao,',um, 'notas de 1')

else:
        print('DINHEIRO NAO SUFICIENTE')
