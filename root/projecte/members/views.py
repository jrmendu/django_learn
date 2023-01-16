from django.http import HttpResponse
from django.template import loader
from .models import Member
	
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details_members.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    members = Member.objects.all().values()
    variable = "Estoy en el context"
    cars = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "doors": 3,
        "year": "1950",
    },
    {
        "brand": "Ford",
        "model": "Sierra",
        "doors": 5,
        "year": "1960",
    },
    {
        "brand": "Ford",
        "model": "Bronco",
        "doors": 5,
        "year": "1960",
    },
    {
        "brand": "Volvo",
        "model": "XC90",
        "doors": 5,
        "year": "1960",
    },
    {
        "brand": "Volvo",
        "model": "P1800",
        "doors": 2,
        "year": "1990",
    }]
    sorted_cars = sorted(cars, key=lambda x:x['year'])
    context = {
        'members': members,
        'animals': ['Dog', 'Cat', 'Horse', 'Bird'],
        'variable': variable,
        'heading_no_esc' : "<h1>Heading1</h1>",
        'heading_esc' : "&lt;h1&gt;Heading1&lt;/h1&gt;",
        'lista_num': [1,2,3,4,5,6,7,8,9,10], 
        'lista_num2': [1,2,3,4,5,5,6,6,7,8,9,10],
        'cars' : [
    {
        "brand": "Ford",
        "model": "Mustang",
        "doors": 3,
        "year": "1950",
    },
    {
        "brand": "Ford",
        "model": "Sierra",
        "doors": 5,
        "year": "1960",
    },
    {
        "brand": "Ford",
        "model": "Bronco",
        "doors": 5,
        "year": "1960",
    },
    {
        "brand": "Volvo",
        "model": "XC90",
        "doors": 5,
        "year": "1960",
    },
    {
        "brand": "Volvo",
        "model": "P1800",
        "doors": 2,
        "year": "1990",
    }],
    'sorted_cars' : sorted_cars,
        }
    return HttpResponse(template.render(context, request))

