from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def signup_contr(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_contr(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           
            return redirect('login:signup')
    else:
    	form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
    
    
    
	