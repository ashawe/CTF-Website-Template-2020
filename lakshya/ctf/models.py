from django.db import models
from django.contrib.auth.models import User

VERY_EASY = 'VE'
EASY = 'E'
MEDIUM = 'M'
HARD = 'H'
VERY_HARD = 'VH'
difficulty = [(VERY_EASY, 'very_easy'), (EASY,'easy'), (MEDIUM, 'medium'), (HARD, 'hard'), (VERY_HARD, 'very_hard')]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='example@gmail.com')
    phone = models.CharField(max_length=10)
    clg = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, null=True)
    dept = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    totlesub = models.IntegerField(default=0)
    time = models.TimeField(default="00:00")
    Rid = models.CharField(max_length=100, default="EINC-5e5a")   #reciept id

    def __str__(self):
        return self.user.username


class Questions(models.Model):
    Qid = models.IntegerField(default='0')
    Qtitle = models.CharField(max_length=70)
    Qdes = models.CharField(max_length=1000)
    Hint = models.CharField(max_length=500, default="this is hint")
    level = models.CharField(max_length=2, choices=difficulty, default=HARD)
    flag = models.CharField(max_length=100, default='pict_CTF{}')
    points = models.IntegerField(default=0)
    solved = models.IntegerField(default=0)


class Submission(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sub_time = models.IntegerField(default=0)
