# Generated by Django 3.2.16 on 2022-12-22 07:26

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('is_shelter', models.BooleanField(choices=[(False, 'Пользователь'), (True, 'Приют')], default=False, verbose_name='Приют или посетитель')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть введен в формате: "+999999999".Допускается до 15 цифр.', regex='^\\+?1?\\d{9,15}$')], verbose_name='Номер телефона')),
                ('address', models.CharField(default='ваш адресс', max_length=100, verbose_name='адрес приюта')),
                ('about', models.TextField(default='ваша информация о приюте', verbose_name='О приюте')),
                ('avatar', models.ImageField(default='default_avatar.jpg', help_text='загрузите картинку', upload_to='uploads/avatars/%Y/%m', verbose_name='Аватар')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
