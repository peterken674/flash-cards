# Generated by Django 3.0 on 2021-07-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
