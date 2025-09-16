from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('family', 'Family'),
    ]

    photo = models.ImageField(upload_to='students_photos/', blank=True, null=True)
    Name = models.CharField(max_length=100, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    description = models.TextField(blank=True)
    price_per_night = models.PositiveIntegerField()
    adults =  models.PositiveIntegerField(default=True)
    child = models.PositiveIntegerField(default=True)
    room_num = models.PositiveIntegerField(default=True)
    # is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.Name} ({self.get_room_type_display()})"
