from django.shortcuts import render
from .models import Property
import json

# views.py
from django.shortcuts import render
import json

# views.py
from django.shortcuts import render
import json

# views.py
from django.shortcuts import render
import json

def dashboard(request):
    with open('data.json', 'r') as file:
        data = json.load(file)
    bhk= [1,2,3,4,5,'5+']
    bathroom = [1,2,3,4,'5+']
    bhk_json= json.dumps(bhk)
    bathroom_json = json.dumps(bathroom)
    return render(request, 'analysis.html', {'bhk': bhk_json},{'bathroom',bathroom_json})


    return render(request, 'home2.html', {'data': data})

def home(request):
    return render(request, 'home2.html')
 
    return render(request, 'your_template.html', {'data': data})


def property_distribution(request):
    with open('data.json') as f:
        property_listings = json.load(f)
    # property_prices = [property['price'] for property in property_listings]
    property_prices = [2000000, 3000000, 2500000, 4000000, 3500000, 5000000, 6000000, 7000000, 8000000]
    property_prices_json = json.dumps(property_prices)
    return render(request, 'analysis.html', {'property_prices': property_prices_json})

def list(request):
    with open('data.json') as f:
        data = json.load(f)
        property_count = len(data)
    return render(request, 'list.html', {'data': data,'property_count': property_count})

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


