from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupview(request):
    writelog('signup function is called')
    
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = User.objects.create_user(username_data, '', password_data)
    else:
        writelog(User.objects.all())
        return render(request, 'signup.html', {})
    return render(request, 'signup.html')

def writelog(text):
    print(text)