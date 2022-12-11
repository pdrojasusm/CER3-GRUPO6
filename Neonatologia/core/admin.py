from django.contrib import admin
from .models import recien_nacido
from .models import madre_padre
from .models import seguimiento
from .models import UserMatrona

# Register your models here.
admin.site.register(recien_nacido)
admin.site.register(madre_padre)
admin.site.register(seguimiento)
admin.site.register(UserMatrona)