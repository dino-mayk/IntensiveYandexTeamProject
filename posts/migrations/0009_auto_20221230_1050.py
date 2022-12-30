# Generated by Django 3.2.16 on 2022-12-30 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_posts_cat_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='age',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'до 1 года'), (2, 'от 1 до 2 лет'), (3, 'от 2 до 5 лет'), (4, 'от 5 до 8 лет'), (5, 'от 8-11 лет'), (6, 'свыше 11 лет')], default=100, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='cat_breed',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'породистый'), (2, 'без породы')], default=100, verbose_name='порода кошки'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='cat_color',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'белый'), (2, 'серый'), (3, 'рыжий'), (4, 'черный'), (5, 'черепаховый'), (6, 'трехцветный'), (7, 'бело-черный'), (8, 'бело-рыжий'), (9, 'бело-серый'), (10, 'рыже-черный')], default=100, verbose_name='цвет кошки'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='dog_color',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'белый'), (2, 'серый'), (3, 'рыжий'), (4, 'черный'), (5, 'черепаховый'), (6, 'трехцветный'), (7, 'бело-черный'), (8, 'бело-рыжий'), (9, 'бело-серый'), (10, 'рыже-черный')], default=100, verbose_name='цвет собаки'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'мужской'), (2, 'женский')], default=100, verbose_name='пол животного'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='health',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'без особенностей'), (2, 'с особенностями')], default=100, verbose_name='состояние здоровья'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='other_animal_type',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'хомяк'), (2, 'кролик'), (3, 'морская свинка'), (4, 'птицы'), (5, 'змеи')], default=100, verbose_name='тип животного'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='size',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'мелкий'), (2, 'средний'), (3, 'крупный')], default=100, verbose_name='размер животного'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='socialization',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'высокая'), (2, 'средняя'), (3, 'низкая')], default=100, verbose_name='уровень социализации'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='wool_type',
            field=models.PositiveSmallIntegerField(choices=[(100, '---'), (1, 'короткошерстная'), (3, 'среднешерстная'), (2, 'длинношерстная')], default=100, verbose_name='тип шерсти'),
        ),
        migrations.CreateModel(
            name='PostsGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(help_text='загрузите картинку', upload_to='uploads/gallery/%Y/%m', verbose_name='картинка')),
                ('item', models.ForeignKey(help_text='выберете питомца', on_delete=django.db.models.deletion.CASCADE, to='posts.posts', verbose_name='питомец')),
            ],
            options={
                'verbose_name': 'фотографию питомца',
                'verbose_name_plural': 'фотогалерея питомцев',
            },
        ),
    ]