from django.contrib import admin

from url_app.models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'used')


admin.site.register(Token, TokenAdmin)
