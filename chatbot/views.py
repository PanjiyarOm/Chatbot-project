from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
import nltk
from django.http import JsonResponse
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('wordnet')


greetFaqs = [
    [r"hi|hello|hey|hlo", ["Hello! How can I help you?"]],
    [r"how are you?", ["I'm doing great, thank you! How about you?"]],
    [r"what is your name|what is your name?|who are you|who are you?", ["I'm a simple chatbot created to assist you."]],
    [r"(.*) help|help (.*)|help", ["Sure! How can I assist you?"]],
    [r"bye|goodbye", ["Goodbye! Have a great day!"]],
    [r"(.*) Django|Django (.*)|Django", ["Django is a high-level Python web framework."]],
    [r"(.*) python|python (.*)|python", ["Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected."]],
    [r"(.*) Danson Solutions|Danson Solutions (.*)|Danson Solutions", ["Danson Solutions is an innovative IT and marketing firm dedicated to delivering cutting-edge solutions and creative content. We are passionate about leveraging technology to drive business growth and enhance customer experiences."]],
    [r"(.*) AI|AI (.*)|(.*) Artificial Intelligence|Artificial Intelligence (.*)|Artificial Intelligence", ["Artificial intelligence (AI) is technology that enables computers and machines to simulate human learning, comprehension, problem solving, decision making, creativity and autonomy."]],
]


nltk_chatbot = Chat(greetFaqs, reflections)

'''FAQS = {
    'What is Django?': 'Django is a high-level Python web framework.',
    'How to use Django?': 'You can start by creating a project and defining models, views, and templates.',
    'What is NLTK?': 'NLTK stands for Natural Language Toolkit. It is a library for NLP in Python.'
}'''


def chat(request):
    user_input = request.GET.get('prompt', '')

    
    chatbot_response = nltk_chatbot.respond(user_input)
    if chatbot_response:
        return JsonResponse({'response': chatbot_response})

    '''for question, answer in FAQS.items():
        if question.lower() in user_input.lower():
            return JsonResponse({'response': answer})'''

    return JsonResponse({'response': "Sorry, I didn't understand that. Can you please rephrase?"})

def chatbot_page(request):
    return render(request, 'chatbot/chatbot.html')
