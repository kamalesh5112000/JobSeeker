from django.db import models

# Create your models here.

class JobPost(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    salary=models.IntegerField()

    def __str__(self):
        return self.title
        
    
     
 
    #  class Meta:
    #      verbose_name = _("JobPost")
    #      verbose_name_plural = _("JobPosts")
 
    #  def __str__(self):
    #      return self.name
 
    #  def get_absolute_url(self):
    #      return reverse("JobPost_detail", kwargs={"pk": self.pk})
 