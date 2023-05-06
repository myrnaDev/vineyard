from django.shortcuts import render, redirect
from wine_database.models import Wine

# Create your views here.

def index(request):
    wine_list = Wine.objects.all()
    context = {"wine_list": wine_list}
    return render(request, 'index.html', context)

def add_wine(request):
    if request.method == 'POST':
        id = request.POST.get('wine_id')
        wine_name = request.POST.get('wine_name')
        wine_variety = request.POST.get('wine_variety')
        wine_type = request.POST.get('wine_type')
        wine_region = request.POST.get('wine_region')
        wine_stock = request.POST.get('wine_stock')

        new_wine = Wine(id=id, wine_name=wine_name, wine_variety=wine_variety, wine_type=wine_type, wine_region=wine_region, wine_stock=wine_stock)
        new_wine.save()

    return redirect('index')

def remove_wine(request):
    if request.method == 'POST':
        id = request.POST.get('wine_id')

        if id is not None:
            Wine.objects.filter(id=id).delete()

    return redirect('index')
