# Generated by Django 4.2.7 on 2023-12-04 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_conent_messages_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
