from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_list_or_404, redirect
from django.core.paginator import Paginator

class BlogView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'pages/index.html', context)