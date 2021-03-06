from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser
from roommate.models import Write

# Create your models here.

class Offcampus_Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user_id = models.ForeignKey(CustomUser,on_delete=CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="offcampus_image/%Y/%m/%d",blank=True, null=True)
    view = models.IntegerField(default=0)


    CHOICES = (
        ('해결했어요', '해결했어요'),
        ('질문있어요', '질문있어요'),
        ('원룸정보', '원룸정보'),

        )
        # 앞의 값으로 저장되고 출력 시 뒤의 값으로 출력
    preface = models.CharField(max_length=10, choices=CHOICES)

    if (preface == 1 or 2):
        CHOICES_2 = (
        ('생활정보', '생활정보'),
        ('원룸', '원룸'),


        )
        # 앞의 값으로 저장되고 출력 시 뒤의 값으로 출력
        preface_2 = models.CharField(max_length=10, choices=CHOICES_2)
    else:
        
        CHOICES_2 = (
        ('정문', '정문'),
        ('후문', '후문'),
        ('남문', '남문'),
        ('호탄', '호탄'),
        ('기타', '기타'),

        )
        # 앞의 값으로 저장되고 출력 시 뒤의 값으로 출력
        preface_2 = models.CharField(max_length=10, choices=CHOICES_2)




class Domitory_Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user_id = models.ForeignKey(CustomUser,on_delete=CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="domitory_image/%Y/%m/%d", blank=True, null=True)
    view = models.IntegerField(default=0)



    CHOICES = (
        ('해결했어요', '해결했어요'),
        ('질문있어요', '질문있어요'),
        ( '기숙사정보', '기숙사정보'),
        ('기숙사후기', '기숙사후기'),

        )
        # 앞의 값으로 저장되고 출력 시 뒤의 값으로 출력
    preface = models.CharField(max_length=10, choices=CHOICES)

    if (preface == 1 or 2):
        CHOICES_2 = (
        ('생활정보', '생활정보'),
        ('아람관','아람관'),

        )
        # 앞의 값으로 저장되고 출력 시 뒤의 값으로 출력
        preface_2 = models.CharField(max_length=10, choices=CHOICES_2)
    else:
        
        CHOICES_2 = (
        ('1동', '1동'),
        ('2동', '2동'),
        ('3동', '3동'),
        ('4동', '4동'),
        ('5동', '5동'),
        ('6동', '6동'),
        ('7동', '7동'),
        ('8동', '8동'),
        ('9동', '9동'),
        ('10동', '10동'),
        ('11동', '11동'),
        ('개척관', '개척관'),

        )
        # 앞의 값으로 저장되고 출력 시 뒤의 값으로 출력
        preface_2 = models.CharField(max_length=10, choices=CHOICES_2)

class Scrap_roommate(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    write = models.ForeignKey(Write, on_delete=models.CASCADE)

class Scrap_dom(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Domitory_Post = models.ForeignKey(Domitory_Post, on_delete=models.CASCADE)

class Scrap_off(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Offcampus_Post = models.ForeignKey(Offcampus_Post, on_delete=models.CASCADE)

class Comment_dom (models.Model):
    writer = models.CharField(max_length=8)
    comment = models.CharField(max_length=200)
    write = models.ForeignKey("Domitory_Post", related_name="comments", on_delete=models.CASCADE)
    create_date=models.DateTimeField()
    def __str__(self):
        return self.writer

class Comment_off (models.Model):
    writer = models.CharField(max_length=8)
    comment = models.CharField(max_length=200)
    write = models.ForeignKey("Offcampus_Post", related_name="comments", on_delete=models.CASCADE)
    create_date=models.DateTimeField()
    def __str__(self):
        return self.writer