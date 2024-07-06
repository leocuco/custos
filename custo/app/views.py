"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest , JsonResponse
from app.models import Produto, Procedimento, Unidade, Especialidade, Paciente, Cirurgia , Familia, LinhasCirurgia, PorteCirurgico,PorteCirurgicoCirurgia
from app.forms import ProdutoForm, ProcedimentoForm, UnidadeForm, EspecialidadeForm , PacienteForm,CirurgiaForm, FamiliaForm,DashboardFilterForm, PorteCirurgicoForm,PorteCirurgicoCirurgiaForm
from django.forms import formset_factory, inlineformset_factory
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as plotly_colors
from django.db import connection
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CirurgiaForm, LinhasCirurgiaFormSet
import plotly.graph_objects as go

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Pagina Inicial',
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
            'title':'Contacto',
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
            'title':'Sobre Nós',
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


#Porte Cirurgico
def lista_porte(request):
    lista_porte= PorteCirurgico.objects.all()
    return render(request, 'app/portecirurgico/lista_porte.html', {'lista_porte': lista_porte})

def criar_porte(request):
    form = PorteCirurgicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_porte')
    else:
        return render(request, 'app/portecirurgico/criar_porte.html', {'form': form})
    
def editar_porte(request, id):
    porte = PorteCirurgico.objects.get(id=id)
    form = PorteCirurgicoForm(request.POST or None, instance=porte)
    if form.is_valid():
        form.save()
        return redirect('lista_porte')
    else:
        return render(request, 'app/portecirurgico/criar_porte.html', {'form': form})

def eliminar_porte(request, id):
    eliminar_porte = PorteCirurgico.objects.get(id=id)
    eliminar_porte.delete()
    return redirect('lista_porte')

def porte(request, id):
    porte = PorteCirurgico.objects.get(id=id)
    return render(request, 'app/portecirurgico/porte.html', {'porte':porte})

#Porte Cirurgico Cirurgia
def lista_portecirurgia(request):
    lista_portecirurgia= PorteCirurgicoCirurgia.objects.all()
    return render(request, 'app/portecirurgia/lista_portecirurgia.html', {'lista_portecirurgia': lista_portecirurgia})

def criar_portecirurgia(request):
    form = PorteCirurgicoCirurgiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_portecirurgia')
    else:
        return render(request, 'app/portecirurgia/criar_portecirurgia.html', {'form': form})
    

def editar_portecirurgia(request, id):
    portecirurgia = PorteCirurgicoCirurgia.objects.get(id=id)
    form = PorteCirurgicoCirurgiaForm(request.POST or None, instance=portecirurgia)
    if form.is_valid():
        form.save()
        return redirect('lista_portecirurgia')
    else:
        return render(request, 'app/portecirurgia/criar_portecirurgia.html', {'form': form})


def eliminar_portecirurgia(request, id):
    eliminar_portecirurgia = PorteCirurgicoCirurgia.objects.get(id=id)
    eliminar_portecirurgia.delete()
    return redirect('lista_portecirurgia')

def portecirurgia(request, id):
    portecirurgia = PorteCirurgicoCirurgia.objects.get(id=id)
    return render(request, 'app/portecirurgia/portecirurgia.html', {'portecirurgia':portecirurgia})












# Cirurgia

def lista_cirurgia(request):
    lista_cirurgia= Cirurgia.objects.all()
    return render(request, 'app/cirurgia/lista_cirurgia.html', {'lista_cirurgia': lista_cirurgia})


# def criar_cirurgia(request):
#     if request.method == 'POST':
#         form = CirurgiaForm(request.POST)
#         formset = LinhaCirurgiaFormset(request.POST, request.FILES)
#         if form.is_valid() and formset.is_valid():
#             cirurgia = form.save()  # Salva a cirurgia principal
#             linhas = formset.save(commit=False)  # Salva as instâncias de linha temporariamente
#             for linha in linhas:
#                 linha.cirurgia = cirurgia  # Associa a cirurgia a cada instância de linha
#                 linha.save()  # Salva a instância de linha individualmente
#             return redirect('lista_cirurgia')  # Substitua pelo nome da sua view de lista de cirurgias
#     else:
#         form = CirurgiaForm()
#         formset = LinhaCirurgiaFormset()
#     return render(request, 'app/cirurgia/criar_cirurgia.html', {'form': form, 'formset': formset})



# def editar_cirurgia(request, id):
#     if request.method == 'POST':
#         form = CirurgiaForm(request.POST)
#         formset = LinhaCirurgiaFormset(request.POST, request.FILES)
#         if form.is_valid() and formset.is_valid():
#             cirurgia = form.save()
#             linhas = formset.save(commit=False)
#             for linha in linhas:
#                 linha.cirurgia = cirurgia
#                 linha.save()
#             return redirect('lista_cirurgia')  # Substitua pelo nome da sua view de lista de cirurgias
#     else:
#         form = CirurgiaForm()
#         formset = LinhaCirurgiaFormset()
#     return render(request, 'app/cirurgia/criar_cirurgia.html', {'form': form, 'formset': formset})

# def eliminar_cirurgia(request, id):
#     eliminar_cirurgia = Cirurgia.objects.get(id=id)
#     eliminar_cirurgia.delete()
#     return redirect('lista_cirurgia')

# def cirurgia(request, id):
#     cirurgia = Cirurgia.objects.get(id=id)
#     return render(request, 'app/cirurgia/cirurgia.html', {'cirurgia':cirurgia})



#Dashboard

# def dashboard_view(request):
#     form = DashboardFilterForm(request.GET or None)

#     # Filtrando os dados
#     cirurgias = Cirurgia.objects.all()
#     if form.is_valid():
#         ano = form.cleaned_data.get('ano')
#         mes = form.cleaned_data.get('mes')
#         cirurgia_id = form.cleaned_data.get('cirurgia')

#         if ano:
#             cirurgias = cirurgias.filter(data__year=ano)
#         if mes:
#             cirurgias = cirurgias.filter(data__month=mes)
#         if cirurgia_id:
#             cirurgias = cirurgias.filter(id=cirurgia_id.id)

#     # Processando os dados
#     df = pd.DataFrame(list(cirurgias.values()))

#     if not df.empty:
#         # Paleta de cores vibrante
#         colors = px.colors.qualitative.Plotly


#         # Gráfico de barras
#         fig_bar = px.bar(
#             df, 
#             x='data', 
#             y='custoTotal', 
#             color='procedimento_id', 
#             title='Custos Totais por Cirurgia', 
#             color_discrete_sequence=colors, 
#             barmode='group'
#         )
#         fig_bar.update_layout(barmode='group')
#         graph_bar = fig_bar.to_html(full_html=False)


#         # Tabela
#         table_html = df.to_html(classes='table table-striped', index=False)

#         # Gráfico de pizza
#         fig_pie = px.pie(
#             df, 
#             names='procedimento_id', 
#             values='custoTotal', 
#             title='Distribuição dos Custos por Procedimento', 
#             color_discrete_sequence=colors
#         )
#         graph_pie = fig_pie.to_html(full_html=False)
#     else:
#         graph_bar = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
#         table_html = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
#         graph_pie = "<p>Nenhum dado disponível para os filtros selecionados.</p>"

#     return render(request, 'dashboard.html', {
#         'graph_bar': graph_bar,
#         'table_html': table_html,
#         'graph_pie': graph_pie,
#         'form': form
#     })
#Dashboard

import plotly.express as px
import pandas as pd
from django.shortcuts import render
from .models import Cirurgia, LinhasCirurgia
from .forms import DashboardFilterForm

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
    df_cirurgias = pd.DataFrame(list(cirurgias.values(
        'id', 'paciente__nome', 'data', 'custoFixo', 'custoVariavel', 'custoTotal', 'portecirurgico__descricao', 'procedimento__descricao'
    )))

    # Obtendo linhas de cirurgia para dados adicionais
    linhas_cirurgias = LinhasCirurgia.objects.filter(cirurgia__in=cirurgias).select_related('codigo__familia')
    df_linhas = pd.DataFrame(list(linhas_cirurgias.values(
        'cirurgia__id', 'codigo__familia__descricao', 'total'
    )))

    if not df_cirurgias.empty:
        # Paleta de cores vibrante
        colors = px.colors.qualitative.Plotly

        # Gráfico de barras para custo total por paciente e procedimento
        df_costs_by_patient_procedure = df_cirurgias.groupby(['paciente__nome', 'procedimento__descricao'])['custoTotal'].sum().reset_index()
        fig_bar_patient_procedure = px.bar(
            df_costs_by_patient_procedure,
            x='paciente__nome',
            y='custoTotal',
            color='procedimento__descricao',
            text='custoTotal',
            title='Custos Totais por Paciente e Procedimento',
            color_discrete_sequence=colors,
            labels={'paciente__nome': 'Paciente', 'custoTotal': 'Custo Total', 'procedimento__descricao': 'Procedimento'},
            barmode='group'
        )
        fig_bar_patient_procedure.update_layout(
            xaxis_title='Paciente',
            yaxis_title='Custo Total',
            xaxis=dict(tickmode='linear'),
            showlegend=True
        )
        fig_bar_patient_procedure.update_traces(texttemplate='%{text}', textposition='outside')
        graph_bar_patient_procedure = fig_bar_patient_procedure.to_html(full_html=False)

        # Gráfico de barras empilhadas para Custos Fixos e Variáveis
        df_stacked = df_cirurgias.groupby('id')[['custoFixo', 'custoVariavel']].sum().reset_index()
        df_stacked = df_stacked.melt(id_vars=['id'], value_vars=['custoFixo', 'custoVariavel'],
                                     var_name='Tipo de Custo', value_name='Valor')
        fig_bar_stacked = px.bar(
            df_stacked,
            x='id',
            y='Valor',
            color='Tipo de Custo',
            text='Valor',
            title='Custos Fixos e Variáveis por Cirurgia',
            color_discrete_sequence=colors,
            labels={'id': 'ID da Cirurgia', 'Valor': 'Valor'},
            barmode='stack'
        )
        fig_bar_stacked.update_layout(
            xaxis_title='ID da Cirurgia',
            yaxis_title='Valor',
            xaxis=dict(tickmode='linear'),
            showlegend=True
        )
        fig_bar_stacked.update_traces(texttemplate='%{text}', textposition='outside')
        graph_bar_stacked = fig_bar_stacked.to_html(full_html=False)

        # Gráfico de pizza para custo por procedimento
        fig_pie = px.pie(
            df_cirurgias,
            names='procedimento__descricao',
            values='custoTotal',
            title='Distribuição dos Custos por Procedimento',
            color_discrete_sequence=colors
        )
        graph_pie = fig_pie.to_html(full_html=False)

        # Gráfico de pizza para custo por porte cirúrgico
        fig_pie_porte = px.pie(
            df_cirurgias,
            names='portecirurgico__descricao',
            values='custoTotal',
            title='Distribuição dos Custos por Porte Cirúrgico',
            color_discrete_sequence=colors
        )
        graph_pie_porte = fig_pie_porte.to_html(full_html=False)

        # Gráfico de pizza para custo por família
        df_familias = df_linhas.groupby('codigo__familia__descricao').agg({'total': 'sum'}).reset_index()
        fig_pie_familia = px.pie(
            df_familias,
            names='codigo__familia__descricao',
            values='total',
            title='Distribuição dos Custos por Família',
            color_discrete_sequence=colors
        )
        graph_pie_familia = fig_pie_familia.to_html(full_html=False)

        # Gráfico de pizza para número de cirurgias por porte cirúrgico
        df_cirurgias_porte = df_cirurgias.groupby('portecirurgico__descricao').size().reset_index(name='count')
        fig_pie_cirurgias_porte = px.pie(
            df_cirurgias_porte,
            names='portecirurgico__descricao',
            values='count',
            title='Número de Cirurgias por Porte Cirúrgico',
            color_discrete_sequence=colors
        )
        graph_pie_cirurgias_porte = fig_pie_cirurgias_porte.to_html(full_html=False)

        # Gráfico de linha para custos ao longo do tempo
        df_line = df_cirurgias.groupby(['data'])[['custoFixo', 'custoVariavel']].sum().reset_index()
        fig_line = px.line(
            df_line,
            x='data',
            y=['custoFixo', 'custoVariavel'],
            title='Custos ao Longo do Tempo',
            labels={'data': 'Data', 'value': 'Valor', 'variable': 'Tipo de Custo'}
        )
        graph_line = fig_line.to_html(full_html=False)

        # Tabela com detalhes das cirurgias
        table_html = df_cirurgias.to_html(classes='table table-striped', index=False)
    else:
        graph_bar_patient_procedure = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        graph_bar_stacked = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        graph_pie = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        graph_pie_porte = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        graph_pie_familia = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        graph_pie_cirurgias_porte = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        graph_line = "<p>Nenhum dado disponível para os filtros selecionados.</p>"
        table_html = "<p>Nenhum dado disponível para os filtros selecionados.</p>"

    return render(request, 'dashboard.html', {
        'form': form,
        'graph_bar_patient_procedure': graph_bar_patient_procedure,
        'graph_bar_stacked': graph_bar_stacked,
        'graph_pie': graph_pie,
        'graph_pie_porte': graph_pie_porte,
        'graph_pie_familia': graph_pie_familia,
        'graph_pie_cirurgias_porte': graph_pie_cirurgias_porte,
        'graph_line': graph_line,
        'table_html': table_html,
    })


#Cirurgia

# Classe para criar uma nova Cirurgia
class CirurgiaCreateView(CreateView):
    model = Cirurgia  # Define o modelo como Cirurgia
    form_class = CirurgiaForm  # Define a classe do formulário como CirurgiaForm
    template_name = 'app/cirurgia/cirurgia_form.html'  # Define o nome do template como 'app/cirurgia/cirurgia_form.html'
    success_url = reverse_lazy('lista_cirurgia')  # Define a URL de redirecionamento após o sucesso como 'lista_cirurgia'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)  # Obtém os dados do contexto da superclasse
        if self.request.POST:
            data['formset'] = LinhasCirurgiaFormSet(self.request.POST)  # Cria uma instância do formset LinhasCirurgiaFormSet com os dados do POST
        else:
            data['formset'] = LinhasCirurgiaFormSet()  # Cria uma instância    def form_valid(self, form):
        context = self.get_context_data()  # Obtém o contexto
        formset = context['formset']  # Obtém o formset do contexto
        if formset.is_valid():
            # Add your code here if the formset is valid
            pass
        else:
            # Add your code here if the formset is not valid
            passexto
        if formset.is_valid():  # Verifica se o formset é válido
            print("Formset is valid")
            self.object = form.save()  # Salva o formulário principal
            formset.instance = self.object  # Associa o objeto do formset ao objeto principal
            formset.save()  # Salva o formset
            self.object.update_costs()  # Atualiza os custos após salvar as linhas
            return redirect(self.success_url)  # Redireciona para a URL de sucesso
        else:
            print("Formset is invalid")
            return self.form_invalid(form)  # Retorna o formulário inválido


# Classe para atualizar uma Cirurgia existente
class CirurgiaUpdateView(UpdateView):
    model = Cirurgia
    form_class = CirurgiaForm
    template_name = 'app/cirurgia/cirurgia_form.html'
    success_url = reverse_lazy('lista_cirurgia')

    def get_context_data(self, **kwargs):
        # Obtém os dados do contexto
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            # Se houver uma requisição POST, cria uma instância do formset com os dados da requisição e a instância da cirurgia
            data['formset'] = LinhasCirurgiaFormSet(self.request.POST, instance=self.object)
        else:
            # Caso contrário, cria uma instância do formset com a instância da cirurgia
            data['formset'] = LinhasCirurgiaFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        # Obtém o contexto
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            # Se o formset for válido, salva a instância do form e do formset
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            self.object.update_costs()  # Atualiza os custos após salvar as linhas
            return redirect(self.success_url)
        else:
            print("Formset is invalid")
            return self.form_invalid(form)
        
# Função para obter os detalhes de um Produto
def get_produto_details(pk):
    produto = Produto.objects.get(pk=pk)
    data = {
        'descricao': produto.descricao,
        'unidade': produto.unidade,
        'custo_unitario': produto.preco,
    }
    return JsonResponse(data)
