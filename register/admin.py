from django.contrib import admin
from .models import Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name','email','city','resume','portfolio','linkedin')
    # list_filter = ('city',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
