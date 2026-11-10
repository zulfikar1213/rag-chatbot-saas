from django.shortcuts import render

def home(request):
    return render(request, 'chatbot/home.html')

def about(request):
    return render(request, 'chatbot/about.html') 

def rag_chatbot(request):
    return render(request, 'chatbot/rag_chatbot.html')

def agent(request):
    return render(request, 'chatbot/agent.html')

def pdf_generator(request):
    return render(request, 'chatbot/pdf_generator.html')

def whatsapp_booking(request):
    return render(request, 'chatbot/whatsapp_booking.html')