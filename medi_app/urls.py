from django.urls import path,include
from.import views,user_views,owner_views

urlpatterns = [
    path ("",views.home,name="home"),
    path ("about/",views.about_us,name="about us"),
    path ("contact/",views.contact_us,name="contact us"),
    path("login/",user_views.login_form,name="login form"),
    path("reg/",user_views.reg_form,name="reg form"),
    path("user_feedback/",user_views.user_feedback,name="feedback form"),
    path("user_home/",user_views.user_home,name="user_home"),

    path("owner_home/",owner_views.owner_home,name="home page"),
    path("owner_login/",owner_views.owner_login,name="owner_login_form"),
    path("owner_registration/",owner_views.owner_reg,name="owner_registration_form"),
    path("user_logout/",user_views.user_logout,name='user_logout'),
    path("owner_logout/",owner_views.owner_logout,name='owner_logout'),
    path("all_feedback/",views.all_feedback,name='all feedback'),
    path("shop_detail/", owner_views.shop_detail,name='shop_detail'),
    path("view_shopkeeper/", owner_views.view_shopkeeper,name='view_shopkeeper'),
    path("map_location/", owner_views.map_location,name='map_location'),
    path("view_map/",user_views.view_map,name='view_map'),
     path("medicine_request/",user_views.medicine_request,name="medicine_request"),
     path("view_medicine_request/",owner_views.view_medicine_request,name=" view_medicine_request"),
     path("update_medicine/",user_views.update_medicine,name="update_medicine"),
     path("update_status/<int:id>",user_views.update_status,name="update_status"),
     path("owner_edit_profile/",owner_views.owner_edit_profile,name="owner_edit_profile"),
     path("user_edit_profile/",user_views.user_edit_profile,name="user_edit_profile")


   
]