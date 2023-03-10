# Generated by Django 4.1.7 on 2023-03-14 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_delete_propertyavailability'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('price', models.FloatField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='property',
            name='name',
        ),
        migrations.RemoveField(
            model_name='property',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='property',
            name='province',
        ),
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='lowest_avail_price',
            field=models.FloatField(blank=True, default=1000000000000),
        ),
        migrations.AddField(
            model_name='property',
            name='num_of_beds',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='property_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_of_guests',
            field=models.IntegerField(blank=True),
        ),
        migrations.DeleteModel(
            name='Amenity',
        ),
        migrations.AddField(
            model_name='propertyavailability',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property'),
        ),
    ]
