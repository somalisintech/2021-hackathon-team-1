# Generated by Django 3.2.8 on 2021-10-30 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20211030_1235'),
        ('box', '0002_giveaway_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='given_to',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='user.serviceuser'),
            preserve_default=False,
        ),
    ]
