# Generated by Django 4.0.3 on 2022-03-11 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]