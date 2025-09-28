from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def chat_room(request):
    messages = Message.objects.order_by('-timestamp')[:50]
    return render(request, 'chat/room.html', {'messages': reversed(messages)})

def fetch_messages(request):
    messages = Message.objects.order_by('-timestamp')[:50]
    data = [{'user': m.user.username, 'text': m.text} for m in reversed(messages)]
    return JsonResponse(data, safe=False)

def send_message(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        user = request.user
        if text:
            Message.objects.create(user=user, text=text)
    return JsonResponse({'status': 'ok'})
