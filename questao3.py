# A minha lógica estava errada, não me atentei para a formula apresentada. Está é a solução para o problema:

salario = float(input())


# Adicionei <=, pois os valores pertencem a faixa salarial indicada.
# É feito o cálculo das faixas salariais e descontados do salário
# Incluído a formatação correta do número
if salario <= 1302:
    print('%.2f'%(salario - ((salario * 0.075))))
elif salario <= 2571.29:
    print('%.2f'%(salario - ((1302 * 0.075) + ((salario - 1302) * 0.09))))
elif salario <= 3856.94:
    print('%.2f'%(salario - ((1302 * 0.075) + ((2571.29 - 1302) * 0.09) + ((salario - 2571.29) * 0.12))))
else:
    print('%.2f'%(salario - ((1302 * 0.075) + ((2571.29 - 1302) * 0.09) + ((3856.94 - 2571.29) * 0.12) + (salario  - 3856.94)* 0.14)))
