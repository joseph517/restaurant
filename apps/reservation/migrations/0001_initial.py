# Generated by Django 4.0.4 on 2023-03-31 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id_reservacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_hora_inicio', models.DateTimeField()),
                ('fecha_hora_fin', models.DateTimeField()),
                ('numero_personas', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('id_mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.table')),
            ],
        ),
    ]
