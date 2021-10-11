from django.db import models


class Pizza(models.Model):
    """Model definition for Pizza."""

    nome = models.CharField(max_length=120)
    ingredientes = models.TextField()

    def __str__(self):
        """Unicode representation of Pizza."""
        return self.nome


