from django.urls import path
from Backend import views

urlpatterns=[
    path('viewindex/', views.viewindex, name="viewindex"),

    path('viewadmin/', views.viewadmin, name="viewadmin"),
    path('saveadmin/', views.saveadmin, name="saveadmin"),
    path('displayadmin/', views.displayadmin, name="displayadmin"),
    path('editadminpage/<int:dataid>/', views.editadminpage, name="editadminpage"),
    path('updateadmin/<int:dataid>/',views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),

    path('addcategory/',views.addcategory, name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategoryfn/', views.displaycategoryfn, name="displaycategoryfn"),
    path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory, name="deletecategory"),



    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct, name="deleteproduct"),



    path('viewlogin/', views.viewlogin, name="viewlogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),




    path('displaycontactfn/', views.displaycontactfn, name="displaycontactfn"),
    path('deletecontactfn/<int:dataid>/', views.deletecontactfn, name="deletecontactfn"),

    path('savecontactus/', views.savecontactus, name="savecontactus"),
    path('displaymessage/', views.displaymessage, name="displaymessage"),
    path('deletemessage/<int:dataid>/', views.deletemessage, name="deletemessage"),

]