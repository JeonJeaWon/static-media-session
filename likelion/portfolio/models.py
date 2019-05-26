from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    #문자열 최대 255
    image = models.ImageField(upload_to='images/')
    #이미지를 받는 field
    description = models.CharField(max_length=500)
    #문자열을 받는 field

    def __str__(self):
        return self.title
        #admin site에 타이틀이 뜨도록 함.