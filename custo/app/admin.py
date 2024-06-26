from django.contrib import admin
from .models import Produto, Procedimento, Unidade, Especialidade, Paciente, Cirurgia, Familia, LinhasCirurgia

admin.site.register(Produto)
admin.site.register(Procedimento)
admin.site.register(Unidade)
admin.site.register(Especialidade)
admin.site.register(Paciente)
admin.site.register(Cirurgia)
admin.site.register(LinhasCirurgia)
admin.site.register(Familia)