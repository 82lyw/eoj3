# Generated by Django 2.2.6 on 2019-11-27 10:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backstage', '0008_auto_20190315_1134'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='emailrecipient',
            unique_together={('user', 'email')},
        ),
    ]
