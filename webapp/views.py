from django.shortcuts import render,redirect
from admin_app.models import CategoryDb,GiftDb
from webapp.models import RegistrationDb,ContactDb

# Create your views here.
def home_page(request):
    gifts = GiftDb.objects.all()
    categories=CategoryDb.objects.all()
    return render(request,"Home.html",{"categories":categories,"gifts":gifts})
def about_page(request):
    gifts = GiftDb.objects.all()
    categories = CategoryDb.objects.all()
    return render(request,"About.html",{"categories":categories,"gifts":gifts})
def contact_page(request):
    gifts = GiftDb.objects.all()
    categories = CategoryDb.objects.all()
    return render(request,"Contact.html",{"categories":categories,"gifts":gifts})
def shop_page(request):
    gifts = GiftDb.objects.all()
    categories = CategoryDb.objects.all()
    return render(request,"Shop.html",{"categories":categories,"gifts":gifts})
def popular_gifts(request):
    categories = CategoryDb.objects.all()
    gifts=GiftDb.objects.all()
    return render(request,"Popular_gifts.html",{"gifts":gifts,"categories":categories})
def filtered_gifts(request,gift_category):
    gifts=GiftDb.objects.filter(Category=gift_category)
    categories = CategoryDb.objects.all()
    return render(request,"Filtered_gifts.html",{"gifts":gifts,"categories":categories})
def single_gift(request,gift_id):
    gift=GiftDb.objects.get(id=gift_id)
    categories = CategoryDb.objects.all()
    return render(request,"Single_gift.html",{"gift":gift,"categories":categories})
def signup_page(request):
    return render(request,"Signup_page.html")
def signin_page(request):
    return render(request,"Signin_page.html")

# user registration or signup
def user_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = RegistrationDb(
            Name=name,
            Phone=phone,
            Email=email,
            Password=password,
            Confirm_password=confirm_password
        )
        if RegistrationDb.objects.filter(Name=name).exists():
            # alert username already exists using js
            return redirect(signup_page)
        elif RegistrationDb.objects.filter(Email=email).exists():
            # alert email already exists using js
            return redirect(signup_page)
        elif password != confirm_password:
            # alert password does not match using js
            return redirect(signup_page)
        else:
            user.save()
            return redirect(signin_page)


def user_login(request):
    if request.method == 'POST':
        un= request.POST.get('username')
        pswd = request.POST.get('password')

        # Check credentials
        user = RegistrationDb.objects.filter(Name=un, Password=pswd).exists()

        if user:
            # Create session
            request.session['Name'] = un
            request.session['Password'] = pswd
            return redirect('home_page')
        else:
            # print("Invalid credentials")
            return redirect('signin_page')
    else:
        return redirect('signin_page')

#delete session
def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(user_login)

#contact view
def save_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        obj=ContactDb(User_name=name,User_email=email,Subject=subject,Message=message)
        obj.save()
        return redirect(contact_page)




