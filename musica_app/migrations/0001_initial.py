# Generated by Django 4.1 on 2022-10-03 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('instrumento_principal', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_lanzamiento', models.DateField()),
                ('estrellas', models.IntegerField()),
                ('musico_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica_app.musico')),
            ],
        ),
    ]
