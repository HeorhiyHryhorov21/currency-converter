from django.shortcuts import render
import requests
from django.http import HttpResponse
import json
from math import floor

# Create your views here.
def index(request):
    return render(request, 'currency_exchange/index.html')

def currency_table(request):
    return render(request,'currency_exchange/currency_table.html')

def signup_login(request):
    return render(request,'currency_exchange/signup_login.html')

def exchange(request):
    if request.method == 'POST':

        # get data from post request
        amount = request.POST['amount']
        from_convert = request.POST['from_convert']
        to_convert = request.POST['to_convert']
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']

        if len(month) < 2 :
            month = '0' + month

        # send a request to converter api
        url = f'https://free.currencyconverterapi.com/api/v5/convert?q={from_convert}_{to_convert}&compact=ultra&date={year}-{month}-{day}&apiKey=ee368c0a2db8983f80bd'

        response = requests.get(url)
        data = response.json()

        # multiply currency rate by amount
        result = round(data[f'{from_convert}_{to_convert}'][f'{year}-{month}-{day}'], 2) * int(amount)
        
        # return data to ajax success function
        return HttpResponse(result)

def exchange_table(request):
    if request.method == 'POST':

        # get data from post request
        from_convert = request.POST['from_convert']
        to_convert = request.POST['to_convert']
        start_day = request.POST['start_day']
        start_month = request.POST['start_month']
        start_year = request.POST['start_year']

        end_day = request.POST['end_day']
        end_month = request.POST['end_month']
        end_year = request.POST['end_year']

        if len(start_month) < 2 :
            start_month = '0' + start_month

        if len(end_month) < 2 :
            end_month = '0' + end_month

        # send a request to converter api
        url = f'https://free.currencyconverterapi.com/api/v5/convert?q={from_convert}_{to_convert}&compact=ultra&date={start_year}-{start_month}-{start_day}&endDate={end_year}-{end_month}-{end_day}&apiKey=ee368c0a2db8983f80bd'

        response = requests.get(url)
        data = response.json()
        
        # multiply currency rate by amount
        
        # return data to ajax success function
        return HttpResponse(json.dumps(data[f'{from_convert}_{to_convert}']), content_type="application/json")

