from .models import Property  # Import your models

def custom_context(request):
    #  Count of properties
    property_count = Property.objects.count()

    #  List of property prices
    prices = Property.objects.values_list('price', flat=True)
    prices_list = list(prices)

    #  Any other custom variable you need
    some_variable = 'Hello from the context processor!'
    
    # Return the variables as a dictionary
    return {
        'property_count': property_count,
        'prices_list': prices_list,
        'some_variable': some_variable,
    }
