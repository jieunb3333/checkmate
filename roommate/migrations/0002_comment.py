# Generated by Django 3.2.6 on 2021-08-19 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roommate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=8)),
                ('comment', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField()),
                ('write', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='roommate.write')),
            ],
        ),
    ]
