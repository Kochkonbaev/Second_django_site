from django.db import models

class Landing(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.URLField()

    def __str__(self):
        return self.title

class Workers(models.Model):
    firs_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    position = models.CharField(max_length=100)
    text = models.TextField()
    img = models.URLField()


    def __str__(self):
        return f'{self.firs_name} {self.last_name}'


class Feedback(models.Model):
    
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    

    def __str__(self):
        return f'Спасибо за отклик, {self.name}'
