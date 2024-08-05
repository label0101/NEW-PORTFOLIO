# Generated by Django 5.0.7 on 2024-08-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='Images/gallery_category')),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
