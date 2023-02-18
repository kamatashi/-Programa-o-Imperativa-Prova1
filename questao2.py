
'''
O processo para obter o resultado dos triglicerídeos e colesterol é parecido. 
Para evitar repetir IFs, criei dois parametros, metrica1 e metrica2, para receber os valores para classíficação da faixa.
'''
def avaliar(input, metrica1, metrica2):
    if input < metrica1:
        message = 'DESEJAVEL'
    # Adicionado um <= considerando a inclusão do valor da segunda métrica de acordo com o que foi pedido na questão
    elif input <= metrica2:
        message = 'LIMITROFE'
    else:
        message = 'ALTO'

    return message


# Testa se é negativo, se não, aplica a função avaliar nas duas variáveis. Isso especializa cada função em uma tarefa.
def ehNegativo(valor1, valor2):

    # NA prova foi usado and, mas isso é um erro. Basta uma das condições ser verdade.
    if trigli < 0 or coles < 0:
        print('Algum valor fora da faixa')
    else:
        # Na prova, as variáveis estavam dentro dos {} diretamente, mas isso está errado. Para ficar mais limpo usei o format.
        print('Triglicerideos {} mg/dl: {}'.format(valor1, avaliar(valor1, 150, 200)))

        # Não prova não incluí a formatação do float usando o :.f, isso é um erro, pois a questão pede apenas uma casa decímal depois da vírgula
        print('Colesterol total {:.1f} mg/dl ({})'.format(valor2, avaliar(valor2, 150, 170)))



'''
O input foi deixado para o final do código para ficar organizado.
O código primeiro carrega as funções, independente das variáveis com o valor inputado, pois estão fora do escopo.
Depois que as funções foram definidas, é aplicada a função ehNegativo.
'''
trigli = int(input())
coles = float(input())

ehNegativo(trigli, coles)
