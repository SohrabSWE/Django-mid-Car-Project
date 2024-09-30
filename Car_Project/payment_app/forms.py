from django import forms

class PaymentForm(forms.Form):
    quantity=forms.IntegerField(min_value=1)