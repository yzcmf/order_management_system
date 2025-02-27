from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 导入 Customer 对象定义
from  common.models import Customer

def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")


# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        # %s
        
        {% for customer in customers %}
            <tr>

            {% for name, value in customer.items %}            
                <td>{{ value }}</td>            
            {% endfor %}
            
            </tr>
        {% endfor %}


        </table>
    </body>
</html>
'''


from django.template import engines
django_engine = engines['django']
template = django_engine.from_string(html_template)

def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('phonenumber', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber=ph)

    # # 定义返回字符串
    # retStr = ''
    # for customer in  qs:
    #     for name, value in customer.items():
    #         retStr += f'{name} : {value} | '
    #
    #     # <br> 表示换行
    #     retStr += '<br>'
    # return HttpResponse(retStr)

    # 生成html模板中要插入的html片段内容
    # tableContent = ''
    # for customer in qs:
    #     tableContent += '<tr>'
    #
    #     for name, value in customer.items():
    #         tableContent += f'<td>{value}</td>'
    #
    #     tableContent += '</tr>'
    # return HttpResponse(html_template % tableContent)

    # 传入渲染模板需要的参数
    rendered = template.render({'customers': qs})

    return HttpResponse(rendered)



