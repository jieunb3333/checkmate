# Generated by Django 3.2.5 on 2021-07-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20210726_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyessential',
            name='earphones',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='surveyessential',
            name='invite_friends',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='surveyessential',
            name='smoke',
            field=models.NullBooleanField(default=False),
        ),
    ]