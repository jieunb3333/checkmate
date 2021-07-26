# Generated by Django 3.2.5 on 2021-07-25 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyOptional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share', models.BooleanField()),
                ('toilet', models.IntegerField()),
                ('ventilate', models.IntegerField()),
                ('feel', models.IntegerField()),
                ('bug', models.BooleanField()),
                ('keyboard', models.IntegerField()),
                ('game', models.BooleanField()),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyEssential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('room_type', models.BooleanField()),
                ('dormitory_number', models.CharField(choices=[(10, '10동'), (8, '8동'), (6, '6동'), (3, '3동'), (2, '2동'), (1, '1동')], default=10, max_length=1)),
                ('dormitory_year_start', models.IntegerField()),
                ('dormitory_semester_start', models.CharField(choices=[('1', '1학기'), ('S', '여름방학'), ('2', '2학기'), ('W', '겨울방학')], default=10, max_length=1)),
                ('dormitory_year_end', models.IntegerField()),
                ('dormitory_semester_end', models.CharField(choices=[('1', '1학기'), ('S', '여름방학'), ('2', '2학기'), ('W', '겨울방학')], default=10, max_length=1)),
                ('relationship', models.BooleanField()),
                ('wakeup_time', models.DateField()),
                ('bed_time', models.DateField()),
                ('smoke', models.BooleanField()),
                ('cleaning', models.IntegerField()),
                ('sleeping_habits', models.BooleanField()),
                ('sleeping_habits_other', models.CharField(max_length=10)),
                ('invite_friends', models.BooleanField()),
                ('earphone', models.BooleanField()),
                ('eat', models.IntegerField()),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]