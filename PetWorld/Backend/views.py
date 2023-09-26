from django.shortcuts import render,redirect
# Create your views here.
from Backend.models import admindb, categordb, productdb, admincontactdb, contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from Frontend.views import contactpage


def viewindex(req):
    return render(req,"index.html")

def viewadmin(req):
    return  render(req,"addadmin.html")
def saveadmin(req):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        num = req.POST.get('number')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        img = req.FILES['image']
        obj = admindb(NAME=na, EMAIL=email, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=img)
        obj.save()
        return redirect(viewadmin)
def displayadmin(req):
    data = admindb.objects.all()
    return render(req,"displayadmin.html", {'data':data})

def editadminpage(req,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html", {'data':data})
def updateadmin(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        num = req.POST.get('number')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).IMAGE
        admindb.objects.filter(id=dataid).update(NAME=na, EMAIL=email, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=file)
        return redirect(displayadmin)

def deleteadmin(req,dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)


def addcategory(req):
    return render(req,"addcategory.html")
def savecategory(req):
    if req.method == "POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        img = req.FILES['image']
        obj =categordb(NAME=na, DISCRIPTION=dis, IMAGE=img)
        obj.save()
        return redirect(addcategory)
def displaycategoryfn(req):
    data = categordb.objects.all()
    return render(req,"displaycategory.html",{'data':data})

def editcategory(req,dataid):
    data = categordb.objects.get(id=dataid)
    print(data)
    return render(req,"editcategory.html",{'data':data})
def updatecategory(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categordb.objects.get(id=dataid).IMAGE
        categordb.objects.filter(id=dataid).update(NAME=na, DISCRIPTION=dis, IMAGE=file)
        return redirect(displaycategoryfn)
def deletecategory(req,dataid):
    data = categordb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategoryfn)




def addproduct(req):
    data =categordb.objects.all()
    return render(req,"addproductpage.html", {'data':data})
def saveproduct(req):
    if req.method == "POST":
        cat = req.POST.get('category')
        na = req.POST.get('name')
        quan = req.POST.get('quantity')
        prz = req.POST.get('prize')
        dis = req.POST.get('discription')
        img = req.FILES['image']
        obj = productdb(NAME=na, CATEGORY=cat, PRIZE=prz, QUANTITY=quan, DISCRIPTION=dis, IMAGE=img)
        obj.save()
        return redirect(addproduct)
def displayproduct(req):
    data = productdb.objects.all()
    return render(req,"displayproductpage.html", {'data':data})
def editproduct(req,dataid):
    data= productdb.objects.get(id=dataid)
    da = categordb.objects.all()
    return render(req,"editproductpage.html", {'datas':data,'da':da})
def updateproduct(req,dataid):
    if req.method == "POST":
        cat = req.POST.get('category')
        na = req.POST.get('name')
        quan = req.POST.get('quantity')
        prz = req.POST.get('prize')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= productdb.objects.get(id=dataid).IMAGE
        productdb.objects.filter(id=dataid).update(NAME=na, CATEGORY=cat, PRIZE=prz, QUANTITY=quan, DISCRIPTION=dis, IMAGE=file)
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    data.delete()
    return redirect(displayproduct)




def viewlogin(req):
    return render(req,"login.html")
def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(viewindex)
            else:
                return redirect(viewadmin)
        else:
            return redirect(viewadmin)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(viewlogin)


def displaycontactfn(req):
    data = admincontactdb.objects.all()
    return render(req,"dispalycontactus.html", {'data':data})
def deletecontactfn(req,dataid):
    data = admincontactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontactfn)

def savecontactus(req):
    if req.method=="POST":
        na = req.POST.get('name')
        ln= req.POST.get('lname')
        em = req.POST.get('email')
        sb = req.POST.get('subject')
        ms = req.POST.get('message')
        obj = contactdb(Name=na,LName=ln,Email=em,Subject=sb,Message=ms)
        obj.save()
        return redirect(contactpage)

def displaymessage(req):
    data=contactdb.objects.all()
    return render(req,"displaycontact.html",{'data':data})

def deletemessage(req,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymessage)