# Generated by Django 5.0.1 on 2024-02-29 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facil', '0007_remove_articulo_ideart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='ideUser',
        ),
    ]
