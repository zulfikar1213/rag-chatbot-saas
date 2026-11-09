from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Doha Tech Solutions - RAG Chatbot SaaS</h1><p>Coming soon! We build AI chatbots for restaurants, clinics and hotels in Qatar and Iraq.</p>")