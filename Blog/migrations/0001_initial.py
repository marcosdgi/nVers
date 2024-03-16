# Generated by Django 5.0.1 on 2024-03-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sender_mail', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Mails',
            },
        ),
    ]