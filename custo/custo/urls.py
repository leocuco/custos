"""
Definition of urls for custo.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.views.generic.edit import CreateView, UpdateView



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    #Produto
    path('produto/', views.lista_de_produto, name='lista_de_produto'),
    path('produto/novo', views.criar_produto, name='criar_produto'),
    path('produto/<int:id>/', views.produto, name='produto'),
    path('produto/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produto/remover/<int:id>/', views.eliminar_produto, name='eliminar_produto'),
    #Procedimento
    path('procedimento/', views.lista_de_procedimento, name='lista_procedimento'),
    path('procedimento/novo', views.criar_procedimento, name='criar_procedimento'),
    path('procedimento/<int:id>/', views.procedimento, name='procedimento'),
    path('procedimento/editar/<int:id>/', views.editar_procedimento, name='editar_procedimento'),
    path('procedimento/remover/<int:id>/', views.eliminar_procedimento, name='eliminar_procedimento'),
    #Unidade
    path('unidade/', views.lista_unidade, name='lista_unidade'),
    path('unidade/novo', views.criar_unidade, name='criar_unidade'),
    path('unidade/<int:id>/', views.unidade, name='unidade'),
    path('unidade/editar/<int:id>/', views.editar_unidade, name='editar_unidade'),
    path('unidade/remover/<int:id>/', views.eliminar_unidade, name='eliminar_unidade'),
    #Especialidade
    path('especialidade/', views.lista_especialidade, name='lista_especialidade'),
    path('especialidade/novo', views.criar_especialidade, name='criar_especialidade'),
    path('especialidade/<int:id>/', views.especialidade, name='especialidade'),
    path('especialidade/editar/<int:id>/', views.editar_especialidade, name='editar_especialidade'),
    path('especialidade/remover/<int:id>/', views.eliminar_especialidade, name='eliminar_especialidade'),
    #Paciente
    path('paciente/', views.lista_paciente, name='lista_paciente'),
    path('paciente/novo', views.criar_paciente, name='criar_paciente'),
    path('paciente/<int:id>/', views.paciente, name='paciente'),
    path('paciente/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('paciente/remover/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
    #Familia
    path('familia/', views.lista_familia, name='lista_familia'),
    path('familia/novo', views.criar_familia, name='criar_familia'),
    path('familia/<int:id>/', views.familia, name='familia'),
    path('familia/editar/<int:id>/', views.editar_familia, name='editar_familia'),
    path('familia/remover/<int:id>/', views.eliminar_familia, name='eliminar_familia'),

    #Cirurgia
    path('cirurgia/', views.lista_cirurgia, name='lista_cirurgia'),
    # path('cirurgia/novo', views.criar_cirurgia, name='criar_cirurgia'),
    # path('cirurgia/<int:id>/', views.cirurgia, name='cirurgia'),
    # path('cirurgia/editar/<int:id>/', views.editar_cirurgia, name='editar_cirurgia'),
    # path('cirurgia/remover/<int:id>/', views.eliminar_cirurgia, name='eliminar_cirurgia'),
    # path('cirurgia/add/', views.CirurgiaCreateView, name='add_cirurgia'),
    # path('cirurgia/<int:pk>/edit/', views.CirurgiaUpdateView, name='edit_cirurgia'),
    path('cirurgia/add/', views.CirurgiaCreateView.as_view(), name='add_cirurgia'),
    path('cirurgia/<int:pk>/edit/', views.CirurgiaUpdateView.as_view(), name='edit_cirurgia'),
    path('get_produto_details/<int:pk>/',views.get_produto_details, name='get_produto_details'),

    #Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
    #Porte Cirurgico
    path('porte/', views.lista_porte, name='lista_porte'),
    path('porte/novo', views.criar_porte, name='criar_porte'),
    path('porte/<int:id>/', views.porte, name='porte'),
    path('porte/editar/<int:id>/', views.editar_porte, name='editar_porte'),
    path('porte/remover/<int:id>/', views.eliminar_porte, name='eliminar_porte'),
    #Porte Cirurgico Cirurgia
    path('portecirurgia/', views.lista_portecirurgia, name='lista_portecirurgia'),
    path('portecirurgia/novo', views.criar_portecirurgia, name='criar_portecirurgia'),
    path('portecirurgia/<int:id>/', views.portecirurgia, name='portecirurgia'),
    path('portecirurgia/editar/<int:id>/', views.editar_portecirurgia, name='editar_portecirurgia'),
    path('portecirurgia/remover/<int:id>/', views.eliminar_portecirurgia, name='eliminar_portecirurgia'),
    #api
    path('ft/', views.ft_view, name='ft_view'),
    path('ft/<int:fno>/', views.ft_detail_view, name='ft_detail_view'),
]
