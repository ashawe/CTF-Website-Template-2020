from django.db import models
from django.contrib.auth.models import User


EASY = 'E'
MEDIUM = 'M'
HARD = 'H'
WEB = 'category_web'
REVERSE = 'category_reversing'
STEG = 'category_steg'
PWNING = 'category_pwning'
MISC = 'category_misc'
CRYPT = 'category_crypt'


difficulty = [(EASY, 'easy'), (MEDIUM, 'medium'), (HARD, 'hard')]
category = [(WEB, 'category_web'), (REVERSE, 'category_reversing'), (STEG, 'category_steg'), (PWNING, 'category_pwning'), (MISC, 'category_misc'), (CRYPT, 'category_crypt')]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Rid = models.CharField(max_length=100, default="EINC-5e5a")  # reciept id
    score = models.IntegerField(default=0)
    totlesub = models.IntegerField(default=0)
    latest_sub_time = models.CharField(default="00:00", max_length=10)
    time = models.TimeField(default="00:00")

    def __str__(self):
        return self.user.username


class Questions(models.Model):
    Qid = models.IntegerField(default='0')
    Qtitle = models.CharField(max_length=70)
    Qdes = models.CharField(max_length=1000)
    Hint = models.CharField(max_length=500, default="hint is ----")
    level = models.CharField(max_length=2, choices=difficulty, default=HARD)
    Easy = models.IntegerField(default=1)
    Med = models.IntegerField(default=1)
    Hard = models.IntegerField(default=1)
    flag = models.CharField(max_length=100, default='pict_CTF{}')
    points = models.IntegerField(default=0)
    solved_by = models.IntegerField(default=0)
    file = models.FileField(blank=True)
    category = models.CharField(max_length=50, choices=category, default=STEG)


class Submission(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    curr_score = models.IntegerField(default=0)
    solved = models.IntegerField(default=0)
    sub_time = models.CharField(default="00:00", max_length=10)
