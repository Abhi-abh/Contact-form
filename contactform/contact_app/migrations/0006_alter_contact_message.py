# Generated by Django 5.1.6 on 2025-02-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0005_alter_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
