from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Interest

# Create your views here.
def index(request):
    return render(request, 'interest/index.html')

def people(request):
    users = User.objects.all()
    return render(request, 'interest/userlist.html',{'users':users} )

def process(request):
    if request.method != "POST":
        return redirect('/')
    user_check = User.objects.validate(request.POST)
    interest_check = Interest.objects.validate(request.POST)
    if user_check[0] == True and interest_check[0] == True:
        # user_check[1].interests.add(interest_check[1])
        interest_check[1].users.add(user_check[1])
    if user_check[0] == False:
        messages.info(request, user_check[1])
    if interest_check[0] == False:
        messages.info(request, interest_check[1])
    return redirect('/')


def show(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        messages.info(request, "User not found!")
        return redirect('/people')
    return render(request, 'interest/interests.html', {"user":user})

def delete(request, id):
    try:
        user = User.objects.get(id=id)
        name = user.name
        user.delete()
        messages.info(request, "User {} deleted!".format(name))
    except User.DoesNotExist:
        messages.info(request, "User not found!")
        return redirect('/people')
    return redirect('/people')
