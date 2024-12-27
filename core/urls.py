from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('product/<int:pk>', views.product, name='product'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary', views.category_summary, name='category_summary'),
    path('search/', views.search_products, name='search'),
    # path('cart', views.cart, name)
]