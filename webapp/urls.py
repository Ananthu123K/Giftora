from django.urls import path
from webapp import views

urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('shop_page/',views.shop_page,name="shop_page"),
    path('popular_gifts/',views.popular_gifts,name="popular_gifts"),
    path('filtered_gifts/<gift_category>/',views.filtered_gifts,name="filtered_gifts"),
    path('single_gift/<int:gift_id>/',views.single_gift,name="single_gift"),
    path('signup_page/',views.signup_page,name="signup_page"),
    path('signin_page/',views.signin_page,name="signin_page"),
    path('user_signup/',views.user_signup,name="user_signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),

]