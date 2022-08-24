from index import app
from flask import Flask, jsonify, request, make_response
from flask import session
from functools import wraps
import jwt
import datetime
from app.Http.Controllers.user_controller import *

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'token' not in session:
            return jsonify({'message' : 'Falta el token.'}), 403
        try:
            data = jwt.decode(session['token'], app.config['SECRET_KEY'])
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
        user = get_data_user(username)
        session['name'] = user.name
        session['role_id'] = user.role_id
        role = get_data_role(user.role_id)
        session['role'] = role.nombre
        token_info = jwt.encode({'username': _json['username'],
                            'name': session['name'],
                            'role_id': session['role_id'],
                            'role': session['role'],
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 
                            app.config['SECRET_KEY'])
        session['token'] = token_info.decode('UTF-8')
        return jsonify({'token' : token_info.decode('UTF-8')})
    return jsonify({'message' : 'Datos inválidos.'})

@app.route("/logout", methods=["GET"])
@token_required
def logout():
    session.clear()
    return jsonify(msg="Cerraste sesión")