import datetime
from django.shortcuts import render,redirect
from admin_app.models import CategoryDb,GiftDb
from webapp.models import ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index_page(request):
    categories = CategoryDb.objects.count()
    gifts=GiftDb.objects.count()
    date = datetime.datetime.now()
    return render(request,"index.html", {"categories": categories,"gifts":gifts,"date":date})

def add_category(request):
    return render(request,"Add_category.html")
def display_category(request):
    categories=CategoryDb.objects.all()
    return render(request,"Display_category.html",{"categories":categories})
def save_category(request):
    if request.method=="POST":
        category_name=request.POST.get('Category_name')
        description=request.POST.get('Description')
        cover_image=request.FILES['Cover_Image']

        obj=CategoryDb(
            Category_name=category_name,
            Description=description,
            Cover_Image=cover_image

        )
        obj.save()
        return redirect(add_category)
def edit_category(request,category_id):
    category=CategoryDb.objects.get(id=category_id)
    return render(request,"Edit_category.html",{"category":category})



def update_category(request,cat_id):
    if request.method=="POST":
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')

        try:
            img=request.FILES['Cover_Image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=cat_id).Cover_Image
        CategoryDb.objects.filter(id=cat_id).update(
            Category_name=category_name,
            Description=description,
            Cover_Image=file

        )
        return redirect(display_category)

def delete_category(request, cat_id):
    category = CategoryDb.objects.filter(id=cat_id)
    category.delete()
    return redirect(display_category)

#Gift views

def add_gift(request):
    categories = CategoryDb.objects.all()
    return render(request,"Add_gift.html",{"categories":categories})

def display_gift(request):
    gifts=GiftDb.objects.all()
    return render(request,"Display_gift.html",{"gifts":gifts})

def save_gift(request):
    if request.method=="POST":
        gift_name=request.POST.get('gift_name')
        category=request.POST.get('category')
        price=request.POST.get('price')
        stock=request.POST.get('stock')
        brand=request.POST.get('brand')
        description=request.POST.get('description')
        gift_image=request.FILES['gift_image']

        obj=GiftDb(
            Gift_name=gift_name,
            Category=category,
            Price=price,
            Stock=stock,
            Brand=brand,
            Description=description,
            Gift_image=gift_image

        )
        obj.save()
        return redirect(add_gift)

def edit_gift(request,gift_id):
    gifts=GiftDb.objects.get(id=gift_id)
    categories = CategoryDb.objects.all()
    return render(request,"Edit_gift.html",{"gifts":gifts,"categories":categories})


def update_gift(request, gift_id):
    if request.method == "POST":
        gift_name = request.POST.get('gift_name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        brand = request.POST.get('brand')
        description = request.POST.get('description')

        try:
            img = request.FILES['gift_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = GiftDb.objects.get(id=gift_id).Gift_image

        GiftDb.objects.filter(id=gift_id).update(
            Gift_name=gift_name,
            Category=category,
            Price=price,
            Stock=stock,
            Brand=brand,
            Description=description,
            Gift_image=file
        )

        return redirect(display_gift)

def delete_gift(request,g_id):
    data=GiftDb.objects.filter(id=g_id)
    data.delete()
    return redirect(display_gift)

def admin_login_page(request):
    return render(request,"Admin_login.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data=authenticate(username=un,password=pswd)
            if data is not None:
                login(request,data)
                request.session['username']=un
                request.session['password']=pswd
                return redirect(index_page)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

#message view

def display_message(request):
    messages=ContactDb.objects.all()
    return render(request,"Display_message.html",{"messages":messages})


def delete_message(request,m_id):
    data=ContactDb.objects.filter(id=m_id)
    data.delete()
    return redirect(display_message)



