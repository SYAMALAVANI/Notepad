# Generated by Django 4.2.3 on 2023-08-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_due_date_note_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
