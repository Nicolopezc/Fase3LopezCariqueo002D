# Generated by Django 3.1.2 on 2020-10-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0011_auto_20201024_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=50)),
                ('visita', models.CharField(max_length=50)),
                ('estadio', models.CharField(max_length=100)),
                ('fecha_partido', models.DateField(blank=True, null=True)),
                ('competicion', models.CharField(max_length=100)),
            ],
        ),
    ]
