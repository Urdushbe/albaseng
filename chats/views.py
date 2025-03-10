import time
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import ChatMessage
from .forms import ChatForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ChatView(LoginRequiredMixin, View):
    template_name = 'chat.html'

    def get(self, request):
        chat_messages = ChatMessage.objects.all().order_by('-timestamp')[:50]

        last_message_time = request.session.get('last_message_time')
        current_time = time.time()

        if last_message_time is None or current_time - last_message_time > 2:
            can_post = True
        else:
            can_post = False

        chat_form = ChatForm()

        context = {
            'chat_messages': chat_messages,
            'chat_form': chat_form,
            'can_post': can_post,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        chat_messages = ChatMessage.objects.all().order_by('-timestamp')[:50]

        last_message_time = request.session.get('last_message_time')
        current_time = time.time()

        if last_message_time is None or current_time - last_message_time > 1:
            can_post = True
        else:
            can_post = False

        chat_form = ChatForm(request.POST)

        if can_post and chat_form.is_valid():
            new_message = chat_form.save(commit=False)
            user_id = request.user.id
            last_message = get_last_message(user_id)

            if last_message is None or last_message.message != new_message.message:
                new_message.user = request.user
                new_message.save()
                chat_form = ChatForm()  # To clear the form after submission
                request.session['last_message_time'] = current_time

        context = {
            'chat_messages': chat_messages,
            'chat_form': chat_form,
            'can_post': can_post,
        }
        return render(request, self.template_name, context)

def get_last_message(user_id):
    try:
        return ChatMessage.objects.filter(user_id=user_id).latest('timestamp')
    except ChatMessage.DoesNotExist:
        return None



class ChatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ChatMessage
    template_name = 'chat_delete.html'
    success_url = reverse_lazy('chat')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser

class ChatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ChatMessage
    template_name = 'chat_edit.html'
    fields = ('message',)
    success_url = reverse_lazy('chat')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser