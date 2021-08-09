# Generated by Django 3.2.5 on 2021-08-09 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('survey', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Write',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('state', models.CharField(choices=[('1', '매칭중'), ('2', '매칭완료')], default='1', max_length=1)),
                ('survey_ess_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.surveyessential')),
                ('survey_opt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.surveyoptional')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
