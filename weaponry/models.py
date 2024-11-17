from django.db import models
import random


class Weapon(models.Model):
    STATUSES = {
        "old": "Old",
        "new": "New",
        "broken": "Broken",
        "repaired": "Repaired",
    }
    name = models.CharField(max_length=100, default="new", primary_key=True)
    status = models.CharField(max_length=100, choices=STATUSES.items())
    age = models.IntegerField()
    price = models.FloatField(default=100)
    place = models.ForeignKey("Place", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def repair(self):
        self.status = "repaired"
        self.age = 0
        self.save()


class Place(models.Model):
    UTILITIES = {
        "repair": "Repair",
        "sell": "Sell",
        "No utility": "No utility",
        "earn new weapons": "Earn new weapons",
    }
    name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(default="No description")
    earnings = models.FloatField(default=0)
    utility = models.CharField(
        max_length=100, default="No utility", choices=UTILITIES.items())

    def __str__(self):
        return self.name

    def use_facility(self, weapons):
        if self.utility == "repair":
            for weapon in weapons:
                if weapon.status == "broken" and weapon.place.utility == "repair":
                    self.earnings -= random.randint(0, weapon.age*2)
                    weapon.repair()
        if self.utility == "sell":
            for weapon in weapons:
                if weapon.place.utility == "sell":
                    self.earnings += weapon.price - weapon.age * 5
                    weapon.delete()
        if self.utility == "earn new weapons":
            if len(weapons) == 0:
                self.earnings -= 5000
                new_weapon = Weapon(
                    "SUPER:" + str(random.randint(0, 1000)), "new", random.randint(0, 100), random.randint(10, 1000), self)
                new_weapon.save()
                return
            self.earnings -= 500
            for weapon in weapons:
                if weapon.place.utility == "earn new weapons":
                    rand = random.randint(0, weapon.price)
                    if rand < 50 + weapon.age or weapon.status == "broken":
                        weapon.status = "broken"
                        self.earnings -= weapon.age
                        weapon.save()
                    else:
                        new_weapon = Weapon(
                            "SUPER:" + str(random.randint(0, 1000)), "new", random.randint(0, 100), random.randint(10, 1000), self)
                        new_weapon.save()
        self.save()
