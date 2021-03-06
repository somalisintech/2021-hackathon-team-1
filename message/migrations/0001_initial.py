# Generated by Django 3.2.8 on 2021-10-30 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=160)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sent_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.serviceuser')),
            ],
        ),
    ]
