"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from app.models import Produto, Procedimento, Unidade, Especialidade, Paciente , Cirurgia, Familia, LinhasCirurgia, PorteCirurgico , PorteCirurgicoCirurgia
from django.forms import inlineformset_factory , formset_factory
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'preco', 'descricao','unidade','tipoCusto','familia']
        labels = {
            'codigo': 'Código',
            'preco': 'Preço',
            'descricao': 'Descrição',
            'unidade': 'Unid.',
            'tipoCusto':'Tido de Custo',
            'familia': 'Familia'
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?', 'required': 'required'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': 'required'}),
            'unidade' : forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'familia': forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'tipoCusto':forms.Select(attrs={'class': 'form-control col-md-12', 'required': True})
        }

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = {'descricao'}
        labels = {
            'descricao': 'Descrição',
        }
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': 'required'})
        }


class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = ['sigla', 'nome', 'valor']
        labels = {
            'sigla': 'Sigla',
            'nome': 'Nome',
            'valor': 'Valor',
        }
        widgets = {
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?'}),
        }


class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = {'descricao'}
        labels = {
            'descricao': 'Descrição',
        }
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': 'required'})
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente  # Assume que você tem um modelo chamado Paciente
        fields = ['apelido', 'nome', 'datanacimento', 'localnascimento', 'nacionalidade']  # Use lista para campos
        labels = {  # Use dictionary comprehension for labels
            'apelido': 'Apelido',
            'nome': 'Nome',
            'datanacimento': 'Data de Nascimento',
            'localnascimento': 'Local de Nascimento',
            'nacionalidade': 'Nacionalidade',
        }
        widgets = {  # Use dictionary comprehension for widgets
            'apelido': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True}),
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True}),
            'datanacimento': forms.DateInput (attrs={'class': 'form-control col-md-12', 'required': True}),
            'localnascimento': forms.TextInput(attrs={'class': 'form-control col-md-12', 'format': '%Y-%m-%d' , 'required': True}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True})
        }

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['familia','descricao']
        labels = {
            'familia':'Familia',
            'descricao':'Descricao'
        }
        widgets = {
            'familia': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True}),
            'descricao': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True})
        }



class PorteCirurgicoForm(forms.ModelForm):
    class Meta:
        model = PorteCirurgico
        fields = ['descricao','tempo_minutos']
        labels = {
            'descricao':'Descrição',
            'tempo_minutos':'Tempo em Minutos'
        }
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True}),
            'tempo_minutos': forms.NumberInput(attrs={'class': 'form-control col-md-12', 'required': True})
        }

class PorteCirurgicoCirurgiaForm(forms.ModelForm):
    class Meta:
        model = PorteCirurgicoCirurgia
        fields = ['descricao', 'produto','quantidade','total']
        labels = {
            'descricao':'Descrição',
            'produto':'Produto',
            'quantidade':'Quantidade',
            'total':'Total'
        }
        widgets = {
            'descricao': forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'produto': forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control col-md-12', 'required': True}),
            'total': forms.NumberInput(attrs={'class': 'form-control col-md-12', 'required': True})
        }



class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ['portecirurgico', 'procedimento', 'paciente', 'especialidade', 'tempoCirurgia', 'tempoInternacao', 'localInternacao', 'custoFixo', 'custoVariavel', 'custoTotal']

class LinhasCirurgiaForm(forms.ModelForm):
    class Meta:
        model = LinhasCirurgia
        fields = ['codigo', 'descricao', 'unidade', 'custoUnitario', 'quantidade', 'total']

LinhasCirurgiaFormSet = inlineformset_factory(Cirurgia, LinhasCirurgia, form=LinhasCirurgiaForm, extra=1, can_delete=True)




# class CirurgiaForm(forms.ModelForm):
#     class Meta:
#         model = Cirurgia
#         fields = ['portecirurgico','procedimento', 'paciente', 'especialidade', 'tempoCirurgia', 'tempoInternacao', 'localInternacao', 'custoFixo', 'custoVariavel', 'custoTotal', 'data']
#         labels = {
#             'portecirurgico':'Porte Cirurgico',
#             'procedimento': 'Procedimento',
#             'paciente': 'Paciente',
#             'especialidade': 'Especialidade',
#             'tempoCirurgia': 'Tempo de Cirurgia',
#             'tempoInternacao': 'Tempo de Internação',
#             'localInternacao': 'Local de Internação',
#             'custoFixo': 'Custo Fixo',
#             'custoVariavel': 'Custo Variável',
#             'custoTotal': 'Custo Total',
#             'data': 'Data'
#         }
#         widgets = {
#             'Porte': forms.Select(attrs={'class': 'form-control'}),
#             'Procedimento': forms.Select(attrs={'class': 'form-control'}),
#             'Paciente': forms.Select(attrs={'class': 'form-control'}),
#             'Especialidade': forms.Select(attrs={'class': 'form-control'}),
#             'Tempo de Cirurgia': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Tempo de Internacao': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Local de Internacao': forms.TextInput(attrs={'class': 'form-control'}),
#             'Custo Fixo': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Custo Variavel': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Custo Total': forms.NumberInput(attrs={'class': 'form-control'}),
#             'Data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#         }

# class LinhasCirurgiaForm(forms.ModelForm):
#     class Meta:
#         model = LinhasCirurgia
#         fields = ['codigo', 'descricao', 'unidade', 'custoUnitario', 'quantidade', 'total']
#         labels = {
#             'codigo': 'Código',
#             'descricao': 'Descrição',
#             'unidade': 'Unidade',
#             'custoUnitario': 'Custo Unitário',
#             'quantidade': 'Quantidade',
#             'total': 'Total'
#         }
#         widgets = {
#             'codigo': forms.Select(attrs={'class': 'form-control'}),
#             'descricao': forms.TextInput(attrs={'class': 'form-control'}),
#             'unidade': forms.Select(attrs={'class': 'form-control'}),
#             'custoUnitario': forms.NumberInput(attrs={'class': 'form-control'}),
#             'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
#             'total': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# LinhaCirurgiaFormset = inlineformset_factory(
#     Cirurgia,
#     LinhasCirurgia,
#     form=LinhasCirurgiaForm,
#     extra=1,
#     can_delete=True
# )


class DashboardFilterForm(forms.Form):
    ano = forms.ChoiceField(
        choices=[(ano.year, ano.year) for ano in Cirurgia.objects.dates('data', 'year')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control col-md-12'})
    )
    mes = forms.ChoiceField(
        choices=[(mes, mes) for mes in range(1, 13)],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control col-md-12'})
    )
    cirurgia = forms.ModelChoiceField(
        queryset=Cirurgia.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control col-md-12'})
    )
