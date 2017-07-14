from django.http import HttpResponse
from jazz.models import People
from django.shortcuts import render


def index(request):
    # return HttpResponse("jazz says hey there world!")
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    People_list = People.objects.order_by('last_name')[:5]
    context_dict = {'People': People_list}

    # Render the response and send it back!
    # return render(request, 'jazz/index.html', context_dict)
    return render(request, 'jazz/index.html', context_dict)
