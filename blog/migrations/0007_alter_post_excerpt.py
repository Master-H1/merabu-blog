# Generated by Django 3.2.12 on 2023-10-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_excerpt_post_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=150),
        ),
    ]
