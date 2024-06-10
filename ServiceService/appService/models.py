from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    courriel = models.EmailField(max_length=255)
    motDePasse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    adresse = models.TextField()
    class Meta:
        db_table = 'client'

class Prestataire(models.Model):
    idPrestataire = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=255)
    courriel = models.EmailField(max_length=255)
    motDePasse = models.CharField(max_length=255)
    description= models.TextField()
    class Meta:
        db_table = 'prestataire'


class Service(models.Model):
    idService = models.AutoField(primary_key=True)
    idPrestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    duree = models.IntegerField()
    categorie = models.CharField(max_length=255)
    class Meta:
        db_table = 'service'

class Demande(models.Model):
    idDemande = models.AutoField(primary_key=True)
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    idPrestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE)
    idService = models.ForeignKey(Service, on_delete=models.CASCADE)
    numeroDemande = models.CharField(max_length=255)
    dateDemande = models.DateField()
    statut = models.CharField(max_length=255)
    class Meta:
        db_table = 'demande'

class Evaluation(models.Model):
    idEvaluation = models.AutoField(primary_key=True)
    idDemande = models.ForeignKey(Demande, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    class Meta:
        db_table = 'evaluation'