# Generated by Django 3.2 on 2022-07-23 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.CharField(choices=[('Starter', 'starter'), ('Main', 'main'), ('Dessert', 'dessert')], max_length=10),
        ),
    ]