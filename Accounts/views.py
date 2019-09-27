from django.shortcuts import render , redirect ,  HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/App/hotel_booking/home/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('Invalid login details')
    else:
        auth_form = AuthenticationForm()
        template_name = 'registration/login.html'
        return render(request, template_name,{'form':auth_form})


    
def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

    

def signup_view(request):
    if request.method == 'POST':
        cr_form = UserCreationForm(request.POST)
        if cr_form.is_valid():
            print('Form is Valid :)')
            cr_form.save()
            return redirect('/accounts/login')
        else:
            print('Form is InValid!!')
            cr_form = UserCreationForm()
            template_name = 'registration/Signup.html'
            return render(request, template_name,{'form':cr_form})
    else:
        cr_form = UserCreationForm()
        template_name = 'registration/Signup.html'
        return render(request, template_name,{'form':cr_form})

    
