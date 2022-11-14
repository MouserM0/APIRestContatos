import sqlite3, random, datetime
from models import Contato


def getNewId():
    return random.getrandbits(28)


contatos = [
    {
        'empresa': 'Empresa1',
        'nome': 'Rodrigo',
        'telefone': '33334444',
        'email': 'r@r.com'
    },
    {
        'empresa': 'Empresa1',
        'nome': 'Romanim',
        'telefone': '33334445',
        'email': 'r2@r2.com'
    },
    {
        'empresa': 'Empresa1',
        'nome': 'Gabriel',
        'telefone': '33334446',
        'email': 'g@g.com'
    },
    {
        'empresa': 'Empresa1',
        'nome': "Breno",
        'telefone': '33334447',
        'email': 'b@b.com'
    },
    {
        'empresa': 'Empresa2',
        'nome': 'Darmes',
        'telefone': '33334448',
        'email': 'd@d.com'
    },
    {
        'empresa': 'Empresa2',
        'nome': 'Larissa',
        'telefone': '33334449',
        'email': 'l@l.com'
    },
]

def connect():
    conn = sqlite3.connect('contatos.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contatos (id INTEGER PRIMARY KEY, empresa TEXT, nome TEXT, telefone TEXT, email TEXT)")
    conn.commit()
    conn.close()
    for i in contatos:
        ct = Contato(getNewId(), i['empresa'], i['nome'], i['telefone'],i['email'])
        insert(ct)

def insert(contato):
    conn = sqlite3.connect('contatos.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO contatos VALUES (?,?,?,?,?)", (
        contato.id,
        contato.empresa,
        contato.nome,
        contato.telefone,
        contato.email
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('contatos.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM contatos")
    rows = cur.fetchall()
    contatos = []
    for i in rows:
        contato = Contato(i[0],i[1], i[2], i[3], i[4])
        contatos.append(contato)
    conn.close()
    return contatos

def update(contato):
    conn = sqlite3.connect('contatos.db')
    cur = conn.cursor()
    cur.execute("UPDATE contatos SET empresa=?, nome=? WHERE id=?", (contato.empresa, contato.nome, contato.id))
    conn.commit()
    conn.close()

def delete(theId):
    conn = sqlite3.connect('contatos.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM contatos WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('contatos.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM contatos")
    conn.commit()
    conn.close()