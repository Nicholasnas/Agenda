# Generated by Django 4.1.1 on 2022-10-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_alter_contato_sobrenome'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
