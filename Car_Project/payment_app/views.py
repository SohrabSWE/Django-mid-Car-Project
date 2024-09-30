from django.shortcuts import render, redirect
from payment_app.models import PaymentModel
from post_app.models import Post
from payment_app.forms import PaymentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def payment_by_car(request, id):
    item = Post.objects.get(pk=id)

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]

            if item.car_quantity >= quantity:
                item.car_quantity -= quantity
                item.save()

                historie = PaymentModel.objects.create(
                    car_model=item,
                    user=request.user,
                    net_quantity=quantity,
                    total_price=item.price * quantity,
                )
                messages.success(request,"Payment Succesful.You will receive your product withiin 2 days.",)
                return redirect("detail_post", id=item.pk)
            else:
                messages.error(request, "Insufficient quantity")
        else:
            messages.error(request, "Please Type Interger Or Number")
    else:
        form = PaymentForm()
    return render(request, "buynow.html", {"form": form})