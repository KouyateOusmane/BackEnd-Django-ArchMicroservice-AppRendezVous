from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password

class ClientManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class Client(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    username = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    adresse = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ClientManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nom', 'prenom', 'telephone', 'adresse']

    class Meta:
        db_table = 'clients'

    def save(self, *args, **kwargs):
        if not self.pk or (Client.objects.filter(pk=self.pk).exists() and Client.objects.get(pk=self.pk).password != self.password):
            self.password = make_password(self.password)
        super(Client, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save(update_fields=["password"])
class Prestataire(models.Model):
    idPrestataire = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=255)
    username = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    description= models.TextField()
    class Meta:
        db_table = 'prestataires'


class Service(models.Model):
    idService = models.AutoField(primary_key=True)
    idPrestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    duree = models.IntegerField()
    categorie = models.CharField(max_length=255)
    class Meta:
        db_table = 'services'

class Demande(models.Model):
    idDemande = models.AutoField(primary_key=True)
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    idPrestataire = models.ForeignKey(Prestataire, on_delete=models.CASCADE)
    idService = models.ForeignKey(Service, on_delete=models.CASCADE)
    numeroDemande = models.CharField(max_length=255)
    dateDemande = models.DateField()
    statut = models.CharField(max_length=255)
    class Meta:
        db_table = 'demandes'

class Evaluation(models.Model):
    idEvaluation = models.AutoField(primary_key=True)
    idDemande = models.ForeignKey(Demande, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    class Meta:
        db_table = 'evaluations'