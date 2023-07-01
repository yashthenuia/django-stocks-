from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name="home"), #path would be empty beacuse we want our home page to open directly

	path('about.html',views.about, name="about"),

	path('add_stock.html',views.add_stock, name="add_stock"),
	path('delete/<stock_id>',views.delete , name="delete"),
	
]
