from django.contrib import admin
from .models import Category, Malumot



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_display_links = ('ism', 'fm', 'ifo', 'bulim', 'lavozim', 'is_published')
    # search_fields = ('ifo',)
    # list_editable = ('is_published', )
    # list_filter = ('is_published', 'bulim')
    # prepopulated_fields = {'slug': ('ism', 'fm')}
admin.site.register(Category, CategoryAdmin)




class MalumotAdmin(admin.ModelAdmin):
    list_display = ('name', 'raqami', 'turi')
    # list_display_links = ('ism', 'fm', 'ifo', 'bulim', 'lavozim', 'is_published')
    # search_fields = ('ifo',)
    # list_editable = ('is_published', )
    # list_filter = ('is_published', 'bulim')
    # prepopulated_fields = {'slug': ('ism', 'fm')}

admin.site.register(Malumot, MalumotAdmin)