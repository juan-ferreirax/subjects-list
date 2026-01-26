from django.db import models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    if TYPE_CHECKING:
        subject_set: "RelatedManager[Subject]"

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text
    
class Subject(models.Model):
    """Assunto específico sobre um determinado tópico/tema."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "subjects"

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text[:50] + "..."
