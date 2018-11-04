from django.db import models


class Schedule(models.Model):
    user = models.CharField(max_length=16, default='goodstart')
    label = models.CharField(max_length=8, default='myschedule')
    status = models.CharField(max_length=16, default='running')
    title = models.CharField(max_length=32, blank=False)
    text = models.TextField(blank=True)
    dt_start = models.CharField(max_length=16, blank=False)
    dt_end = models.CharField(max_length=16, blank=False)
    ts_create = models.DateTimeField(auto_now=True, null=True, blank=True)
    ts_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Label(models.Model):
    user = models.CharField(max_length=16, default='goodstart')
    label = models.CharField(max_length=8, default='myschedule')