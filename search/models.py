from django.db import models

class Preference(models.Model):
    HEADPHONE_QUALITIES = {
        "AU": "Audio",
        "MC": "Microphone"
    }
    STARS = {
        "1": "1",
        "2": "2",
        "3": "3"
    }

    quality = models.CharField(max_length=20, choices=HEADPHONE_QUALITIES)
    rating = models.CharField(max_length=20, default='1', choices=STARS)

    def __str__(self):
        return self.quality