from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request):
    if request.method == "POST":
        text = request.POST.get("message")
        if text:
            Message.objects.create(user=request.user, text=text)
        return redirect('chat_room')
    
    messages = Message.objects.all().order_by('timestamp')
    return render(request, "chat/chat_room.html", {"messages": messages})
