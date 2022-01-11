from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LaptopsModel
from .serializers import LaptopSerializer

# Create your views here.
@csrf_exempt
def LaptopsView(request):
    if request.method == 'GET':
            laptops = LaptopsModel.objects.all()
            serializer = LaptopSerializer(laptops, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LaptopSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def GetLaptop_View(request, pk):
    try:
        laptop = LaptopsModel.objects.get(id=pk)
    except LaptopsModel.DoesNotExist:
        raise Http404('Not Found')

    if request.method == 'GET':
        serializer = LaptopSerializer(laptop)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LaptopSerializer(laptop, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    if request.method == 'DELETE':
        laptop.delete()
        return HttpResponse(status=204)

