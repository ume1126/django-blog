# Generated by Django 2.0.6 on 2018-10-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='live',
            field=models.BooleanField(default=False),
        ),
    ]
