from . import views
from django.urls import path

app_name = 'store'

urlpatterns = [
    path('', views.index, name="index"),
    path('customer/', views.customer_page, name='customer_page'),
    path('employee/', views.employee_page, name='employee_page'),
    path('admin_page/', views.admin_page, name='admin_page'),
]