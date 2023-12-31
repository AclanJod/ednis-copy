# Generated by Django 4.2.4 on 2023-10-11 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0012_remove_mortalityform_sire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('vaccine', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('dosage', models.CharField(max_length=255)),
                ('pig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccines', to='Authentication.pig')),
            ],
        ),
    ]
