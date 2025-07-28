from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
from src import db
from src.models.chamado import Chamado
import logging

chamados_bp = Blueprint('chamados', __name__, url_prefix='/chamados')

@chamados_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obter dados do formulário
        numero = request.form.get('numero')
        responsavel = request.form.get('responsavel')
        empresa = request.form.get('empresa')
        descricao = request.form.get('descricao')
        data_inclusao_str = request.form.get('data_inclusao')
        data_agendamento_str = request.form.get('data_agendamento')
        estado = request.form.get('estado', 'aberto')
        
        # Log para debug
        print(f"Dados recebidos: numero={numero}, responsavel={responsavel}, empresa={empresa}")
        print(f"data_inclusao={data_inclusao_str}, data_agendamento={data_agendamento_str}, estado={estado}")
        
        # Validar dados
        if not numero or not responsavel or not empresa or not descricao:
            return render_template('registro_chamado.html', error="Todos os campos são obrigatórios", hoje=datetime.now().strftime('%Y-%m-%d'))
        
        # Verificar se as datas estão vazias e usar valores padrão se necessário
        if not data_inclusao_str:
            data_inclusao_str = datetime.now().strftime('%Y-%m-%d')
        
        if not data_agendamento_str:
            # Se não houver data de agendamento, usar data atual + 7 dias como padrão
            data_agendamento_str = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)).strftime('%Y-%m-%d')
        
        try:
            # Verificar se o número já existe
            chamado_existente = Chamado.query.filter_by(numero=numero).first()
            if chamado_existente:
                return render_template('registro_chamado.html', error="Número de chamado já existe. Por favor, use outro número.", hoje=datetime.now().strftime('%Y-%m-%d'))
            
            # Converter strings para datas com tratamento de erro mais detalhado
            try:
                data_inclusao = datetime.strptime(data_inclusao_str, '%Y-%m-%d').date()
            except ValueError as e:
                print(f"Erro ao converter data_inclusao: {str(e)}, valor recebido: {data_inclusao_str}")
                return render_template('registro_chamado.html', error=f"Formato de data de inclusão inválido: {data_inclusao_str}", hoje=datetime.now().strftime('%Y-%m-%d'))
            
            try:
                data_agendamento = datetime.strptime(data_agendamento_str, '%Y-%m-%d').date()
            except ValueError as e:
                print(f"Erro ao converter data_agendamento: {str(e)}, valor recebido: {data_agendamento_str}")
                return render_template('registro_chamado.html', error=f"Formato de data de agendamento inválido: {data_agendamento_str}", hoje=datetime.now().strftime('%Y-%m-%d'))
            
            # Criar novo chamado
            novo_chamado = Chamado(
                numero=numero,
                responsavel=responsavel,
                empresa=empresa,
                descricao=descricao,
                data_inclusao=data_inclusao,
                data_agendamento=data_agendamento,
                estado=estado
            )
            
            # Salvar no banco
            db.session.add(novo_chamado)
            db.session.commit()
            print(f"Chamado salvo com sucesso: ID={novo_chamado.id}, numero={novo_chamado.numero}")
            
            # Redirecionar para o dashboard
            return redirect(url_for('chamados.dashboard'))
            
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar chamado: {str(e)}")
            return render_template('registro_chamado.html', error=f"Erro ao salvar: {str(e)}", hoje=datetime.now().strftime('%Y-%m-%d'))
    
    # GET request - exibir formulário
    return render_template('registro_chamado.html', hoje=datetime.now().strftime('%Y-%m-%d'))

@chamados_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@chamados_bp.route('/gerenciar')
def gerenciar():
    return render_template('gerenciar.html')

@chamados_bp.route('/api/chamados', methods=['GET'])
def listar_chamados():
    chamados = Chamado.query.all()
    return jsonify([chamado.to_dict() for chamado in chamados])

@chamados_bp.route('/api/chamados/<int:id>', methods=['GET'])
def obter_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    return jsonify(chamado.to_dict())

@chamados_bp.route('/api/chamados/<int:id>', methods=['PUT'])
def atualizar_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    data = request.json
    
    # Verificar se o número está sendo alterado e se já existe
    if 'numero' in data and data['numero'] != chamado.numero:
        chamado_existente = Chamado.query.filter_by(numero=data['numero']).first()
        if chamado_existente:
            return jsonify({"error": "Número de chamado já existe"}), 400
    
    # Atualizar campos
    chamado.numero = data.get('numero', chamado.numero)
    chamado.responsavel = data.get('responsavel', chamado.responsavel)
    chamado.empresa = data.get('empresa', chamado.empresa)
    chamado.descricao = data.get('descricao', chamado.descricao)
    
    if 'data_inclusao' in data:
        chamado.data_inclusao = datetime.strptime(data['data_inclusao'], '%Y-%m-%d').date()
        
    if 'data_agendamento' in data:
        chamado.data_agendamento = datetime.strptime(data['data_agendamento'], '%Y-%m-%d').date()
    
    chamado.estado = data.get('estado', chamado.estado)
    
    db.session.commit()
    return jsonify(chamado.to_dict())

@chamados_bp.route('/api/chamados/<int:id>', methods=['DELETE'])
def excluir_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    db.session.delete(chamado)
    db.session.commit()
    return jsonify({"message": "Chamado excluído com sucesso"})

@chamados_bp.route('/api/chamados/<int:id>/resolver', methods=['PUT'])
def resolver_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    chamado.estado = 'fechado'
    db.session.commit()
    return jsonify(chamado.to_dict())
