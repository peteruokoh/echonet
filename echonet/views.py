from django.shortcuts import render, redirect
from blog.models import Post
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_posts') 
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def homepage(request):
    return render(request, "homepage.html") #To display HTML, use render instead of HttpResponse

def register_user(request):
    if (request.method == "POST"):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user) # login user automatically after registration
            return redirect("list_posts")
    else:
        # for GET request
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})