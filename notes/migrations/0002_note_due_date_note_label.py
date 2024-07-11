# Generated by Django 4.2.3 on 2023-08-01 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 18, 22, 34, 198002)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('SE', 'secondary'), ('S', 'success'), ('D', 'danger'), ('W', 'warning'), ('I', 'info'), ('L', 'light'), ('D', 'dark')], default='P', max_length=2),
            preserve_default=False,
        ),
    ]
