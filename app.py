import requests
from flask import Flask, request, Response
from Produto import Produto, engine
from sqlmodel import Session, select

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.post('/produto')
def post_produto():
    produto = Produto(**request.json)
    try:
        with Session(engine) as session:
            session.add(produto)
            session.commit()
            session.refresh(produto)
        return f'produto {produto.json()} criado'
    except:
        return 'Produto já cadastrado', 400

@app.get('/produto/<codigo>')
def get_produto(codigo):
    with Session(engine) as session:
        produto = select(Produto).where(Produto.codigo == codigo)
        resultado = session.exec(produto).first()
        if resultado:
            return resultado.json
        return 'não existe', 404

@app.patch('/produto/')
def patch_produto():
    pass

@app.delete('/produto')
def delete_produto():
    pass

if __name__ == '__main__':
    app.run()