from django.db import models
# Create your models here.
class Location(models.Model):
    area = models.CharField(max_length=64)
    pincode = models.IntegerField()

    def __str__(self):
        return f"{self.area} ({self.pincode})"


class Subject(models.Model):
    subject = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.subject}"

class Teacher(models.Model):
    CLASS_CHOICES = (('1-5', 'First to Fifth'),
                    ('6-8', 'Sixth to Eighth'),
                    ('9-10', 'Ninth to Tenth'),
                    ('11-12', 'Eleventh to Twelfth')
    )

    TUTOR_CHOICES = ( 
                    ('Home Tutor', 'HT'),
                    ('Tution Center Teacher', 'TT')
                    )

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    experience = models.DecimalField(max_digits=4, decimal_places=2)
    classes = models.CharField(max_length=6, choices=CLASS_CHOICES)
    phone = models.CharField(max_length=10)
    photo = models.ImageField(blank=True, null=True, upload_to='teachers/%Y/%m/%D/')
    teacher_type = models.CharField(max_length=30 ,choices=TUTOR_CHOICES, blank=True)
    address = models.CharField(max_length=100, blank=True)
    subject1 = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, related_name="subject1")
    subject2 = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, related_name="subject2")
    subject3 = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, related_name="subject3")

    def __str__(self):
        return f"{self.name} | Experience - {self.experience} | Location - {self.location} | Classes - {self.classes} "
