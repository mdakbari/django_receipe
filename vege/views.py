# from pyexpat.errors import messages
from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here
@login_required(login_url='/login/')
def receipe(request):
    if request.method =='POST':
        receipe_img = request.FILES.get('receipe_img')
        receipe_name = request.POST.get('receipe_name')
        receipe_ingr = request.POST.get('receipe_ingr')
        receipe_desc = request.POST.get('receipe_desc')

        try:
            hid = request.POST.get('hid')
            obj = Vege.objects.get(id=hid)
            if receipe_img:
                obj.receipe_img = receipe_img
            obj.receipe_name = receipe_name
            obj.receipe_desc = receipe_desc
            obj.receipe_ingr = receipe_ingr
            obj.save()
        except:
            Vege.objects.create(
                receipe_desc=receipe_desc,
                receipe_name=receipe_name,
                receipe_img=receipe_img,
                receipe_ingr=receipe_ingr
            ) 
        return redirect('/data/')
    else: 
        pass
    
    set= {
        'path': request.path
    }
    return render(request,'index.html',set)


def receipe_1(request, hid):
    try:
        obj = Vege.objects.get(id=hid)
    except:
        return redirect('/')

    items = {
        'obj': obj,
        'hid': hid,
        'path': request.path
    }
    return render(request,'index.html', items)

@login_required(login_url='/login/')
def showdata(request):

    qset  = Vege.objects.all()
    if request.GET.get('search'):
        x = request.GET.get('search')
        qset = qset.filter(receipe_name__icontains=x)
    context = {'vege': qset, 'path': request.path}
    return render(request, 'data.html', context)

def deletedata(request, id):
    try:
        qset = Vege.objects.get(id=id)
        qset.delete()
    except:
        pass
    return redirect('/data/')

# def search(request):
#     query = request.GET.get('search')

#     if query:
#         qset = Vege.objects.filter(receipe_name__icontains=query)
#         context = {'vege': qset, 'query': query}
#         return render(request, 'data.html', context)
#     else:
#         return render(request, 'data.html', {'vege': Vege.objects.all()})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username =username).exists():
            messages.error(request, 'Username does not exists')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('/login/')
    set = { 'path': request.path}
    return render(request, 'login.html', set)

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            hid = request.POST.get('hid')
            obj = User.objects.get(id=hid)
            obj.first_name = first_name
            obj.last_name = last_name
            obj.user_name = username
            obj.password = password
            obj.save()
        except:
            
            user = User.objects.filter(username=username)

            if user.exists():
                messages.info(request, 'Username already exists')
                return redirect('/register/')

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username
                
            )
            user.set_password(password)
            user.save()
            messages.info(request, 'User created successfully')

            
        return redirect('/login/')

    return render(request, 'register.html', {'path': request.path})

def logout_page(request):
    logout(request)
    return redirect('/login/')
