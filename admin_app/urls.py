from django.urls import path
from admin_app import views

urlpatterns = [
    path('Home/',views.index_page,name="Home"),
    path('add_category/',views.add_category,name="add_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('edit_category/<int:category_id>',views.edit_category,name="edit_category"),
    path('update_category/<int:cat_id>',views.update_category,name="update_category"),
    path('delete_category/<int:cat_id>',views.delete_category,name="delete_category"),
    path('add_gift/',views.add_gift,name="add_gift"),
    path('display_gift/',views.display_gift,name="display_gift"),
    path('save_gift/',views.save_gift,name="save_gift"),
    path('edit_gift/<int:gift_id>/',views.edit_gift,name="edit_gift"),
    path('update_gift/<int:gift_id>/',views.update_gift,name="update_gift"),
    path('delete_gift/<int:g_id>/',views.delete_gift,name="delete_gift"),
    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('display_message/',views.display_message,name="display_message"),
    path('delete_message/<int:m_id>',views.delete_message,name="delete_message"),
    ]