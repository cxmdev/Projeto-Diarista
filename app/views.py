from django.shortcuts import redirect, render
from .forms import TarefaForm
from .models import Tarefa


def cadastrar_tarefa(request):
    if request.method == "POST":
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            form_tarefa.save()
            return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(request, "form_cadastro.html", {"form_tarefa": form_tarefa})


def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "lista_tarefas.html", {"tarefas": tarefas})
