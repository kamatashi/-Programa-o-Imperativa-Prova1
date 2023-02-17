trigli = int(input())
coles = float(input())

# Apaguei as variáveis triglicerideoMessage e colesterolMessage por não terem utilidade.

if trigli < 0 or coles < 0:
    print('Algum valor fora da faixa')

else:
    if trigli < 150:
        triglicerideoMessage = 'DESEJAVEL'

    # Colocado um <= no ELIF considerando que o valor 200 pertence a faixa.
    elif trigli <= 200:
        triglicerideoMessage = 'LIMITROFE'
    else:
        triglicerideoMessage = 'ALTO'


    if coles < 150:
        colesterolMessage = 'DESEJAVEL'
    elif coles < 170:
        colesterolMessage = 'LIMITROFE'
    else:
        colesterolMessage = 'ALTO'

    print('Triglicerideos {} mg/dl: {}'.format(trigli, triglicerideoMessage))

    # Não prova não incluí a formatação do float usando o :.f, isso é um erro, pois a questão pede apenas uma casa decímal depois da vírgula
    print('Colesterol total {:.1f} mg/dl ({})'.format(coles, colesterolMessage))