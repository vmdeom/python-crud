from flask import Blueprint, render_template

# Definindo o Blueprint para as rotas principais
main_routes = Blueprint('main', __name__)

# Rota para a página inicial
@main_routes.route('/')
def index():
    return render_template('index.html')