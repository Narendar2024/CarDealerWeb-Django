# Generated by Django 4.2.7 on 2023-11-17 11:49

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=48, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('WY', 'Wyoming')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], verbose_name='year'),
        ),
    ]