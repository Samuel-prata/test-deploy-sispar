from src.model import db
from sqlalchemy import text, func

class Refund(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    colaborador = db.Column(db.String(255))
    empresa = db.Column(db.String(100))
    tipo_reembolso = db.Column(db.String(50))
    centro_custo = db.Column(db.String(150))
    ordem_interna = db.Column(db.Integer, nullable=True)
    divisao = db.Column(db.Integer, nullable = True)
    pep = db.Column(db.Integer, nullable=True)
    moeda = db.Column(db.String(10))
    valor = db.Column(db.Float)
    data = db.Column(db.Date, nullable=False, server_default=func.current_date())
    motivo = db.Column(db.String(1000))
    distancia_km = db.Column(db.String(100))
    valor_km = db.Column(db.Float)
    despesa = db.Column(db.Float)
    status = db.Column(db.String(10))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable = False)
    numero_prestacao_contas = db.Column(db.String(25))
    
    
    def __init__(self, colaborador, empresa, tipo_reembolso, centro_custo,ordem_interna, divisao, pep, moeda, valor, data, motivo, numero_prestacao_contas, employee_id, status='pendente'):
        if valor <=0:
            raise ValueError('O valor deve ser maior que 0')
    
        
        self.colaborador = colaborador
        self.empresa = empresa
        self.tipo_reembolso = tipo_reembolso
        self.centro_custo = centro_custo
        self.ordem_interna =ordem_interna
        self.divisao = divisao
        self.pep = pep
        self.moeda = moeda
        self.valor = valor
        self.data = data
        self.motivo = motivo
        self.status = status
        self.numero_prestacao_contas = numero_prestacao_contas
        self.employee_id = employee_id

        
        
    def to_dict(self):
        """Converte o objeto em um dicionário para ser usado em APIs."""
        return {
            "id": self.id,
            "value": self.valor,
            "date": self.data.isoformat() if self.date else None,
            "reason": self.motivo,
            "category": self.tipo_reembolso,
            "employee_id": self.employee_id,
        }
        