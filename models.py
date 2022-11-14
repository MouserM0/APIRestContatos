class Contato:
  def __init__(self, id, empresa, nome, telefone, email):
    self.id = id
    self.nome = nome
    self.empresa = empresa
    self.email = email
    self.telefone = telefone

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'nome': self.nome,
      'empresa': self.empresa,
      'email':self.email,
      'telefone':self.telefone
    }