from django.db import models

class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    social_life = models.IntegerField()
    grade = models.IntegerField()
    dependence = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'