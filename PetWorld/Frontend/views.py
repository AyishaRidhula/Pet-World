from django.contrib import messages
from django.shortcuts import render, redirect

from Backend.models import categordb, productdb
from Frontend.models import cartdb, customerdb


# Create your views here.
def homepage(req):
    data = categordb.objects.all()
    return render(req,"Home.html" , {'data': data})

def disproduct(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(CATEGORY=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"products.html",context)

def contactpage(req):
    return render(req, "contact.html")
def aboutpage(req):
    return render(req, "about.html")

def productsingle(request,dataid):
    data=productdb.objects.get(id=dataid)
    return render(request,"single.html",{'dat':data})

def viewcart(req):
    data=cartdb.objects.all()
    return render(req,"cartpage.html",{'data':data})

def savecart(req):
    if req.method == "POST":
        na = req.POST.get('name')
        qty = req.POST.get('quantity')
        tp = req.POST.get('totalprice')
        obj = cartdb(Name=na, Quantity=qty, Total=tp)
        obj.save()
        return redirect(homepage)

def deletecartfont(req,dataid):
    data = cartdb.objects.get(id=dataid)
    data.delete()
    return redirect(viewcart)

def viewcheckout(req):
    data = cartdb.objects.all()
    return render(req,"checkout.html", {'data':data})

def cat(req):
    data = categordb.objects.all()
    return render(req,"categories.html",{'data': data})


def weblogin(req):
    return render(req,"weblogin.html")

def savecustomer(request):
    if request.method == "POST":
        Us  = request.POST.get('username')
        Em = request.POST.get('email')
        pas = request.POST.get('password')
        Cp  = request.POST.get("conpassword")
        if pas==Cp:
            obj = customerdb(Username=Us,Password=pas,Confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request, "Registered Successfully")

        return redirect(weblogin)

def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if customerdb.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request, "Login Successfully...!")
            return redirect(homepage)
        else:
            messages.error(request,"Invalid User..!")
            return render(request,'weblogin.html')

def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    return redirect(weblogin)

def singlee(req,dataid):
    data = productdb.objects.get(id=dataid)
    return render(req,"single1.html",{'dat':data})
