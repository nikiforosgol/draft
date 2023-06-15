from django.db import models


class PracticeArea(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    practice_area = models.ForeignKey(PracticeArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)
    template = models.FileField(upload_to='templates/', default='templates/BOJ Form 1_Template.docx')

    def __str__(self):
        return self.name


class Placeholder(models.Model):
    name = models.CharField(max_length=100)
    documents = models.ManyToManyField(Document)

    def __str__(self):
        return self.name


class UserInput(models.Model):
    placeholder = models.ForeignKey(Placeholder, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    # Add more fields as needed

