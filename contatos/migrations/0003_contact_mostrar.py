# Generated by Django 3.2.3 on 2021-07-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contact_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
