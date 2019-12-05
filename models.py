from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Statistic(models.Model):
    page_name = models.CharField(max_length=100, default='index')
    number_of_clicks = models.IntegerField(default=0)

    def __str__(self):
        return 'Number of clicks of ' + self.page_name + ': ' + str(self.number_of_clicks)

class Course(models.Model):
    course_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.course_name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOR = models.DateField(default=timezone.now())
    author_qualification = models.TextField(max_length=500)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Article(models.Model):
    article_name = models.CharField(max_length=1000)
    article_text = models.TextField(default="")
    article_date = models.DateField('date published')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_name

class Comment(models.Model):
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=1000)
    comment_email = models.CharField(max_length=1000)
    comment_date = models.DateField(default=timezone.now())
    comment_text = models.TextField(default='')

    def __str__(self):
        return self.comment_article.article_name + ' ' + self.comment_author
