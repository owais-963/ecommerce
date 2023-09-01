from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def test(request, nicNo):
    c = Customer.objects.get(NICno=nicNo)
    add = Address.objects.filter(customer_ID=nicNo)
    add = add[0]
    response = "Name: " + c.Fname + " " + c.Lname + " Phone NO " + c.phoneNo + " Email " + c.email
    response1 = add.street_add + " " + str(add.postal_code) + " " + add.city + " " + add.state + " " + add.country
    return HttpResponse("Personal info:  " + response + "<br>Address:  " + response1)


def index(request):
    if request.session.has_key('user_logged'):
        userLogged = True
    else:
        userLogged = False

    c = Customer.objects.order_by('date_of_join').all()
    info = c.all()[:]
    add = Address.objects.all()[:]
    context = {
        'info': info, 'addr': add, 'userLogged': userLogged,
    }
    return render(request, 'shop/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save the user instance
            user = form.save(commit=False)
            # user.password=(form.cleaned_data['password'])
            user.save()

            return redirect('login')

            # Create an Address instance associated with the user
        else:
            signup_form = SignupForm()
            messages.error(request, form.errors)
            return render(request, 'shop/form.html',
                          {'signup_form': signup_form})
    else:
        signup_form = SignupForm()
        return render(request, 'shop/form.html', {'signup_form': signup_form})


def login(request):
    if request.method == "POST":
        nic = request.POST['nic']
        pas = request.POST['password']
        try:
            c = Customer.objects.get(NICno=nic)
            if c.password == pas:
                request.session['user_logged'] = True
                request.session['user'] = c.NICno
                return redirect('index')
            else:
                messages.error(request, 'Invalid password')
                return redirect('login')
        except:
            messages.error(request, 'Invalid user')
            return redirect('login')
    else:
        return render(request, 'shop/login.html')
    # return HttpResponse("<h1> Welcome to login </h1>")


def logOut(request):
    del request.session['user_logged']
    return redirect('login')


def profile(request):
    return render(request, 'shop/profile.html')


def orders(request):
    return render(request, 'shop/orders.html')


def cart(request):
    return render(request, 'shop/cart.html')


def categories(request):
    return render(request, 'shop/categories.html')


def explore(request):
    return render(request, 'shop/explore.html')


def contact(request):
    return render(request, 'shop/contact.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
