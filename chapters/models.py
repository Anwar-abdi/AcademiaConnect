from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def validate_registration_number(value):
    # Add your specific validation logic here
    if not value.startswith('UCU/'):
        raise ValidationError('Registration number must start with UCU/')

class Student(models.Model):
    COURSE_CHOICES = [
        ('BCS', 'Bachelor of Computer Science'),
        ('BIT', 'Bachelor of Information Technology'),
        ('BSE', 'Bachelor of Software Engineering'),
        ('BIS', 'Bachelor of Information Systems'),
    ]

    registration_number = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex='^UCU/\d{4}/\d{3}$',
                message='Registration number must be in format UCU/YYYY/XXX'
            ),
            validate_registration_number
        ]
    )
    access_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    student_id_scan = models.ImageField(upload_to='student_ids/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.registration_number}"

class Chapter(models.Model):
    CHAPTER_CHOICES = [
        ('CS', 'Cyber Security'),
        ('AR', 'AI & Robotics'),
        ('SE', 'Software Engineering'),
        ('GM', 'Gaming'),
    ]

    name = models.CharField(max_length=2, choices=CHAPTER_CHOICES, unique=True)
    description = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.get_name_display()

class ChapterRegistration(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    rejection_reason = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'chapter')

    def __str__(self):
        return f"{self.student} - {self.chapter}"
