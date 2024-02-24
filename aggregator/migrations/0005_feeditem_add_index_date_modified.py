# Generated by Django 3.2.25 on 2024-04-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0004_add_local_django_community'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='feeditem',
            index=models.Index(fields=['-date_modified'], name='aggregator__date_mo_d6dfa1_idx'),
        ),
    ]