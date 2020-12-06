from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import chat
from .serializers import ChatModelSerializer
from django.views.decorators.csrf import csrf_exempt

def index(request):

    return HttpResponse("Hello Chat API")

@csrf_exempt
def chat_view(request):
    if request.method == "GET":
        masseges = chat.objects.all()
        serializer = ChatModelSerializer(masseges, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ChatModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
