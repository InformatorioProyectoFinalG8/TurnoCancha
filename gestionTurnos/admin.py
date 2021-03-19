from django.contrib import admin
from .models import Cancha, Horario, Reserva


# Register your models here.

class CanchaAdmin(admin.ModelAdmin):
    pass

class HorarioAdmin(admin.ModelAdmin):
    pass

class ReservaAdmin(admin.ModelAdmin):
    pass



admin.site.register(Cancha, CanchaAdmin)

admin.site.register(Horario, HorarioAdmin)

admin.site.register(Reserva, ReservaAdmin)