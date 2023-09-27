from django.db import models


class Usuario(models.Model):
    GENDER_CHOICE = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
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

    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT,
                              related_name='autor')
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=255)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES,
                              null=False, blank=False,
                              default=STATUS_CHOICES[0][1])
    created_at = models.DateTimeField(auto_now_add=True)
