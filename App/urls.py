from django.urls import path
from App import views

urlpatterns=[
    path('',views.index, name = 'index'),
    path('1/', views.index1, name = '404'),
    path('2/', views.index2, name = 'cart'),
    path('3/', views.index3, name = 'checkout'),
    path('4/', views.index4, name = 'contact'),
    path('5/', views.index5, name = 'shop-detail'),
    path('6/', views.index6, name = 'shop'),
    path('7/', views.index7, name = 'testimonial'),
]