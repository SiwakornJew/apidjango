# Generated by Django 3.2.9 on 2021-12-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodCat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcat',
            name='img',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
