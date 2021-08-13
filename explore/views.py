from explore.forms import search
from django.shortcuts import render
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.
class SearchView(ListView):
    model = User
    template_name = 'explore/index.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = User.objects.filter(username__contains=query)
          result = postresult
       else:
           result = None
       return result