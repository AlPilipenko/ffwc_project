# Generated by Django 4.0.4 on 2022-05-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffwc_app', '0006_alter_user_data_weight_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='weight_update',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]