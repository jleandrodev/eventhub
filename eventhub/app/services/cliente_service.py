from ..models import Cliente

def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, 
                           cpf=cliente.cpf, telefone=cliente.telefone, endereco=cliente.endereco)