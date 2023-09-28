from datetime import timezone
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Usuario(models.Model):
    GENDER_CHOICE = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Prefiro não informar')
    ]
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, blank=False)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username


class Card(models.Model):
    STATUS_CHOICES = [('todo', 'To do'),
                      ('inprogress', 'In progress'),
                      ('done', 'Done')]
    PRIORITY_CHOICES = [('1', 'Baixa'),
                        ('2', 'Média'),
                        ('3', 'Alta')]

    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT,
                              related_name='cards_criados')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES,
                              null=False, blank=False,
                              default=STATUS_CHOICES[0])
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES,
                                default=PRIORITY_CHOICES[0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Adicione esta linha
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Card)
def update_completed_at(sender, instance, **kwargs):
    if instance.status == 'Done' and not instance.completed_at:
        instance.completed_at = timezone.now()
