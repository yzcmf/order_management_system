# order_management_system
This is a system for online order management

Web 开发


Python + Django 


Start & Configuration

python manage.py runserver 0.0.0.0:80 (restart each time when we make changes)

python manage.py startup appname 



Network & URL

<1> order_manager_system / urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('sales.urls')),
]



<2>  sales / urls.py

from django.urls import path
from sales.views import listorders, listcustomers

urlpatterns = [
    path('orders/', listorders),
    path('customers/', listcustomers)
]


<3> http://127.0.0.1/sales/customers/?phonenumber=18870661556

id : 2 | name : 李逵 | phonenumber : 18870661556 | address : berkeley | qq : 354506121 |


def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph =  request.GET.get('phonenumber',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 定义返回字符串
    retStr = ''
    for customer in  qs:
        for name,value in customer.items():
            retStr += f'{name} : {value} | '
        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)





DataBase 

<1> create  a user database module =>
python manage.py startup common (数据库名称)


<2> update a user database module =>
python manage.py makemigrations common(数据库名称) — 修改代码端，在 ./imigrations 文件夹会生成记录
python manage.py migrate — 提交修改整个数据库
 

<3> create a superuser database account =>

python manage.py createsuperuser

zyx
yzcmf94@gmail.com
12345678
12345678


￼

Login in  http://127.0.0.1/admin/ 

Register a exist table 

修改应用里面的 管理员 配置文件 common/admin.py，注册我们定义的model类。

from django.contrib import admin

from .models import Customer

admin.site.register(Customer)



Bugs and fixed:

(1) https://forum.codewithmosh.com/t/no-such-table-main-auth-user-old/2415/3
(2) update database common， should use make, otherwise, our front end page will encounter an error

python manage.py makemigrations common(数据库名称) — 修改代码端，在 ./imigrations 文件夹会生成记录
python manage.py migrate — 提交修改整个数据库

 (3) why cannot change the front end page ‘药品‘ => ‘食品‘ ？

we should use txt editor instead of pycharm or webstorm， for they will lock the index.js when we make changes



跨平台app开发



架构设计


技术栈选择
<1>  REACT Native JS  + Python Django  + All Kinds
<2>  REACT Native JS  + Node JS + MongoDB




