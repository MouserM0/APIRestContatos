from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db
from models import Contato


app = Flask(__name__)

if not os.path.isfile('contatos.db'):
    db.connect()

@app.route("/")
def index():
    return render_template("index.html")

def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return True
    else:
      return False


@app.route("/request", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    email = req_data['email']
    if not isValid(email):
        return jsonify({
            'status': '422',
            'res': 'failure',
            'error': 'Email invalido. Por favor insira um endereço de email existente'
        })
    nome = req_data['nome']
    cts = [b.serialize() for b in db.view()]
    for b in cts:
        if b['nome'] == nome:
            return jsonify({
                # 'error': '',
                'res': f'Error ⛔❌! o contato {nome} já existe no banco de dados!',
                'status': '404'
            })

    ct = Contato(db.getNewId(), True, nome, datetime.datetime.now())
    print('new contato: ', ct.serialize())
    db.insert(ct)
    new_cts = [b.serialize() for b in db.view()]
    print('contatos in lib: ', new_cts)
    
    return jsonify({
                # 'error': '',
                'res': ct.serialize(),
                'status': '200',
                'msg': 'Sucesso criando um novo contato!👍😀'
            })


@app.route('/request', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    cts = [b.serialize() for b in db.view()]
    if (content_type == 'application/json'):
        json = request.json
        for b in cts:
            if b['id'] == int(json['id']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Sucesso recebendo os contatos do banco!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Contato com o id '{json['id']}' não encontrado!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': cts,
                    'status': '200',
                    'msg': 'Sucesso recebendo os contatos do banco!👍😀',
                    'no_of_contatos': len(cts)
                })


@app.route('/request/<id>', methods=['GET'])
def getRequestId(id):
    req_args = request.view_args
    # print('req_args: ', req_args)
    cts = [b.serialize() for b in db.view()]
    if req_args:
        for b in cts:
            if b['id'] == int(req_args['id']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pelo ID!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Contato com o id '{req_args['id']}' não encontrado!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': cts,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pelo ID!👍😀',
                    'no_of_contatos': len(cts)
                })

@app.route('/request/nome/<nome>', methods=['GET'])
def getRequestNome(nome):
    req_args = request.view_args
    # print('req_args: ', req_args)
    cts = [b.serialize() for b in db.view()]
    if req_args:
        for b in cts:
            if b['nome'] == str(req_args['nome']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pelo nome!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Contato com o nome '{req_args['nome']}' não encontrado!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': cts,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pelo nome!👍😀',
                    'no_of_contatos': len(cts)
                })

@app.route('/request/emp/<empresa>', methods=['GET'])
def getRequestEmp(empresa):
    req_args = request.view_args
    # print('req_args: ', req_args)
    cts = [b.serialize() for b in db.view()]
    if req_args:
        for b in cts:
            if b['empresa'] == str(req_args['empresa']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pela empresa!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Contato com a empresa '{req_args['empresa']}' não encontrado!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': cts,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pela empresa!👍😀',
                    'no_of_contatos': len(cts)
                })

@app.route('/request/email/<email>', methods=['GET'])
def getRequestEmail(email):
    req_args = request.view_args
    # print('req_args: ', req_args)
    cts = [b.serialize() for b in db.view()]
    if req_args:
        for b in cts:
            if b['email'] == str(req_args['email']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pelo email!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Contato com o email '{req_args['email']}' não encontrado!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': cts,
                    'status': '200',
                    'msg': 'Sucesso recebendo o contato pelo email!👍😀',
                    'no_of_contatos': len(cts)
                })

@app.route("/request", methods=['PUT'])
def putRequest():
    req_data = request.get_json()
    availability = req_data['empresa']
    nome = req_data['nome']
    the_id = req_data['id']
    cts = [b.serialize() for b in db.view()]
    for b in cts:
        if b['id'] == the_id:
            ct = Contato(
                the_id, 
                availability, 
                nome, 
                datetime.datetime.now()
            )
            print('new contato: ', ct.serialize())
            db.update(ct)
            new_cts = [b.serialize() for b in db.view()]
            print('contatos in lib: ', new_cts)
            return jsonify({
                # 'error': '',
                'res': ct.serialize(),
                'status': '200',
                'msg': f'Sucesso atualizand o contato {nome}!👍😀'
            })        
    return jsonify({
                # 'error': '',
                'res': f'Error ⛔❌! Falha ao atualizar o contato {nome}!',
                'status': '404'
            })
    
    


@app.route('/request/<id>', methods=['DELETE'])
def deleteRequest(id):
    req_args = request.view_args
    print('req_args: ', req_args)
    cts = [b.serialize() for b in db.view()]
    if req_args:
        for b in cts:
            if b['id'] == int(req_args['id']):
                db.delete(b['id'])
                updated_cts = [b.serialize() for b in db.view()]
                print('updated_cts: ', updated_cts)
                return jsonify({
                    'res': updated_cts,
                    'status': '200',
                    'msg': 'Suceso deletando o contato pelo ID!👍😀',
                    'no_of_contatos': len(updated_cts)
                })
    else:
        return jsonify({
            'error': f"Error ⛔❌! Nenhum ID de contato enviado!",
            'res': '',
            'status': '404'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)