from django.contrib import admin
from .models import recien_nacido
from .models import madre_padre
from .models import seguimiento
# Register your models here.
class recien_nacidoAdmin(admin.ModelAdmin):
        list_display=['__all__']
admin.site.register(recien_nacido)
admin.site.register(madre_padre)
admin.site.register(seguimiento)