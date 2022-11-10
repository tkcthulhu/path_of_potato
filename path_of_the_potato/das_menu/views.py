from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.forms.models import model_to_dict
# Create your views here.
def get_full_menu(request):

    full_menu = MenuItem.objects.filter(stock=True)

    JSON_data = list()

    for item in full_menu:

        JSON_data.append({
            'title': item.title,
            'price': item.price,
            'description': item.description,
            'spicy_level': item.spicy_level,
            'category': model_to_dict(Category.objects.get(id=item.category_id), fields=['title']),
            'cuisine': model_to_dict(Cuisine.objects.get(id=item.cuisine_id))  
            })

    return JsonResponse(JSON_data, safe=False)