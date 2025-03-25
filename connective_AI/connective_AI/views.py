from django.shortcuts import render
from django.contrib import redirects
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .firebaseDB import updateDB, readDB

def home (request):
    if request.method == "POST":
        command = request.POST["command"]
        ID = request.POST["id"]
        passkey = request.POST["passkey"]
        updateDB({
                "command": command,
                "id": ID,
                "passkey": passkey,
                "time_tag": str(datetime.now())
             })
       
    return render(request=request, template_name="home.html")

@csrf_exempt
def getCommand(request):
    if request.method == "GET":
        data = readDB()

        return JsonResponse(data=data)








