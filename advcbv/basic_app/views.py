from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView,UpdateView,
                                DeleteView,)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools' #returns a list named schools
    model = models.School
    #returns a list with the name school_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    #without context_object_name returns school (lowercase)

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    #expects template named school_form.html

class SchoolUpdateView(UpdateView):
    fields = ('name','principal',)
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    #reverse_lazy used since we dont want it evaluated completely when running the .py file
    #waits until actually called as a success
    success_url = reverse_lazy("basic_app:list") #Once view successfully deleted reverses to the 'list' url from apps url.py
