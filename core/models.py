from django.db import models


class Course(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    level = models.CharField(
        max_length=100,
        default='Beginner'
    )

    hours = models.PositiveIntegerField(
        default=0
    )

    lectures = models.PositiveIntegerField(
        default=0
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Service(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class Statistic(models.Model):

    title = models.CharField(
        max_length=100
    )

    value = models.CharField(
        max_length=50
    )

    icon = models.CharField(
        max_length=100
    )

    is_active = models.BooleanField(
        default=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.title} - {self.value}"