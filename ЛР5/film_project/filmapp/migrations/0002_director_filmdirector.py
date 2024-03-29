# Generated by Django 4.0 on 2022-04-11 15:58

from django.db import migrations, models
import django.db.models.deletion
import filmapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField(null=True, validators=[filmapp.models.validate_positive])),
            ],
        ),
        migrations.CreateModel(
            name='FilmDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filmapp.director')),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filmapp.film')),
            ],
        ),
    ]
