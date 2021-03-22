from django.urls import path
from .views import ItemCreate, ItemView, ItemDelete, PurchaseCreate, PurchaseView, \
    PurchaseDelete, PurchaseEdit, PurchaseDetailedView, OrderCreate, OrderLineCreate, \
    BillGenrate, Registration, LoginView, SearchView, DailySales

urlpatterns = [
    path('item', ItemCreate.as_view(), name='item'),
    path('itemview', ItemView.as_view(), name='itemview'),
    path('itemdelete/<int:pk>', ItemDelete.as_view(), name='itemdelete'),
    path('productcreate', PurchaseCreate.as_view(), name='productcreate'),
    path('purchaseview', PurchaseView.as_view(), name='purchaseview'),
    path('productdelete/<int:pk>', PurchaseDelete.as_view(), name='productdelete'),
    path('productedit/<int:pk>', PurchaseEdit.as_view(), name='productedit'),
    path('productview/<int:pk>', PurchaseDetailedView.as_view(), name='productview'),
    path('ordercreate', OrderCreate.as_view(), name='ordercreate'),
    path('orderlinecreate/<str:billnumber>', OrderLineCreate.as_view(), name='orderlinecreate'),
    path('generatebill/<str:billnumber>', BillGenrate.as_view(), name='generatebill'),
    path('register',Registration.as_view(), name='register'),
    path('signin',LoginView.as_view(), name='signin'),
    path('search', SearchView.as_view(), name='search'),
    path('dsales', DailySales.as_view(), name='dsales')


]