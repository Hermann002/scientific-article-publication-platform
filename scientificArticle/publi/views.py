from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from publi.models import User


from .forms import InfoUser

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_info(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = request.POST
        name = form['userName']
        email = form['userEmail']
        password = form['password']

        user = User(userName=name , userEmail=email , password=password)

        user.save()

        return render(request, "publi/inform.html")
        # check whether it's valid:
    # if a GET (or any other method) we'll create a blank form
    else:
        form =InfoUser()
    context = {"form":form}

    return render(request, "publi/index.html", context)