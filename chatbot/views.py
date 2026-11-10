from django.shortcuts import render

def home(request):
    return render(request, 'chatbot/home.html')

def about(request):
    return render(request, 'chatbot/about.html')    