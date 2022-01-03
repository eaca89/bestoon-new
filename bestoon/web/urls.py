from django.urls.conf import path
from . import views

urlpatterns = [
    path('submit/expense/', views.submit_expense, name='submit_expense')
]