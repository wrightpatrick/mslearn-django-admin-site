# Generated by Django 3.1.6 on 2021-02-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0002_auto_20210209_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='adoption_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
