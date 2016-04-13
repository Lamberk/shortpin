from django.db import models


class Key(models.Model):

    STATES = (
        ('granted', 'granted'),
        ('repaid', 'repaid'),
    )

    id = models.CharField(primary_key=True, max_length=4)
    status = models.CharField(max_length=15, choices=STATES, default='prog')

    def __unicode__(self):
        return '%s' % (
            self.id
        )
