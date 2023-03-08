from django.shortcuts import render, redirect
from .models import Plant, Category
from django.core.paginator import Paginator



# Create your views here.


# INDEX PAGE
def indexPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/index.html', context)

# CONTACT PAGE
def contactPage(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/contact.html', context)

# ERROR PAGE
def error_404(request):
    data = Plant.objects.all()
    categories = Category.objects.all()

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/error.html', context)


# PLANT PAGE
def plantPage(request):
    data = Plant.objects.get_queryset().order_by('id')
    #data = Plant.objects.all()

    items_per_page = 9
    paginator = Paginator(data, items_per_page)

    page_number = request.GET.get('page')

    if not page_number:
        page_number = 1

    page = paginator.get_page(page_number)
    
    categories = Category.objects.all()

    context = {
        "plants" : data,
        "categories" : categories,
        "page": page
    }
    return render(request, 'plants/plants.html', context)

def onePlantDisplayPage(request, iID):
    data = Plant.objects.get(id=iID)
    categories = Category.objects.all()
    #print(data.botanical_name)

    context = {
        "plant" : data,
        "categories" : categories
    }
    return render(request, 'plants/display.html', context)


# CATEGORY PAGES
def categoryPage(request):
    data = Category.objects.all()
    categories = Category.objects.all()

    context = {
        "categories" : data
    }
    return render(request, 'plants/category.html', context)

# Filters all Plants with that specific category
def categoryDisplayPage(request, sName):
    category = Category.objects.get(name=sName)
    categories = Category.objects.all()

    data = Plant.objects.get_queryset().filter(category = category).order_by('id')
    #data = Plant.objects.filter(category = category)

    items_per_page = 9
    paginator = Paginator(data, items_per_page)

    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1

    page = paginator.get_page(page_number)

    context = {
        "plants" : data,
        "category" : category,
        "categories" : categories,
        "page": page
    }
    return render(request, 'plants/plants.html', context)


# Search Pages
def searchPage(request):
    search = (request.GET['search'])
    if search == '':
        return redirect('index')

    page_number = (request.GET.get('page'))
    data = Plant.objects.get_queryset().filter(variety__icontains=search).order_by('variety')
    # data = Plant.objects.filter(variety__icontains=search)

    items_per_page = 9
    paginator = Paginator(data, items_per_page)

   
    if not page_number:
        page_number = 1

    page = paginator.get_page(page_number)

    categories = Category.objects.all()
    context = {
        "plants" : data,
        "categories" : categories,
        "search": search,
        "page": page
    }

    return render(request, 'plants/plants.html', context)
