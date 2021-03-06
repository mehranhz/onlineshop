# Generated by Django 3.1.4 on 2020-12-20 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipment', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.address'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.agent'),
        ),
    ]
