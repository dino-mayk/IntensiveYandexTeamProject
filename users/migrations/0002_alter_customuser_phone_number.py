# Generated by Django 3.2.16 on 2022-12-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=17, verbose_name='Номер телефона'),
        ),
    ]