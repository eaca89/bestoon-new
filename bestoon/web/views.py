from json.encoder import JSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Expense, Income
from datetime import datetime

@csrf_exempt
def submit_income(request):

    #TODO: validate data. user might be fake. Token might be fake. amount might be fake.
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    
    Income.objects.create(
        user=this_user, amount=request.POST['amount'],
        text=request.POST['text'], date=date)

    print('I\'m in submit expense')
    print(request.POST)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):

    #TODO: validate data. user might be fake. Token might be fake. amount might be fake.
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    
    Expense.objects.create(
        user=this_user, amount=request.POST['amount'],
        text=request.POST['text'], date=date)

    print('I\'m in submit expense')
    print(request.POST)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
