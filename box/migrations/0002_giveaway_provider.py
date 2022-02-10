# Generated by Django 3.2.8 on 2021-10-30 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20211030_1235'),
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giveaway',
            name='provider',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.provider'),
            preserve_default=False,
        ),
    ]