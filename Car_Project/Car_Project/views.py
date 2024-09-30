
from django.shortcuts import render
from categories_app.models import Category
from post_app.models import Post 
 

def home(request, category_slug=None):
    unauthenticated_user = Post.objects.order_by("?")[:8]
    authenticated_user = Post.objects.all()  
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)  
        authenticated_user = Post.objects.filter(category=category)  
    categories = Category.objects.all()  
    context = {
        'unauthenticated_user': unauthenticated_user,
        'authenticated_user': authenticated_user,
        'category': categories,
    }
    return render(request, 'home.html', context)