from django.shortcuts import render
from .models import Property
import json

# Create your views here.

def home(request):
    return render(request, 'home2.html')

def property_distribution(request):
    prices = Property.objects.values_list('price', flat=True)
    prices_list = list(prices)
    prices_json = json.dumps(prices_list)
    return render(request, 'analysis.html', {'prices_json': prices_json})


def list(request):
    return render(request, 'list.html')

# def analysis(request):
#     properties = Property.objects.all()
#     context = {'properties': properties}
#     return render(request, 'analysis.html', context)

# def data(request):
#     properties = Property.objects.values('name', 'price')
#     return JsonResponse(list(properties), safe=False)

# class AnalyticsPageView(View):
#     def get(self, request):
#         return render(request, 'index.html')

# class PropertiesPageView(View):
#     def get(self, request):
#         return render(request, 'index.html')

# class AnalysisPageView(View):
#     def get(self, request):
#         return render(request, 'index.html')
