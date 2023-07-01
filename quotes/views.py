from django.shortcuts import render, redirect

# Create your views here.
import yfinance as yf

from .models import Stock

from .forms import StockForm

from django.contrib import messages

def home(request): # this is browser request means someone is requesting our page so we return new web page 

	import requests
	import json 

	if request.method == "POST":
		ticker = request.POST['ticker']         #this is ticker we will put in the search box 

		stockre = yf.Ticker(ticker).info


		yash_request = stockre

		if yash_request == None:
			yash_request= "Error..."

				# try:
		# 	api = yash_request
		# except Exception as e:
		# 	api = "Error..."


		return render(request, 'home.html', {'api': yash_request})

	else:
		return render(request, 'home.html', {'ticker': "enter a ticker symbol above..."})


	# url = "https://yh-finance-complete.p.rapidapi.com/yhprice"

	# querystring = {"ticker":"TSLA"}

	# headers = {
	# 	"X-RapidAPI-Key": "252efd75e6mshfa585dd560bae49p1ffb75jsnc1e6fcd5c06d",
	# 	"X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
	# }
	


    # API pk_ba588fd1b9e847d9823e381fa717db7d
	

def about(request):
	return render(request, 'about.html',{})



def add_stock(request):
	import requests

	if request.method == "POST":
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('add_stock')
		else:
			ticker = Stock.objects.all()
			return render(request, 'add_stock.html', {'ticker': ticker})


	else:
		ticker = Stock.objects.all()
		outputs =[]
		for ticker_item in ticker:
			stockre = yf.Ticker(str(ticker_item)).info
			outputs.append(stockre)

		return render(request, 'add_stock.html', {'ticker': ticker, 'outputs':outputs})



def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request,("Stock has been deleted"))
	return redirect('add_stock')









