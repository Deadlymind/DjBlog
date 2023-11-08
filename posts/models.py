from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

'''
        1 : html widget
        2 : validation
        3 : best for db
'''

'''
    post:
        - title
        - content
        - draft
        - publish_date
        - autor
        - images
        - tags
        - category
        - comments
'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)
    # publish_date2 = models.DateTimeField(auto_now=True)

    tags = TaggableManager()


    def __str__(self):
        return self.title
