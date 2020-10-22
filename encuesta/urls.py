from django.urls import path
from . import views

app_name = 'encuesta'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/resultados/', views.ResultsView.as_view(), name='results'),
    path('pregunta/', views.QuestionFormView.as_view(), name='pregunta_form'),
    path('pregunta/nuevo/', views.nuevaPregunta, name='nueva_pregunta'),
    path('<int:id_pregunta>/voto/', views.nuevoVoto, name='nuevo_voto'),
]
