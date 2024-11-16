from flask import Flask
from database import create_db_and_tables
from routes.produto import produto_bp

app = Flask(__name__)

create_db_and_tables()

app.register_blueprint(produto_bp)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)