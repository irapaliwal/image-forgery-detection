# Generated by Django 3.0.3 on 2021-02-10 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forgerydetection', '0005_subscriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptions',
            old_name='haflyear',
            new_name='halfyear',
        ),
    ]
