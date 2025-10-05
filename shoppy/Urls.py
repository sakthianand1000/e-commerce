from django.urls import path
from . import views

urlpatterns=[
  path("",views.home,name="home"),
  path("fav/",views.fav_page,name="fav"),
  path("login/",views.login_form,name="login"),
  path("register/",views.register,name="register"),
  path("form/",views.form,name="form"),
  path("collection/",views.collection,name="collection"),
  path("collectionview/",views.collectionview,name="collectionview"),
  path("fav_page/",views.fav_page,name="fav_page"),
  path("login_form/",views.login_form,name="login_form"),
  path("register/",views.register,name="register"),
  path("form/",views.form,name="form"),
  path("cart/",views.cart,name="cart")
]