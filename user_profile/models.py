from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    Customer model exands on allauth user model.
    Name and email are autofilled from the associated
    user model.
    The customer model has additional attributes of
    physical addresses, shipping and billing, as well
    as a nickname field, left optional. This will be used
    later, where customers will be prompted to use
    customised aliases for social actions, such as reviews
    or comments.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    shipping_address = models.TextField()
    billing_address = models.TextField()
    nickname = models.CharField(max_length=255, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.user.get_full_name()
        if not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
