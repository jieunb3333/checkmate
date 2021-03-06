from django.db import models
from account.models import CustomUser
from survey.models import SurveyEssential, SurveyOptional


# Create your models here.

class Write(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    state_choice = (
        ('1', '매칭중'), 
        ('2', '매칭완료'),
        )
    state = models.CharField(max_length=1, choices=state_choice, default='1')

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    survey_ess_id = models.ForeignKey(SurveyEssential, on_delete=models.CASCADE)
    survey_opt_id = models.ForeignKey(SurveyOptional, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment (models.Model):
    writer = models.CharField(max_length=8)
    comment = models.CharField(max_length=200)
    write = models.ForeignKey("Write", related_name="comments", on_delete=models.CASCADE)
    create_date=models.DateTimeField()
    def __str__(self):
        return self.writer