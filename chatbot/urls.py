from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/rag-chatbot/', views.rag_chatbot, name='rag_chatbot'),
    path('services/agent/', views.agent, name='agent'),
    path('services/pdf-generator/', views.pdf_generator, name='pdf_generator'),
    path('services/whatsapp-booking/', views.whatsapp_booking, name='whatsapp_booking'),
]