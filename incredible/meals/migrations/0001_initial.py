# Generated by Django 4.2.4 on 2023-08-11 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname_text', models.CharField(max_length=200)),
                ('lname_text', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entree_choice_text', models.CharField(max_length=200)),
                ('restaurant_name_text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='Date dined')),
                ('eaten_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.user')),
            ],
        ),
    ]