from django.db import models


class Weapon(models.Model):
    STATUSES = {
        "old": "Old",
        "new": "New",
        "broken": "Broken",
        "repaired": "Repaired",
    }
    name = models.CharField(max_length=100, primary_key=True)
    status = models.CharField(max_length=100, choices=STATUSES.items())
    age = models.IntegerField()
    place = models.ForeignKey("Place", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name
