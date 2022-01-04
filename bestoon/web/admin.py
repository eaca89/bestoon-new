from django.contrib import admin
from django.contrib.auth.models import User
from .models import Expense, Income, Token

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'amount', 'date')
    # list_display_links = ('id', 'title')
    # list_filter = ('realtor',)
    # list_editable = ('is_published',)
    # search_fields = ('title', 'description', 'address', 'state', 'zipcode', 'price')
    list_per_page = 25

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'amount', 'date')    
    list_per_page = 25

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Token)