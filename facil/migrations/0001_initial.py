# Generated by Django 5.0.1 on 2024-02-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideArt', models.IntegerField()),
                ('nombreArt', models.CharField(max_length=67)),
                ('modeloArt', models.CharField(max_length=40)),
                ('stockArt', models.IntegerField()),
                ('precioArt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideArt', models.IntegerField()),
                ('fecha', models.DateField()),
                ('observacion', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideArt', models.IntegerField()),
                ('urlfile', models.CharField(max_length=240)),
            ],
        ),
    ]
