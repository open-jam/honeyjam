from django.shortcuts import render
from django.views import View

from apps.domains.gag.repositories import GagRepository


class GagListView(View):
    @staticmethod
    def get(request):
        offset = 0
        limit = 100
        gags = GagRepository.find_active(offset, limit)
        return render(request, 'www/gag/index.html', {'gags': gags})
