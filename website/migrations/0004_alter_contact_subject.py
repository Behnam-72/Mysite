# Generated by Django 4.2.9 on 2024-02-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]