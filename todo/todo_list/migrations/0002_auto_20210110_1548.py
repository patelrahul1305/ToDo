# Generated by Django 3.0.8 on 2021-01-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
