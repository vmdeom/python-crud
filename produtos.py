produto = {
    'tipo': '',
    'nome': '',
    'codigo': '',
    'preco': 0.0,
    'quantidade': 0
}

def get_produto():
    return produto

def set_produto(dados):
    produto['tipo'] = dados['tipo']
    produto['nome'] = dados['nome']
    produto['codigo'] = dados['codigo']
    produto['preco'] = dados['preco']
    produto['quantidade'] = dados['quantidade']