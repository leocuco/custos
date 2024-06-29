from django.contrib import admin
from .models import Produto, Procedimento, Unidade, Especialidade, Paciente, Cirurgia, Familia, LinhasCirurgia
from django.forms import TextInput, NumberInput


class LinhasCirurgiaInline(admin.TabularInline):  # Use StackedInline para uma apresentação em pilha
    model = LinhasCirurgia
    extra = 1
    fields = ['codigo', 'descricao', 'unidade', 'custoUnitario', 'quantidade', 'total']
    # Pode adicionar outras opções de personalização aqui, como widgets personalizados.

class CirurgiaAdmin(admin.ModelAdmin):
    list_display = ['procedimento', 'paciente', 'especialidade', 'data']
    inlines = [LinhasCirurgiaInline]
    fieldsets = (
        (None, {
            'fields': ('procedimento', 'paciente', 'especialidade', 'data')
        }),
        ('Tempos', {
            'fields': ('tempoCirurgia', 'tempoInternacao', 'localInternacao')
        }),
        ('Custos', {
            'fields': ('custoFixo', 'custoVariavel', 'custoTotal')
        }),
    )

admin.site.register(Cirurgia, CirurgiaAdmin)



admin.site.register(Produto)
admin.site.register(Procedimento)
admin.site.register(Unidade)
admin.site.register(Especialidade)
admin.site.register(Paciente)
# admin.site.register(Cirurgia)
# admin.site.register(LinhasCirurgia)
admin.site.register(Familia)