# Generated by Django 4.1.1 on 2022-09-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0007_alter_flyingsite_wind_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyingsite',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
