from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            # Pega os dados do formulário
            preco_filamento = float(request.form['preco_filamento']) # Ex: 120.00
            peso_rolo = float(request.form['peso_rolo'])           # Ex: 1000 (1kg)
            gramas_usadas = float(request.form['gramas_usadas'])   # Ex: 50
            
            # Lógica do cálculo: (Preço / Peso Total) * Gramas Usadas
            custo_por_grama = preco_filamento / peso_rolo
            resultado = custo_por_grama * gramas_usadas
            
            # Formata para duas casas decimais
            resultado = f"{resultado:.2f}"
        except ValueError:
            resultado = "Erro: Digite apenas números."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)