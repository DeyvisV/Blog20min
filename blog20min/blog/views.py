from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Entry


class IndexView(ListView):

	template_name = 'index.html'
	model = Entry


class EntryDetailView(DetailView):

	template_name = 'entry_detail.html'
	model = Entry