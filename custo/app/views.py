"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest 
from app.models import Produto, Procedimento, Unidade, Especialidade, Paciente, Cirurgia , Familia, LinhasCirurgia
from app.forms import ProdutoForm, ProcedimentoForm, UnidadeForm, EspecialidadeForm , PacienteForm,CirurgiaForm, FamiliaForm, LinhaCirurgiaFormset,DashboardFilterForm
from django.forms import formset_factory, inlineformset_factory
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as plotly_colors
from django.db import connection

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )



def lista_de_produto(request):
    lista_de_produtos = Produto.objects.all()
    return render(request, 'app/produto/lista_de_produto.html', {'lista_de_produtos': lista_de_produtos})


def criar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_de_produto')
    else:
        return render(request, 'app/produto/criar_produto.html', {'form': form})

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_de_produto')
    else:
        return render(request, 'app/produto/criar_produto.html', {'form': form})

def eliminar_produto(request, id):
    eliminar_produto = Produto.objects.get(id=id)
    eliminar_produto.delete()
    return redirect('lista_de_produto')

def produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'app/produto/produto.html', {'produto': produto})



def lista_de_procedimento(request):
    lista_procedimento = Procedimento.objects.all()
    return render(request, 'app/procedimento/lista_procedimento.html', {'lista_procedimento': lista_procedimento})

def criar_procedimento(request):
    form = ProcedimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_procedimento')
    else:
        return render(request, 'app/procedimento/criar_procedimento.html', {'form': form})

def editar_procedimento(request, id):
    procedimento = Procedimento.objects.get(id=id)
    form = ProcedimentoForm(request.POST or None, instance=procedimento)
    if form.is_valid():
        form.save()
        return redirect('lista_procedimento')
    else:
        return render(request, 'app/procedimento/criar_procedimento.html', {'form': form})

def eliminar_procedimento(request, id):
    eliminar_procedimento = Procedimento.objects.get(id=id)
    eliminar_procedimento.delete()
    return redirect('lista_procedimento')

def procedimento(request, id):
    procedimento= Procedimento.objects.get(id=id)
    return render(request, 'app/procedimento/procedimento.html', {'procedimento': procedimento})



def lista_unidade(request):
    lista_unidade = Unidade.objects.all()
    return render(request, 'app/unidade/lista_unidade.html', {'lista_unidade': lista_unidade})

def criar_unidade(request):
    form = UnidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_unidade')
    else:
        return render(request, 'app/unidade/criar_unidade.html', {'form': form})

def editar_unidade(request, id):
    unidade = Unidade.objects.get(id=id)
    form = UnidadeForm(request.POST or None, instance=unidade)
    if form.is_valid():
        form.save()
        return redirect('lista_unidade')
    else:
        return render(request, 'app/unidade/criar_unidade.html', {'form': form})

def eliminar_unidade(request, id):
    eliminar_unidade = Unidade.objects.get(id=id)
    eliminar_unidade.delete()
    return redirect('lista_unidade')

def unidade(request, id):
    unidade= Unidade.objects.get(id=id)
    return render(request, 'app/unidade/unidade.html', {'unidade': unidade})



def lista_especialidade(request):
    lista_especialidade= Especialidade.objects.all()
    return render(request, 'app/especialidade/lista_especialidade.html', {'lista_especialidade': lista_especialidade})

def criar_especialidade(request):
    form = EspecialidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_especialidade')
    else:
        return render(request, 'app/especialidade/criar_especialidade.html', {'form': form})

def editar_especialidade(request, id):
    especialidade = Especialidade.objects.get(id=id)
    form = EspecialidadeForm(request.POST or None, instance=especialidade)
    if form.is_valid():
        form.save()
        return redirect('lista_especialidade')
    else:
        return render(request, 'app/especialidade/criar_especialidade.html', {'form': form})

def eliminar_especialidade(request, id):
    eliminar_especialidade = Especialidade.objects.get(id=id)
    eliminar_especialidade.delete()
    return redirect('lista_especialidade')

def especialidade(request, id):
    especialidade = Especialidade.objects.get(id=id)
    return render(request, 'app/especialidade/especialidade.html', {'especialidade': especialidade})



def lista_paciente(request):
    lista_paciente= Paciente.objects.all()
    return render(request, 'app/paciente/lista_paciente.html', {'lista_paciente': lista_paciente})

def criar_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_paciente')
    else:
        return render(request, 'app/paciente/criar_paciente.html', {'form': form})

def editar_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista_paciente')
    else:
        return render(request, 'app/paciente/criar_paciente.html', {'form': form})

def eliminar_paciente(request, id):
    eliminar_paciente = Paciente.objects.get(id=id)
    eliminar_paciente.delete()
    return redirect('lista_paciente')

def paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    return render(request, 'app/paciente/paciente.html', {'paciente': paciente})


def criar_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_paciente')
    else:
        return render(request, 'app/paciente/criar_paciente.html', {'form': form})
    


def lista_familia(request):
    lista_familia= Familia.objects.all()
    return render(request, 'app/familia/lista_familia.html', {'lista_familia': lista_familia})

def criar_familia(request):
    form = FamiliaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_familia')
    else:
        return render(request, 'app/familia/criar_familia.html', {'form': form})

def editar_familia(request, id):
    familia = Familia.objects.get(id=id)
    form = FamiliaForm(request.POST or None, instance=familia)
    if form.is_valid():
        form.save()
        return redirect('lista_familia')
    else:
        return render(request, 'app/familia/criar_familia.html', {'form': form})

def eliminar_familia(request, id):
    eliminar_familia = Familia.objects.get(id=id)
    eliminar_familia.delete()
    return redirect('lista_familia')

def familia(request, id):
    familia = Familia.objects.get(id=id)
    return render(request, 'app/familia/familia.html', {'familia':familia})



def lista_cirurgia(request):
    lista_cirurgia= Cirurgia.objects.all()
    return render(request, 'app/cirurgia/lista_cirurgia.html', {'lista_cirurgia': lista_cirurgia})

def criar_cirurgia(request):
    if request.method == 'POST':
        form = CirurgiaForm(request.POST)
        formset = LinhaCirurgiaFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            cirurgia = form.save()  # Salva a cirurgia principal
            linhas = formset.save(commit=False)  # Salva as instâncias de linha temporariamente
            for linha in linhas:
                linha.cirurgia = cirurgia  # Associa a cirurgia a cada instância de linha
                linha.save()  # Salva a instância de linha individualmente
            return redirect('lista_cirurgia')  # Substitua pelo nome da sua view de lista de cirurgias
    else:
        form = CirurgiaForm()
        formset = LinhaCirurgiaFormset()
    return render(request, 'app/cirurgia/criar_cirurgia.html', {'form': form, 'formset': formset})


def editar_cirurgia(request, id):
    if request.method == 'POST':
        form = CirurgiaForm(request.POST)
        formset = LinhaCirurgiaFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            cirurgia = form.save()
            linhas = formset.save(commit=False)
            for linha in linhas:
                linha.cirurgia = cirurgia
                linha.save()
            return redirect('lista_cirurgia')  # Substitua pelo nome da sua view de lista de cirurgias
    else:
        form = CirurgiaForm()
        formset = LinhaCirurgiaFormset()
    return render(request, 'app/cirurgia/criar_cirurgia.html', {'form': form, 'formset': formset})

def eliminar_cirurgia(request, id):
    eliminar_cirurgia = Cirurgia.objects.get(id=id)
    eliminar_cirurgia.delete()
    return redirect('lista_cirurgia')

def cirurgia(request, id):
    cirurgia = Cirurgia.objects.get(id=id)
    return render(request, 'app/cirurgia/cirurgia.html', {'cirurgia':cirurgia})



def dashboard_view(request):
    form = DashboardFilterForm(request.GET or None)

    # Filtrando os dados
    cirurgias = Cirurgia.objects.all()
    if form.is_valid():
        ano = form.cleaned_data.get('ano')
        mes = form.cleaned_data.get('mes')
        cirurgia_id = form.cleaned_data.get('cirurgia')

        if ano:
            cirurgias = cirurgias.filter(data__year=ano)
        if mes:
            cirurgias = cirurgias.filter(data__month=mes)
        if cirurgia_id:
            cirurgias = cirurgias.filter(id=cirurgia_id.id)

    # Processando os dados
    df = pd.DataFrame(list(cirurgias.values()))

    if not df.empty:
        # Paleta de cores vibrante
        colors = px.colors.qualitative.Plotly

        # Gráfico de barras
        fig_bar = px.bar(df, x='data', y='custoTotal', color='procedimento_id', title='Custos Totais por Cirurgia', color_discrete_sequence=colors)
        graph_bar = fig_bar.to_html(full_html=False)

        # Tabela
        table_html = df.to_html(classes='table table-striped', index=False)

        # Gráfico de pizza
        fig_pie = px.pie(df, names='procedimento_id', values='custoTotal', title='Distribuição dos Custos por Procedimento', color_discrete_sequence=colors)
        graph_pie = fig_pie.to_html(full_html=False)
    else:
        graph_bar = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        table_html = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        graph_pie = "<p>Nenhum dado disponível para os filtros selecionados.</p>"

    return render(request, 'dashboard.html', {
        'graph_bar': graph_bar,
        'table_html': table_html,
        'graph_pie': graph_pie,
        'form': form
    })

