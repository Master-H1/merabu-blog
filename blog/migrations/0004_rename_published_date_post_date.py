# Generated by Django 3.2.12 on 2023-10-07 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231007_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='date',
        ),
    ]
