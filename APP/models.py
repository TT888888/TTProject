from django.db import models

# 建模型

class Post(models.Model):
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
