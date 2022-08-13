from index import app
from flask import Flask, jsonify, request, make_response
from functools import wraps
import jwt
import datetime
from app.Http.Controllers.user_controller import *

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Falta el token.'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'El token es inválido.'}), 403

        return f(*args, **kwargs)
    return decorated  

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Cualquiera puede ver esto.'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'Esto solo esta disponible para usuarios con tokens válidos.'})

@app.route('/login', methods=['POST'])
def login():
    _json = request.json
    username = _json['username']
    password = _json['password']
    if check_login(username,password) == True:
        token = jwt.encode({'user': _json['username'],
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 
                            app.config['SECRET_KEY'])
        registrar_token(token)
        return jsonify({'token' : token.decode('UTF-8')})
    return jsonify({'message' : 'Datos inválidos.'})

@app.route("/logout", methods=["GET"])
@token_required
def logout():
    token = None
    #eliminar registro del token
    return jsonify(msg="Cerraste sesión")