from django.contrib import admin
from .models import Patron

# Register your models here.

class PatronAdmin(admin.ModelAdmin):
    list_display = ("fname", "mname", "lname", "mobile", "start_date",)

admin.site.register(Patron, PatronAdmin)
