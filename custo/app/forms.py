"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from app.models import Produto, Procedimento, Unidade, Especialidade, Paciente , Cirurgia, Familia, LinhasCirurgia
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



class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ['procedimento','paciente','especialidade','tempoCirurgia','tempoInternacao','localInternacao','custoFixo','custoVariavel','custoTotal','data']
        labels = {
            'procedimento':'Procedimento',
            'paciente':'Paciente',
            'especialidade':'Especialidade',
            'tempoCirurgia':'TempoCirurgia',
            'tempoInternacao':'Tempo Internamento',
            'localInternacao':'Local Internamento',
            'custoFixo':'Custo Fixo',
            'custoVariavel': 'Custo Variavel',
            'custoTotal':'CustoTotal',
            'data':'Data'
        }
        widgets = {
            'procedimento':forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'paciente':forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'especialidade':forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'tempoCirurgia': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?'}),
            'tempoInternacao':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?'}),
            'localInternacao': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True}),
            'custoFixo':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?', 'required': 'required'}),
            'custoVariavel':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?', 'required': 'required'}),
            'custoTotal':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?', 'required': 'required'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control col-md-12', 'required': True}),
        }
       

class LinhaCirurgiaForm(forms.ModelForm):
    class Meta:
        model = LinhasCirurgia
        fields = ['cirurgia','codigo','descricao','unidade','custoUnitario','quantidade','total']
        labels = {
            'cirurgia' : 'Cirurgia',
            'codigo' : 'Código',
            'descricao' : 'Descrçāo',
            'unidade': 'Unidade',
            'custoUnitario' : 'CustoUnitario',
            'quantidade': 'Quantidade',
            'total' : 'Total'
        }
        widgets = {
            'cirurgia':forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'codigo':forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'descricao': forms.TextInput(attrs={'class': 'form-control col-md-12', 'required': True}),
            'unidade':forms.Select(attrs={'class': 'form-control col-md-12', 'required': True}),
            'custoUnitario':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?'}),
            'quantidade':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?'}),
            'total':forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'pattern': '[0-9]+([\.][0-9]+)?'})
        }


LinhaCirurgiaFormset = inlineformset_factory(
    Cirurgia, 
    LinhasCirurgia,
    form= LinhaCirurgiaForm,
    extra=1,
    can_delete=True
)




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
