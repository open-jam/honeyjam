from django.shortcuts import render
from django.views import View


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'www/home/index.html', {})
