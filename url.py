from django.urls import path 
from . import views


urlpatterns = [    
    path('', views.home , name='home'),    
    path('signup/', views.signup , name='signup'),    
    path('items/', views.items , name='items'),    
    path('login/', views.login , name='login'),    
    path('logout/', views.logout , name='logout'),    
    path('details/<int:pk>', views.details , name='details'),    
    path('category/<str:pk>', views.category , name='category'), 
    # cart
    path('cart_summary' , views.cart_summary , name="cart_summary") ,  
    path('add/' , views.cart_add , name="cart_add") ,  
    path('delete/' , views.cart_delete , name="cart_delete") ,  
    path('update/' , views.cart_update , name="cart_update") ,  
]