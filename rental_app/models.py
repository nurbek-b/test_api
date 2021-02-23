from django.db import models


class Friend(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)


class Belonging(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)


class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    whom = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
