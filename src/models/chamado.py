from datetime import datetime
from src import db

class Chamado(db.Model):
    __tablename__ = 'chamados'
    
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), unique=True, nullable=False)
    responsavel = db.Column(db.String(100), nullable=False)
    empresa = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_inclusao = db.Column(db.Date, nullable=False)  # Removido o default para permitir edição
    data_agendamento = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='aberto')
    
    def __init__(self, numero, responsavel, empresa, descricao, data_agendamento, data_inclusao=None, estado='aberto'):
        self.numero = numero
        self.responsavel = responsavel
        self.empresa = empresa
        self.descricao = descricao
        # Se data_inclusao não for fornecida, usa a data atual
        self.data_inclusao = data_inclusao if data_inclusao else datetime.now().date()
        self.data_agendamento = data_agendamento
        self.estado = estado
    
    def to_dict(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'responsavel': self.responsavel,
            'empresa': self.empresa,
            'descricao': self.descricao,
            'data_inclusao': self.data_inclusao.strftime('%Y-%m-%d'),
            'data_agendamento': self.data_agendamento.strftime('%Y-%m-%d'),
            'estado': self.estado
        }
    
    @staticmethod
    def get_status_color(chamado, data_atual=None):
        if data_atual is None:
            data_atual = datetime.now().date()
            
        if chamado.estado == 'fechado':
            return 'blue'
            
        if chamado.data_agendamento == data_atual:
            return 'yellow'
        elif chamado.data_agendamento < data_atual:
            return 'red'
        else:
            return 'green'
            
    @staticmethod
    def get_status_text(chamado, data_atual=None):
        if data_atual is None:
            data_atual = datetime.now().date()
            
        if chamado.estado == 'fechado':
            return 'Resolvido'
            
        if chamado.data_agendamento == data_atual:
            return 'Vence hoje'
        elif chamado.data_agendamento < data_atual:
            return 'Atrasado'
        else:
            return 'A vencer'
