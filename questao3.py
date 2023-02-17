salario = float(input())

# Na prova, fiz cada calculo direto nos IFs. Aqui deixei separado para não repetir o código
faixaSal1 = salario * 0.075
faixaSal2 = salario * 0.09
faixaSal3 = salario * 0.12
faixaSal4 = salario * 0.14

# Adicionei <=, pois os valores pertencem a faixa salarial indicada

# Na prova, cometi um erro grave.
if salario <= 1302:
    print(salario - (faixaSal1))
elif salario <= 2571.29:
    print(salario - (faixaSal1 + faixaSal2))
elif salario <= 3856.94:
    print(salario - (faixaSal1 + faixaSal2 + faixaSal3))
else:
    print(salario - (faixaSal1 + faixaSal2 + faixaSal3 + faixaSal4))