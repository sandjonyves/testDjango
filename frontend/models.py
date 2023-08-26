from django.db import models


# Create your models here.
class DataReact(models.Model):
    name = models.CharField(max_length=200)
    ville = models.CharField(max_length=150)
    quartier = models.CharField(max_length=150)
    niveau = models.CharField(max_length=100)
    classe = models.CharField(max_length=200)
    matiere = models.CharField(max_length=300)
    jours =  models.CharField(max_length=300)
    heure = models.CharField(max_length=100)
    numTel=models.CharField(max_length= 150)
    addEmail= models.EmailField(max_length=250)
    addresse =models.CharField(max_length=250)
    taux = models.CharField(max_length=150)
    Price = models.CharField(max_length=50)
    class Meta:
        verbose_name = ("data")

    def __str__(self):
        return self.name

class DataEncadreur(models.Model):
    name = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    numTel=models.CharField(max_length= 15)
    addEmail= models.EmailField(max_length=250)
    untEnseignaement = models.CharField(max_length=250)

    def __str__(self):
        return self.name     