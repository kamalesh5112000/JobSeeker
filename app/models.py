from django.db import models
from django.utils.text import slugify

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)


class Auther(models.Model):
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)


class Location(models.Model):
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    zip=models.CharField(max_length=50)


class JobPost(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)
    salary=models.IntegerField()
    slug=models.SlugField(null=True,unique=True)
    location=models.OneToOneField(Location,on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(Auther,on_delete=models.CASCADE,null=True)
    user=models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug=slugify(self.title)
        return super(JobPost,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

        
    
     
 
    #  class Meta:
    #      verbose_name = _("JobPost")
    #      verbose_name_plural = _("JobPosts")
 
    #  def __str__(self):
    #      return self.name
 
    #  def get_absolute_url(self):
    #      return reverse("JobPost_detail", kwargs={"pk": self.pk})
 