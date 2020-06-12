from django.urls import path,include
from . import views
urlpatterns = \
    [
    path('register',views.Register,name="User Register"),
    path('login',views.Login,name="User Login"),
    path('Forgotpassword',views.Forgotpassword,name="User Forgotpassword"),
    path('Allplans',views.Allplans,name=" Allplans"),
    path('Allcats',views.All_Intrest_Category,name=" All Cats"),
    path('Allsubcats',views.All_Intrest_Sub_Category,name=" All Sub Cats"),
    path('Setuserplan',views.Setuserplan,name=" Set user plan"),

    ]