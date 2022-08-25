from django.contrib import admin
from .models import Title, Account, Attributes


class TitleAdmin(admin.ModelAdmin):
    fields = ['title_name', 'desc', 'tags', 'tumbnail']
    list_display = ('title_name', 'desc', 'date_added')


class AttributesAdmin(admin.ModelAdmin):
    fields = ['attribute_name']
    list_display = ('attribute_name',)


admin.site.register(Account)
admin.site.register(Title, TitleAdmin)
admin.site.register(Attributes, AttributesAdmin)
