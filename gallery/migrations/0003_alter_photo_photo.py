# Generated by Django 4.2 on 2023-04-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0002_photo_deleted_at_photo_is_deleted_photo_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="photo",
            field=models.ImageField(upload_to="user_pic", verbose_name="Фото"),
        ),
    ]
