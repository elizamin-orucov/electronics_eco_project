# Generated by Django 4.2.7 on 2023-11-29 16:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', ckeditor.fields.RichTextField()),
                ('order', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'FAQ',
            },
        ),
    ]
