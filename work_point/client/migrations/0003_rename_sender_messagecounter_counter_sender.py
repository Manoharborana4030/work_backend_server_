# Generated by Django 4.0.3 on 2022-04-25 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_messagecounter_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagecounter',
            old_name='sender',
            new_name='counter_sender',
        ),
    ]