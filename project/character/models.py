from django.db import models

class Character(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    social_life = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    dependence = models.IntegerField(default=0)
    count_for_question = models.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'