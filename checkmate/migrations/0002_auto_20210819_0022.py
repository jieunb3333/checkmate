# Generated by Django 3.2.6 on 2021-08-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkmate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domitory_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='domitory_image/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='offcampus_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='offcampus_image/%Y/%m/%d'),
        ),
    ]