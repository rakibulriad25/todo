from operator import mod
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.http import HttpResponse
from django.shortcuts import render


# Create your models here.

class Create(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()


# class Edit(models.Model):
#     title = models.ForeignKey(Create, on_delete=models.CASCADE, related_name='titles')
#     desc = models.ForeignKey(Create, on_delete=models.CASCADE, related_name='description')


