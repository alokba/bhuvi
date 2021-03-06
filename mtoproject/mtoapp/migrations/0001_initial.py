# Generated by Django 3.0.4 on 2020-03-17 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('fee', models.FloatField(max_length=50)),
                ('book', models.CharField(max_length=50)),
                ('abc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtoapp.Student')),
            ],
        ),
    ]
