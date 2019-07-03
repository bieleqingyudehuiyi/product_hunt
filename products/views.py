from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.

def product_list(request):
    return render(request,'product_list.html')

#添加装饰器，只有当用户登陆后才能跳到该页面
@login_required
def publish(request):
    if request.method == 'GET':
        return render(request,'publish.html')
    elif request.method == 'POST':
        #用户提交的信息
        title = request.POST['标题']
        intro = request.POST['介绍']
        url = request.POST['APP链接']
        try:
            icon = request.FILES['APP图标']
            image = request.FILES['大图']

             #用户传递的信息需要传递给model,因此创建一个model
            product = Product()
            product.title = title
            product.intro = intro
            product.url = url
            product.icon = icon
            product.image = image

            product.pub_date = timezone.datetime.now()
            #用户
            product.hunter = request.user
            #保存   
            product.save()

            return redirect('主页')

        except Exception as err:
            return render(request, 'publish.html', {'错误' :'请上传图片'})

       