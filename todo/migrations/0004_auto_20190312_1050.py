# Generated by Django 2.1.5 on 2019-03-12 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20190312_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='tasktime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]