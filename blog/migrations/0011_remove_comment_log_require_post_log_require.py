# Generated by Django 4.2.9 on 2024-03-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_log_require'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='log_require',
        ),
        migrations.AddField(
            model_name='post',
            name='log_require',
            field=models.BooleanField(default=False),
        ),
    ]
