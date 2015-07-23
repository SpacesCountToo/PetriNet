from django.db import models
import uuid
# Create your models here.

class Unit(models.Model):
    uuid_name = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False)
    human_readable_name = models.CharField(max_length=50, unique=True)
    form = 'O'
    transform = 'L'
    shape_choices = (
        (form, 'Form'),
        (transform,'Transform')
    )
    shape = models.CharField(max_length=1,
                             choices=shape_choices)
    relative_x_position = models.IntegerField()
    relative_y_position = models.IntegerField()
    parent_unit = models.ForeignKey('self', blank=True, null=True)
    def __unicode__(self):
        return self.human_readable_name

class Connection(models.Model):
    source = models.ForeignKey(Unit,related_name='src')
    destination = models.ForeignKey(Unit,related_name='dest')
    def __unicode__(self):
        return '%s to %s' % (self.source, self.destination)
