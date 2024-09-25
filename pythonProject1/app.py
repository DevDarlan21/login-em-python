from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# Lista global para armazenar os jogos
lista = []

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form.get('nome')
    categoria = request.form.get('categoria')
    console = request.form.get('console')

    if nome and categoria and console:
        jogo = Jogo(nome, categoria, console)
        lista.append(jogo)
        return redirect(url_for('index'))  # Redireciona para a lista de jogos
    else:
        return render_template('novo.html', titulo='Novo Jogo', error="Todos os campos são obrigatórios.")
@app.route('/login')
def login():
    return render_template('login.html', titulo='Login')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'admin' == request.form['usuario'] and 'admin' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ': Login realizado com sucesso!')
        return redirect(url_for('index'))
    else:
        flash('Não logado, tente novamente.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] =  None
    flash('logout realizado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)
