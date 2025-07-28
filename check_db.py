from src import create_app
from src.models.chamado import Chamado

app = create_app()

with app.app_context():
    chamados = Chamado.query.all()
    if chamados:
        print(f"Total de chamados: {len(chamados)}")
        for chamado in chamados:
            print(f"ID: {chamado.id}, Número: {chamado.numero}, Responsável: {chamado.responsavel}, Estado: {chamado.estado}")
    else:
        print("Nenhum chamado encontrado no banco de dados.")
