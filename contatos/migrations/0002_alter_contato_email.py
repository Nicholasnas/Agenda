# Generated by Django 4.1.1 on 2022-10-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
