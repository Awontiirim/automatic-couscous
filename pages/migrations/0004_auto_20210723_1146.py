# Generated by Django 3.1 on 2021-07-23 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_createscribe_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createscribe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.customuser'),
        ),
    ]