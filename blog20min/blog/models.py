from django.db import models
from django.template.defaultfilters import slugify


class Entry(models.Model):
	
	title = models.CharField(max_length=200)
	content = models.TextField()
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Entry, self).save(*args, **kwargs)



