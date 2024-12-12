from flask import Flask
from database import create_db_and_tables
from routes.produto import produto_bp
from routes.home import main_routes

app = Flask(__name__)

create_db_and_tables()

app.register_blueprint(produto_bp)
app.register_blueprint(main_routes)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)