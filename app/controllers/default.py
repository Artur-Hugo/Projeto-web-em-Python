from flask import render_template, request
from app import app, db
from app.models.tables import Pessoa

@app.route('/')
@app.route('/listagem')
def listagem():
    lista_pessoas = [
        {'id': 1, 'nome' : 'Fulano de tal', 'idade': 18, 'sexo': 'M', 'salario':2000},
        {'id': 2, 'nome': 'Beotrano da Silva', 'idade': 19, 'sexo': 'M', 'salario':2500},
        {'id': 3, 'nome': 'Fulana de tal', 'idade': 17, 'sexo':'F', 'salario': 2100}
    ]   #Pessoa.query.all()
    return render_template('listagem.html', pessoas=lista_pessoas, ordem='id')