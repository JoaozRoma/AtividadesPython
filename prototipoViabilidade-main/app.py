from flask import Flask,request, url_for, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:12345@localhost/CrudPrototipo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Produto(db.Model):
    codigo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    quantidade = db.Column(db.String(100))
    fornecedor = db.Column(db.String(100))


    def __init__(self, nome, quantidade, fornecedor):

        self.nome = nome
        self.quantidade = quantidade
        self.fornecedor = fornecedor


@app.route('/')
def login():

    return render_template("login.html")


@app.route('/index')
def Index():

    return render_template("index.html")

@app.route('/gerenciadorEstoque')
def gerenciadorEstoque():
    todos_produtos = Produto.query.all()

    return render_template("gerenciadorEstoque.html", lista_produto = todos_produtos)

@app.route('/insert',methods = ['POST'])
def insert():

    if request.method == 'POST':

        nome = request.form['nome']
        quantidade = request.form['quantidade']
        fornecedor = request.form['fornecedor']

        meu_produto = Produto(nome, quantidade, fornecedor)
        db.session.add(meu_produto)
        db.session.commit()

        flash('Produto inserido com sucesso!')

        return redirect(url_for('gerenciadorEstoque'))


@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        meu_produto = Produto.query.get(request.form.get('codigo'))

        meu_produto.nome = request.form['nome']
        meu_produto.quantidade = request.form['quantidade']
        meu_produto.fornecedor = request.form['fornecedor']

        db.session.commit()
        flash("Produto atualizado com Sucesso")

        return redirect(url_for('gerenciadorEstoque'))


@app.route('/delete/<codigo>/', methods = ['GET', 'POST'])
def delete(codigo):
    meu_produto = Produto.query.get(codigo)
    db.session.delete(meu_produto)
    db.session.commit()

    flash("Produto deletado com sucesso")

    return redirect(url_for("gerenciadorEstoque"))

if __name__ == "__main__":
    app.run(debug = True)
