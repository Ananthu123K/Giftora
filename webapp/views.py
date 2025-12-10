from django.shortcuts import render,redirect
from admin_app.models import CategoryDb,GiftDb
from webapp.models import RegistrationDb,ContactDb,CartDb,OrderDb

# Create your views here.
def home_page(request):
    gifts = GiftDb.objects.all()
    categories=CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
    return render(request,"Home.html",{"categories":categories,"gifts":gifts,"cart_total":cart_total})
def about_page(request):
    gifts = GiftDb.objects.all()
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
    return render(request,"About.html",{"categories":categories,"gifts":gifts,"cart_total":cart_total})
def contact_page(request):
    gifts = GiftDb.objects.all()
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
    return render(request,"Contact.html",{"categories":categories,"gifts":gifts,"cart_total":cart_total})
def shop_page(request):
    gifts = GiftDb.objects.all()
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
    return render(request,"Shop.html",{"categories":categories,"gifts":gifts,"cart_total":cart_total})
def popular_gifts(request):
    categories = CategoryDb.objects.all()
    gifts=GiftDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
    return render(request,"Popular_gifts.html",{"gifts":gifts,"categories":categories,"cart_total":cart_total})
def filtered_gifts(request,gift_category):
    gifts=GiftDb.objects.filter(Category=gift_category)
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
    return render(request,"Filtered_gifts.html",{"gifts":gifts,"categories":categories,"cart_total":cart_total})
def single_gift(request,gift_id):
    gift=GiftDb.objects.get(id=gift_id)
    categories = CategoryDb.objects.all()
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
    return render(request,"Single_gift.html",{"gift":gift,"categories":categories,"cart_total":cart_total})
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

def cart_page(request):
    categories = CategoryDb.objects.all()
    gifts = CartDb.objects.filter(Username=request.session['Name'])
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()

        # calculating total amount
    sub_total = 0
    delivery_charge = 0
    total_amount = 0
    for i in gifts:
        sub_total += i.TotalPrice
        if sub_total > 500:
            delivery_charge = 50
        else:
            delivery_charge = 100
        total_amount = sub_total + delivery_charge
    return render(request,"Cart.html",{"categories":categories,"gifts":gifts,"cart_total":cart_total,'sub_total':sub_total,'delivery_charge':delivery_charge,'total_amount':total_amount})


def checkout_page(request):
    categories = CategoryDb.objects.all()
    gifts = CartDb.objects.filter(Username=request.session['Name'])
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
     # calculating total amount
    sub_total = 0
    delivery_charge = 0
    total_amount = 0
    for i in gifts:
        sub_total += i.TotalPrice
        if sub_total > 500:
            delivery_charge = 50
        else:
            delivery_charge = 100
        total_amount = sub_total + delivery_charge

    return render(request,"Checkout.html",{"categories":categories,"gifts":gifts,"cart_total":cart_total,'sub_total':sub_total,'delivery_charge':delivery_charge,'total_amount':total_amount})



def save_to_cart(request):
    if request.method=="POST":
        gift_name=request.POST.get('gift_name')
        quantity=int(request.POST.get('quantity'))
        price=float(request.POST.get('price'))
        total_price=float(request.POST.get('totalprice'))
        username = request.POST.get('username')
        gift=GiftDb.objects.filter(Gift_name=gift_name).first()
        img=gift.Gift_image if gift else None
        obj=CartDb(
            Username=username,
            Giftname=gift_name,
            Quantity=quantity,
            Price=price,
            TotalPrice=total_price,
            Gift_Image=img
        )
        obj.save()
        return redirect('home_page')

def delete_item(request,g_id):
    data=CartDb.objects.filter(id=g_id)
    data.delete()
    return redirect('cart_page')


def save_order(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        mobile= request.POST.get('mobile')
        totalprice = request.POST.get('totalprice')

        # Basic validation
        if not all([first_name, last_name, email, address, state, city, pincode, mobile]):
            # messages.warning(request, "Please fill all required fields.")
            return redirect('checkout_page')

        # Save order to DB
        obj=OrderDb(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            mobile=mobile,
            TotalPrice=totalprice
        )

        obj.save()

        # messages.success(request, "Order placed successfully!")


        return redirect('payment_page')

def payment_page(request):
    category = CategoryDb.objects.all()
    books = CartDb.objects.filter(Username=request.session['Name'])
    cart_total = 0
    uname = request.session.get('Name')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()

    # adding details for payment
    # retrieve the data from the OrderDb with specified id
    customer =OrderDb.objects.order_by('-id').first()
    # Get the amount of the specified customer
    payy = customer.TotalPrice
    amount = int(payy * 100)
    pay_str = str(amount)
    return render(request,"Payment_page.html",{'category':category,'books':books,'cart_total':cart_total})





