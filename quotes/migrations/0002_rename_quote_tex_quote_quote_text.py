# Generated by Django 5.2.3 on 2025-07-24 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quote_tex',
            new_name='quote_text',
        ),
    ]
