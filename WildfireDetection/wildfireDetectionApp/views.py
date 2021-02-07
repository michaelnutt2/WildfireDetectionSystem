import json

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers

from .models import User
from .models import FireTracker
from .forms import UserRegistrationForm
from keras.applications.inception_v3 import preprocess_input as inception_preprocess_input
import threading
from machine_learning import launcher
import tensorflow as tf
from keras.models import load_model
model = None
graph = None
num = None
# Create your views here.
def index(request):
    
    global model
    global graph
    global num
    model =  load_model("machine_learning/model-saves/Inception_based/best_trained_save.h5")
    graph = tf.get_default_graph()
    num = 0
    #model = launcher.loadModelFile()
	
    return render(request, 'wildfireDetectionApp/index.html')

def predict(request):
    if request.method == 'POST':
        print("post")
        return render(request, 'wildfireDetectionApp/confirmation.html')

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

def updateFireTracker(id, status):
    print("updating Fire Tracker " + id)
    camera_list = FireTracker.objects.all().order_by('id')
    fireTracker =  camera_list[int(id)]
    fireTracker.fire_detected = status
    fireTracker.save()
    

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
def frames(request):
    global num
    videoUrl = request.GET['video']
    id = request.GET['id']
    print(videoUrl)
    print("start")
    #video = "/Users/Araib/Desktop/New Folder With Items/Projects/Masters/Projects/ai_softwaredev/wildfire_detection/wildfiredetection/WildfireDetectionSystem/WildfireDetection/wildfireDetectionApp/static/video.mp4"
    num += 1
    data = launcher.videofiredetection(model,graph,num, videoUrl, inception_preprocess_input, 12)
    if data == "no_fire":
        updateFireTracker(id, False)
        return JsonResponse({"success": True, "data": data, "id": id, "fire": False})

    else:
        updateFireTracker(id, True)
        return JsonResponse({"success": True, "data": data, "id": id, "fire": True})

    
def multipleVideos(model, name):
    base =  "/Users/Araib/Desktop/New Folder With Items/Projects/Masters/Projects/ai_softwaredev/wildfire_detection/wildfiredetection/WildfireDetectionSystem/WildfireDetection/wildfireDetectionApp/static/"
    videoUrl = base + name     
    print("starting file: " + name)            
    launcher.videofiredetection(model, videoUrl, inception_preprocess_input, 12)
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1     



