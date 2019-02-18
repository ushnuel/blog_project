from django.shortcuts import render
from django.views.generic import TemplateView
from drycleaningApp.forms import MessageForm
from .models import Message
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# Create your views here.
def home(request):
    form = MessageForm()
    return render(request, 'dryApp/home.html', { 'form':form })

def about_us(request):
    return render(request, 'dryApp/about_us.html')

def billing_policy(request):
    return render(request, 'dryApp/billing_policy.html')

def terms_agreement(request):
    return render(request, 'dryApp/terms_agreement.html')

def my_messages(request):

        if request.method == 'POST':

            form = MessageForm(request.POST)

            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.POST.get('author')
                message.text = request.POST.get('text')
                message.phone = request.POST.get('phone')
                message.location = request.POST.get('location')
                message.plan_type = request.POST.get('plan_type')

                message.save()

                messages.success(request, 'Message recieved, we will get back to you as soon as possible')
                return redirect('home')

            else:
                messages.error(request, 'Invalid form, please fill the necessary fields')
                return redirect('home')

        else:
            form = MessageForm()
        return render(request, 'dryApp/home.html', {'form': form})
