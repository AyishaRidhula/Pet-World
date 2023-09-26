from django.urls import path

from Frontend import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('disproduct/<itemcatg>/',views.disproduct,name="disproduct"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('productsingle/<int:dataid>',views.productsingle,name="productsingle"),
    path('viewcart/',views.viewcart,name="viewcart"),
    path('savecart/',views.savecart,name="savecart"),
    path('deletecartfont/<int:dataid>/', views.deletecartfont, name="deletecartfont"),
    path('viewcheckout/', views.viewcheckout, name="viewcheckout"),
    path('cat/',views.cat,name="cat"),
    path('weblogin/', views.weblogin, name="weblogin"),
    path('savecustomer/', views.savecustomer, name="savecustomer"),
    path('custemerlogin/', views.custemerlogin, name="custemerlogin"),
    path('logout/', views.logout, name="logout"),
    path('singlee/<int:dataid>',views.singlee,name="singlee")

]

