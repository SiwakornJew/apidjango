# Generated by Django 3.2.9 on 2021-12-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopPet', '0002_alter_shoppet_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppet',
            name='img',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shoppet',
            name='prize',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
