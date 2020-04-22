from django.db import models
from django.contrib.auth.models import *
from datetime import datetime
from django.urls import reverse
from django.core.exceptions import ValidationError

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Property(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    street_address = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=20)
    city= models.CharField(max_length = 10)
    zipcode = models.IntegerField()
    units = models.IntegerField()
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.ImageField(upload_to = 'media/images')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property:detail', kwargs={'slug': self.slug})

def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

class Contact(models.Model):
    first_name = models.CharField(max_length =20, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length = 20, validators = [validateLengthGreaterThanTwo])
    email = models.EmailField(validators = [validateLengthGreaterThanTwo])
    message = models.TextField(validators = [validateLengthGreaterThanTwo])
