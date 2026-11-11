from django.shortcuts import render
from .groq_client import ask_groq

def home(request):
    return render(request, 'chatbot/home.html')

def about(request):
    return render(request, 'chatbot/about.html') 

def rag_chatbot(request):
    answer = None
    question = None
    if request.method == "POST":
        question = request.POST.get("question")
        if question:
            answer = ask_groq(question)
    return render(request, 'chatbot/rag_chatbot.html', {
        'question': question,
        'answer': answer,
    })

def agent(request):
    return render(request, 'chatbot/agent.html')

def pdf_generator(request):
    return render(request, 'chatbot/pdf_generator.html')

def whatsapp_booking(request):
    return render(request, 'chatbot/whatsapp_booking.html')