# Generated by Django 5.0.4 on 2024-04-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('cognom', models.CharField(max_length=100)),
                ('edat', models.IntegerField()),
                ('rol', models.CharField(choices=[('estudiant', 'Estudiante'), ('professor', 'Profesor')], max_length=50)),
                ('curs', models.CharField(choices=[('DAW1', 'DAW1'), ('DAW2', 'DAW2'), ('DAM1', 'DAM1'), ('DAM2', 'DAM2'), ('ASIX1', 'ASIX1'), ('ASIX2', 'ASIX2')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('cognom', models.CharField(max_length=100)),
                ('edat', models.IntegerField()),
                ('rol', models.CharField(choices=[('estudiant', 'Estudiante'), ('professor', 'Profesor')], max_length=50)),
            ],
        ),
    ]