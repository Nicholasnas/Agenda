# Generated by Django 4.1.1 on 2022-11-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0006_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]