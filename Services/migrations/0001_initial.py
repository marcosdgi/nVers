# Generated by Django 5.0.1 on 2024-03-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
