
from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_categorie(request):
    if request.method == 'POST': #user post request koreche
        categorie_form  = forms.CategoryForm(request.POST) #user er post request data ekhane capture korlam
        if categorie_form.is_valid(): #post kora deta gula valid kina check kortesi
            categorie_form.save() #jodi data valid hoi tahole database e save hobe
            return redirect('add_categorie') #sob tik takle take add author ei url e pathi dibo
    else: #user normaly website e gele blank form pabe
        categorie_form = forms.CategoryForm()    
    return render(request, 'add_category.html', {'form' : categorie_form})