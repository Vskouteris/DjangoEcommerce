from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('config/', views.stripe_config, name="stripe_config"),
	path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]