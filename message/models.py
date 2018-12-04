from django.db import models
from django.utils import timezone
# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名',null=False, blank=True, default="")
    email = models.EmailField(verbose_name='邮箱',null=False,blank=True,default="")
    text = models.TextField(verbose_name='留言内容',null=False,blank=True,default="")
    create_time = models.DateTimeField(default=timezone.now(),verbose_name='创建时间',null=False,blank=False)

    class Meta:
        verbose_name = '留言板内容'
        ordering = ['-create_time']
        db_table = "message"


