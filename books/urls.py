from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import AllBooksView, AllSagasView, SagasDetailView,	AllGendersView, \
					GenderDetailView


urlpatterns = [
	path('todos/', AllBooksView.as_view()),
	path('sagas/', AllSagasView.as_view(), name='sagas'),
	path('sagas/<slug:slug>/', SagasDetailView.as_view(), name='detail-saga'),
	path('genders/', AllGendersView.as_view(), name='genders'),
	path('genders/<slug:slug>/', GenderDetailView.as_view(), name='detail-gender'),
]

