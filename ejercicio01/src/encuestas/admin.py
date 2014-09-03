from django.contrib import admin
from encuestas.models import Encuesta, Eleccion

# Register your models here.

class EleccionInline(admin.TabularInline):
    model = Eleccion
    extra = 3

class EncuestaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pregunta']}),
        ('fecha de publicacion', {'fields': ['fecha_pub'], 'classes': ['collapse']}),
    ]
    inlines = [EleccionInline]
    list_filter = ['fecha_pub']
    search_fields = ['pregunta']

admin.site.register(Encuesta, EncuestaAdmin)