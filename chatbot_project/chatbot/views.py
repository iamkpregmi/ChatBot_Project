from django.shortcuts import render
from django.http import JsonResponse
from .models import UserQuery
from .chatbot_logic import get_chatbot_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_query = request.POST.get('query')
        response = get_chatbot_response(user_query)
        #Store all chats (Optional)
        UserQuery.objects.create(query=user_query, response=response)
        return JsonResponse({'response': response})
    return render(request, 'chatbot.html')

