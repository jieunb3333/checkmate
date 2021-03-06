# Generated by Django 3.2 on 2021-08-14 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyEssential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('1', '1학년'), ('2', '2학년'), ('3', '3학년'), ('4', '4학년'), ('5', '5학년'), ('6', '6학년')], default='1', max_length=1)),
                ('room_type', models.CharField(choices=[('0', '기숙사'), ('1', '자취')], default='0', max_length=1)),
                ('dormitory_number_man', models.CharField(blank=True, choices=[('10', '10동'), ('8', '8동'), ('6', '6동'), ('3', '3동'), ('2', '2동'), ('1', '1동')], default='10', max_length=2, null=True)),
                ('dormitory_number_woman', models.CharField(blank=True, choices=[('11', '11동'), ('9', '9동'), ('7', '7동'), ('5', '5동'), ('4', '4동')], default='11', max_length=2, null=True)),
                ('dormitory_year_start', models.CharField(choices=[('2021', '2021년도'), ('2022', '2022년도'), ('2023', '2023년도')], default='2021', max_length=4)),
                ('dormitory_semester_start', models.CharField(choices=[('1', '1학기'), ('2', '여름방학'), ('3', '2학기'), ('4', '겨울방학')], default='1', max_length=1)),
                ('dormitory_year_end', models.CharField(choices=[('2021', '2021년도'), ('2022', '2022년도'), ('2023', '2023년도')], default='2021', max_length=4)),
                ('dormitory_semester_end', models.CharField(choices=[('1', '1학기'), ('2', '여름방학'), ('3', '2학기'), ('4', '겨울방학')], default='1', max_length=1)),
                ('relationship', models.CharField(choices=[('0', '친하게'), ('1', '인사만')], default='0', max_length=1)),
                ('wakeup_time', models.TimeField(default=datetime.time(9, 0))),
                ('bed_time', models.TimeField(default=datetime.time(23, 0))),
                ('smoke', models.NullBooleanField(default=False)),
                ('cleaning', models.IntegerField(default='3')),
                ('sleeping_habits_snoring', models.NullBooleanField(default=False)),
                ('sleeping_habits_teeth', models.NullBooleanField(default=False)),
                ('sleeping_habits_other', models.CharField(blank=True, max_length=10, null=True)),
                ('sleeping_habits_nothing', models.NullBooleanField(default=False)),
                ('invite_friends', models.NullBooleanField(default=False)),
                ('call', models.CharField(choices=[('0', '예'), ('1', '아니요'), ('2', '짧은 통화만')], default='0', max_length=1)),
                ('earphones', models.NullBooleanField(default=True)),
                ('eat', models.CharField(choices=[('0', '식사도 방안에서'), ('1', '냄새 안 나는 음식만(간식)'), ('2', '나가서 먹음')], default='0', max_length=1)),
                ('animal_cat', models.NullBooleanField(default=False)),
                ('animal_dog', models.NullBooleanField(default=False)),
                ('animal_no', models.NullBooleanField(default=False)),
                ('animal_other', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyOptional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.CharField(choices=[('0', '선택안함'), ('1', '공유'), ('2', '각자')], default='0', max_length=1)),
                ('toilet', models.IntegerField(blank=True, null=True)),
                ('ventilate', models.IntegerField(blank=True, null=True)),
                ('feel_cold', models.NullBooleanField()),
                ('feel_hot', models.NullBooleanField()),
                ('bug', models.CharField(choices=[('0', '선택안함'), ('1', '잘잡음'), ('2', '못잡음')], default='0', max_length=1)),
                ('keyboard', models.CharField(blank=True, choices=[('0', '선택안함'), ('1', '타이핑&게임 자주함'), ('2', '거의 안함')], max_length=1, null=True)),
                ('keyboard_noise', models.NullBooleanField()),
                ('game', models.CharField(blank=True, choices=[('0', '선택안함'), ('1', '자주'), ('2', '가끔'), ('3', '안함')], max_length=1, null=True)),
                ('mbti', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]
