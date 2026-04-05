from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu

def index(request):
    return render(request, 'index.html')


def menu_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    menus = Menu.objects.all()

    if query:
        menus = menus.filter(name__icontains=query)

    if category:
        menus = menus.filter(category__icontains=category)

    return render(request, 'menu_list.html', {'menus': menus})


def add_menu(request):
    if request.method == 'POST':
        if request.POST.get('password') != PASSWORD:
            return render(request, 'form.html', {'error': 'รหัสผ่านไม่ถูกต้อง'})

        Menu.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            category=request.POST['category'],
            description=request.POST['description']
        )
        return redirect('/menu/')

    return render(request, 'form.html')

def edit_menu(request, id):
    menu = get_object_or_404(Menu, id=id)

    if request.method == 'POST':
        if request.POST.get('password') != PASSWORD:
            return render(request, 'form.html', {'menu': menu, 'error': 'รหัสผ่านไม่ถูกต้อง'})

        menu.name = request.POST['name']
        menu.price = request.POST['price']
        menu.category = request.POST['category']
        menu.description = request.POST['description']
        menu.save()
        return redirect('/menu/')

    return render(request, 'form.html', {'menu': menu})

def delete_menu(request, id):
    menu = get_object_or_404(Menu, id=id)

    if request.method == 'POST':
        if request.POST.get('password') != PASSWORD:
            return render(request, 'confirm_delete.html', {'menu': menu, 'error': 'รหัสผ่านผิด'})

        menu.delete()
        return redirect('/menu/')

    return render(request, 'confirm_delete.html', {'menu': menu})
def about(request):
    return render(request, 'about.html')

PASSWORD = "1234"