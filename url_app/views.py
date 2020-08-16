import secrets

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from url_app import models


def make_token():
    return secrets.token_urlsafe(10)


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        token = make_token()
        data = request.GET
        models.Token.objects.create(token=token, data=data)
        return redirect(reverse('index', args=(token,)))


class URLView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        obj = models.Token.objects.get(token=token)
        if not obj.used:
            return render(request, 'index.html', {'data': obj.data, 'token': token})
        else:
            return render(request, '404.html')

    def post(self, request, *args, **kwargs):
        token = kwargs.get('token')
        obj = models.Token.objects.get(token=token)
        obj.used = True
        obj.save()
        return render(request, '404.html')