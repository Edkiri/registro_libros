from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Books, Sagas, Genders

# Create your views here.

class HomeView(ListView):
	context_object_name = 'books'

	queryset = Books.objects.filter(favorite='1')

	template_name = 'books/home.html'

class AllBooksView(ListView):
	template_name = 'books/todos.html'
	model = Books
	context_object_name = 'books'


class AllSagasView(ListView):
	template_name = 'books/sagas.html'
	model = Sagas
	context_object_name = 'sagas'

class SagasDetailView(DetailView):
	template_name = "books/detail_saga.html"
	model = Sagas
	context_object_name = 'saga'


class AllGendersView(ListView):
	template_name = "books/genders.html"
	model = Genders
	context_object_name = 'genders'

class GenderDetailView(DetailView):
	template_name = "books/detail_gender.html"
	model = Genders
	context_object_name = 'gender'


