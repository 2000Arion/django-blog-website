from django.db import models
from django.contrib.auth.models import User
import markdown2

# Create your models here.

STATUS = ((0, "Entwurf"), (1, "Veröffentlicht"))

class Post(models.Model):
    Titel = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    Autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    Erstellt = models.DateTimeField(auto_now_add=True)
    Aktualisiert = models.DateTimeField(auto_now=True)
    Inhalt = models.TextField()
    Status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-Erstellt"]
        
    def get_markdown_content(self):
        return markdown2.markdown(self.Inhalt)
    
    def __str__(self):
        return self.Titel
    

