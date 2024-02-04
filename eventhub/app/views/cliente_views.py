from django.shortcuts import render

from ..forms import cliente_forms, endereco_forms
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service

def cadastrar_cliente(request):
    if request.method == "POST":
        form_cliente = cliente_forms.ClienteForm(request.POST)
        form_endereco = endereco_forms.EncerecoForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data['nome']
            email = form_cliente.cleaned_data['email']
            cpf = form_cliente.cleaned_data['cpf']
            telefone = form_cliente.cleaned_data['telefone']

            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data['rua']
                cidade = form_endereco.cleaned_data['cidade']
                estado = form_endereco.cleaned_data['estado']
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf,
                                           telefone=telefone, endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)

    else:
        form_cliente = cliente_forms.ClienteForm()
        form_endereco = endereco_forms.EncerecoForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})