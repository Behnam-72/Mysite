# Generated by Django 4.2.9 on 2024-02-13 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['published_date']},
        ),
    ]