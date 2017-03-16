from django.db import models


class Quarter(models.Model):
    state = models.CharField(max_length=14)
    year_issued = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.state, self.year_issued)