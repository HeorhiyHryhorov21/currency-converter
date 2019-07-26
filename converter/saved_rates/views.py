from django.shortcuts import render, redirect
from django.http import HttpResponse
from saved_rates.models import Rates

# Create your views here.
def saved_rates(request):
    # get current logged in user
    current_user = request.user

    # get data from db
    rates = Rates.objects.all().filter(user_id = current_user.id)

    context = {
        'rates': rates
    }
    return render(request,'saved_rates/saved_rates.html', context)

def db_save(request):
    if request.method == 'POST':

        # get current user
        current_user = request.user

        #get POST request data
        table_rows = request.POST['text']
        rate = Rates(user_id=current_user.id, body=table_rows)

        # save a conversion record to db
        rate.save()
        return redirect('/saved_rates/')
        
