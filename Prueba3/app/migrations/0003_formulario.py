# Generated by Django 4.0.5 on 2022-06-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('direccion', models.TextField()),
                ('tipo_pais', models.IntegerField(choices=[[0, 'Chile'], [1, 'Argentina'], [2, 'España']])),
                ('tipo_region', models.IntegerField(choices=[[0, 'Antofagasta'], [1, 'Valparaíso'], [2, 'Araucanía']])),
                ('tipo_flores', models.IntegerField(choices=[[0, 'Lilys'], [1, 'Girasoles'], [2, 'Rosas'], [3, 'Tulipanes'], [4, 'Jasmines'], [5, 'Gladiolas'], [6, 'Hibiscus'], [7, 'Violetas']])),
                ('tipo_especializacion', models.IntegerField(choices=[[0, 'Arbustos'], [1, 'Flores'], [2, 'Maceteros'], [3, 'Tierra de Hojas']])),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]
