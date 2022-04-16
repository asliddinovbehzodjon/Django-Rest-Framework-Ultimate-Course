from django.shortcuts import render
from .models import Maqola
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    data = Maqola.objects.values()
    return JsonResponse({'data':list(data)},safe=False)
# JSON - JavaScript Object Notion