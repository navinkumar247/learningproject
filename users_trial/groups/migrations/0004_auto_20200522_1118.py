# Generated by Django 3.0.3 on 2020-05-22 05:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_groupowner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupowner',
            old_name='owner',
            new_name='owner_group',
        ),
        migrations.AlterUniqueTogether(
            name='groupowner',
            unique_together={('user', 'owner_group')},
        ),
    ]