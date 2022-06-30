from django.contrib import admin

# Register your models here.

from core.models import Categoria
from core.models import Marca

admin.site.register(Categoria)
admin.site.register(Marca)
