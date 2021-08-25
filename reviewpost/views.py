from django.shortcuts import render

# Create your views here.

def signupview(request):
    writelog('signup function is called')
    return render(request, 'signup.html', {'somedata':100})

def writelog(text):
    print(text)