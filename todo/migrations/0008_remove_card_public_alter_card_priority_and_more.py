# Generated by Django 4.2.5 on 2023-09-28 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_card_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='public',
        ),
        migrations.AlterField(
            model_name='card',
            name='priority',
            field=models.CharField(choices=[('1', 'Baixa'), ('2', 'Média'), ('3', 'Alta')], default=('1', 'Baixa'), max_length=1),
        ),
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('todo', 'To do'), ('inprogress', 'In progress'), ('done', 'Done')], default=('todo', 'To do'), max_length=11),
        ),
    ]
