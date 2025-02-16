from django.shortcuts import render, redirect
from item.models import Category,Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.all()[0:6]
    print(f"Number of items: {items.count()}")
    all_items_count = Item.objects.count()
    print(f"Total number of items: {all_items_count}")
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

