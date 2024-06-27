from django.contrib import admin
from .models import Produto, Procedimento, Unidade, Especialidade, Paciente, Cirurgia, Familia, LinhasCirurgia


class LinhasCirurgiaInline(admin.TabularInline):
    model = LinhasCirurgia
    fields = ('codigo', 'descricao', 'unidade', 'custoUnitario', 'quantidade', 'total')
    extra = 1
    verbose_name = "Linha de Cirurgia"
    verbose_name_plural = "Linhas de Cirurgia"
    
class CirurgiaAdmin(admin.ModelAdmin):
    list_display = ('procedimento', 'paciente', 'especialidade', 'tempoCirurgia', 'tempoInternacao', 'localInternacao', 'custoFixo', 'custoVariavel', 'custoTotal', 'data')
    inlines = [LinhasCirurgiaInline]

admin.site.register(Cirurgia, CirurgiaAdmin)

admin.site.register(Produto)
admin.site.register(Procedimento)
admin.site.register(Unidade)
admin.site.register(Especialidade)
admin.site.register(Paciente)
# admin.site.register(Cirurgia)
# admin.site.register(LinhasCirurgia)
admin.site.register(Familia)