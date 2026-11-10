from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/rag-chatbot/', views.rag_chatbot, name='rag_chatbot'),

]