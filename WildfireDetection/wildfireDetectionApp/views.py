from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.core import serializers

from .models import User
from .models import FireTracker
from .forms import UserRegistrationForm


# Create your views here.
def index(request):
    #cameras = serializers.serialize("json",FireTracker.objects.all().order_by('id'))
    return render(request, 'wildfireDetectionApp/index.html', {'cameras' : cameras})


def user_registration(request):
    # If this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegistrationForm(request.POST)
        # Check whether it is valid
        if form.is_valid():
            # clean the data:
            user = form.save()
            return render(request, 'wildfireDetectionApp/confirmation.html')
    else:
        form_class = UserRegistrationForm

    return render(request, 'wildfireDetectionApp/registration.html', {
        'form': form_class,
    })


def confirmation(request):
    return render(request, 'wildfireDetectionApp/confirmation.html')