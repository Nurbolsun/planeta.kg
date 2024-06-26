# Generated by Django 5.0.3 on 2024-04-05 11:16

import app.reference.models
import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/part_images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии моделей',
            },
        ),
        migrations.CreateModel(
            name='RefCarFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Топливо',
                'verbose_name_plural': 'Топливы',
            },
        ),
        migrations.CreateModel(
            name='RefCarGearBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Коробка передатчик',
                'verbose_name_plural': 'Коробка передатчик',
            },
        ),
        migrations.CreateModel(
            name='RefCarMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('emblems', models.ImageField(blank=True, null=True, upload_to='images/emblems', verbose_name='Эмблема машин')),
            ],
            options={
                'verbose_name': 'Марка машина',
                'verbose_name_plural': 'Марки машины',
            },
        ),
        migrations.CreateModel(
            name='RefCarSteeringWheel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Руль',
                'verbose_name_plural': 'Рулей',
            },
        ),
        migrations.CreateModel(
            name='RefCarWheelDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Привод',
                'verbose_name_plural': 'Приводы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/category', verbose_name='Фото категории')),
                ('parentCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference.category', verbose_name='Имя категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории запчастей',
            },
        ),
        migrations.CreateModel(
            name='RefCarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('year', models.IntegerField(choices=app.reference.models.year_choices, default=app.reference.models.current_year, verbose_name='Год выпуска')),
                ('engine_size', models.CharField(max_length=10, verbose_name='Обьем двигателя')),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.refcarfuel', verbose_name='Тип топливо')),
                ('gearbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.refcargearbox', verbose_name='Коробка передатчик')),
                ('mark_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.refcarmark', verbose_name='Марка ID')),
                ('steering_wheel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.refcarsteeringwheel', verbose_name='Руль')),
                ('wheel_drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.refcarwheeldrive', verbose_name='Привод')),
            ],
            options={
                'verbose_name': 'Модель машина',
                'verbose_name_plural': 'Модели машины',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Имя на русском')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновление')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Код машины')),
                ('additional_ru', ckeditor.fields.RichTextField(blank=True, verbose_name='Информации RU')),
                ('additional_ky', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информации KG')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference.category', verbose_name='Категория')),
                ('images', models.ManyToManyField(related_name='parts', to='reference.partimage', verbose_name='Фото продукт')),
                ('car_model_id', models.ManyToManyField(blank=True, to='reference.refcarmodel', verbose_name='Модель машины')),
            ],
            options={
                'verbose_name': 'Продукт / запчасть',
                'verbose_name_plural': 'Запчасти',
            },
        ),
    ]
