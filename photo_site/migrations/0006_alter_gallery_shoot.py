# Generated by Django 4.2 on 2023-04-13 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_site', '0005_delete_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='shoot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photo_site.shoot'),
        ),
    ]