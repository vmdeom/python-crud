from flask import Blueprint, request, jsonify
from models.Produto import Produto
from sqlmodel import Session, select
from database import engine

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produto', methods=['POST'])
def post_produto():
    produto_data = request.json
    produto = Produto(**produto_data)
    try:
        with Session(engine) as session:
            session.add(produto)
            session.commit()
            session.refresh(produto)
        
        return jsonify(produto.dict()), 201

    except:
        return jsonify({"error": str(e)}), 400  

@produto_bp.route('/produto/<codigo>', methods=['GET'])
def get_produto(codigo: str):
    with Session(engine) as session:
        query = select(Produto).where(Produto.codigo == codigo)
        produto = session.exec(produto).first()
        if produto:
            return jsonify(produto.dict()), 200
        
        return jsonify({"error": "prduto não encontrado"}), 404

@produto_bp.route('/produto/<codigo>', methods=['PATCH'])
def patch_produto(codigo: str):
    try:
        produto_data = request.json

        with Session(engine) as session:
            query = select(produto).where(Produto.codigo == codigo)
            produto.session.exec(query).first()

            if not produto:
                return jsonify({"error": "Produto não encontrado"}), 404
            
            for key, value in produto_data.items():
                if hasattr(produto, key):
                    setattr(produto, key, value)
            
            session.add(produto)
            session.commit()
            session.refresh(produto)
        
        return jsonify(produto.dict()), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@produto_bp.route('/produto/<codigo>', methods=['DELETE'])
def delete_produto(codigo: str):
    try:
        with Session(engine) as session:
            query = select(Produto).where(Produto.codigo == codigo)
            prduto = session.exec(query).first()

            if not produto:
                return jsonify({"error": "Produto não encontrado"}), 404

            session.delete(produto)
            session.commit()
        
        return jsonify({"message": "Produto não encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400
