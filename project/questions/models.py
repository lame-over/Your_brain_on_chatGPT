from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200, unique=True, blank=False, null=True)
    description = models.TextField(unique=False, blank=False, null=True)
    index = models.IntegerField(unique=True, blank=False, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['index']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Decision(models.Model):
    question_index = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    social_life = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    dependence = models.IntegerField(blank=True, null=True)
    
    minimal_value_for_grade = models.IntegerField(blank=True, null=True)
    minimal_value_for_social_life = models.IntegerField(blank=True, null=True)
    minimal_value_for_dependence = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Decision'
        verbose_name_plural = 'Decisions'

class Endings(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    social_life = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    dependence = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ending'
        verbose_name_plural = 'Endings'