# Generated by Django 4.2.4 on 2023-10-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0008_alter_sow_pig_id_pigsales'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedsInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeds_brand', models.CharField(max_length=255)),
                ('feeds_ration', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('verified_by', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='PigSales',
        ),
    ]