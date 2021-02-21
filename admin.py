from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget, CharWidget
from .models import Projeto, Tema, Autor, Natureza
from import_export.admin import ImportExportModelAdmin
from cidadaos.admin import M2MCreateWithForeignKey, M2MField


class ForeignCreateWidget(ForeignKeyWidget):

    def clean(self, value, row=None, *args, **kwargs):
        return self.model.objects.get_or_create(**{self.field:value})[0] if value else None

# Register your models here
class ProjetoResource(resources.ModelResource):
    autor = M2MField(attribute="autor",column_name='autor',widget=M2MCreateWithForeignKey(Autor,',', 'nome', create=True))
    tema = M2MField(attribute="tema",column_name='tema',widget=M2MCreateWithForeignKey(Tema,',', 'tema', create=True))
    natureza = Field(attribute="natureza",column_name='natureza',widget=ForeignCreateWidget(Natureza, 'nome'))

    class Meta:
        model = Projeto

class ProjetoAdmin(ImportExportModelAdmin): 
    resource_class = ProjetoResource
    list_display = ('nome',)

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Tema)
admin.site.register(Autor)
admin.site.register(Natureza)