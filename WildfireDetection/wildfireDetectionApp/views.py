import json

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers

from .models import User
from .models import FireTracker
from .forms import UserRegistrationForm


# Create your views here.
def index(request):
    return render(request, 'wildfireDetectionApp/index.html')


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


def markers(request):
    camera_list = FireTracker.objects.all().order_by('id')
    cameras = []
    for cam in camera_list:
        cameras.append({
            'id': cam.camera_id,
            'fire_detected': cam.fire_detected,
            'latitude': float(cam.latitude),
            'longitude': float(cam.longitude)
        })

    json_camera = json.dumps(cameras)
    print(json_camera)

    return JsonResponse({"success": True, 'cameras': json_camera})
