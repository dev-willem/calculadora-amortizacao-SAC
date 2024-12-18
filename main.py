from flask import Flask, render_template, request

app = Flask(__name__)

def calculaAmortizacao(saldo_devedor, numero_de_meses):
    return round(saldo_devedor / numero_de_meses, 2)

def calculaJurosTotais(saldo_devedor, numero_de_meses, taxa_juros):
    total_juros = 0
    amortizacao = saldo_devedor / numero_de_meses
    for mes in range(1, numero_de_meses + 1):
        juros_mes = saldo_devedor * (taxa_juros / 100) / 12
        total_juros += juros_mes
        saldo_devedor -= amortizacao
    return round(total_juros, 2)

def calculaPrestacoes(saldo_devedor, numero_de_meses, taxa_juros):
    prestacoes = []
    amortizacao = saldo_devedor / numero_de_meses
    for mes in range(1, numero_de_meses + 1):
        juros_mes = saldo_devedor * (taxa_juros / 100) / 12
        prestacao = amortizacao + juros_mes
        prestacoes.append(round(prestacao, 2))
        saldo_devedor -= amortizacao
    return prestacoes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        saldo_devedor = float(request.form['saldo_devedor'])
        numero_de_meses = int(request.form['numero_de_meses'])
        taxa_juros = float(request.form['taxa_juros'])

        amortizacao = calculaAmortizacao(saldo_devedor, numero_de_meses)
        juros_totais = calculaJurosTotais(saldo_devedor, numero_de_meses, taxa_juros)
        prestacoes = calculaPrestacoes(saldo_devedor, numero_de_meses, taxa_juros)
        montante = saldo_devedor + juros_totais

        return render_template('amortizacao.html',
                               capital_inicial=round(saldo_devedor, 2),
                               amortizacao=amortizacao,
                               juros_totais=juros_totais,
                               prestacoes=prestacoes,
                               montante=round(montante, 2),
                               saldo_devedor=request.form['saldo_devedor'],
                               numero_de_meses=request.form['numero_de_meses'],
                               taxa_juros=request.form['taxa_juros'])

    return render_template('amortizacao.html')


if __name__ == "__main__":
    app.run(debug=True)
