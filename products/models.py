from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Product(models.Model):
    title = models.CharField(default='例：抖音-用短视频记录美好', max_length=50)  # mc
    intro = models.TextField(default='写APP介绍')  # mt
    url = models.CharField(default='Http://', max_length=100)  # mc
    icon = models.ImageField(default='default_icon.jpg', upload_to='images/')  # mi
    image = models.ImageField(default='default_image.jpg', upload_to='images/')  #mi

    votes = models.IntegerField(default=1)  # mi
    pub_date = models.DateTimeField()  # md 发布时间
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)  # 发布人。ForeignKey：外借，寄生。用户删除时(on_delete)会使用cascade，即串联，连锁反应。
    
    def __str__(self):
        return self.title
