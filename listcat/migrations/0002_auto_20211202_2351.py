# Generated by Django 3.2.9 on 2021-12-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listcat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listcats',
            name='des',
        ),
        migrations.AlterField(
            model_name='listcats',
            name='img',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listcats',
            name='prize',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
