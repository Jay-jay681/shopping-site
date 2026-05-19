from django.shortcuts import render , redirect
from .form import Register
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category , Item
from django.contrib.auth import authenticate , login as auth_login ,logout as auth_logout


# Create your views here.

def home(request):
    #categories = Category.objects.all()
    return render(request, 'homepage.html' ,) #{'categories':categories})

def signup(request):
    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully' + str(user))
        return redirect ('login')
    
    else:
        form = Register()
    return render(request, 'register.html' , {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def items(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    return render(request , 'items.html',{
        'categories':categories,
        'items':items,
    })

def details(request , pk):
    item = Item.objects.get(id=pk)
    return render(request , 'details.html' , {
        'item':item, })

def category(request , pk):
    # replace hyphen with space
    pk = pk.replace('-' , ' ')

    # grwab category from url
    try:
        # look up the category
        category = Category.objects.get(name=pk)
        item = Item.objects.filter(category=category)
        return render(request , 'category.html' , {
            'category':category, 
            'item':item, })
        
    except:
        messages.success(request, 'That category does not exist')
        return redirect('home')
    


# cart

@login_required
def cart_summary(request):
    try:
        return render(request , 'cart_summary.html' , {})
    except:
        return redirect ('login')


def cart_add(request):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass