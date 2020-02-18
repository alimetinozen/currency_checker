from django.contrib import admin
from django import forms
from .models import Provider


class ProviderAdminForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderAdmin(admin.ModelAdmin):
    form = ProviderAdminForm
    list_display = ['name', 'url', 'created', 'last_updated']
    readonly_fields = ['created', 'last_updated']


admin.site.register(Provider, ProviderAdmin)
