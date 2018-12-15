from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from models import balance
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            instance = balance(user = request.user, balance = 0)
            instance.save()
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    msg=""
    if request.method == "POST":
        try:
            username = request.POST["username"]
            amount = request.POST["amount"]
            senderUser = User.objects.get(username=request.user.username)
            receiverrUser =  User.objects.get(username=username)
            sender = balance.objects.get(user = senderUser)
            receiverr = balance.objects.get(user = receiverrUser)
            sender.balance = sender.balance - int(amount)
            receiverr.balance = receiverr.balance + int(amount)
            sender.save()
            receiverr.save()
            msg = "Transaction Success"
        except Exception as e:
            print(e)
            msg = "Transaction Failure, Please check and try again"
    user = balance.objects.get(user=request.user)
    return render(request,'profile.html',{"balance":user.balance,"msg":msg})