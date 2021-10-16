# Generated by Django 3.2.7 on 2021-10-16 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('lastname', models.CharField(max_length=30, verbose_name='Last name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('author', models.CharField(max_length=90, verbose_name='Author')),
                ('language', models.CharField(max_length=30, verbose_name='Language')),
                ('year', models.DateField(verbose_name='Year')),
                ('publisher', models.CharField(max_length=30, verbose_name='Publisher')),
                ('genre', models.CharField(max_length=60, verbose_name='Genre')),
                ('number', models.IntegerField(default=1, verbose_name='Version')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('institution', models.CharField(max_length=60, verbose_name='Institution')),
                ('address', models.CharField(max_length=30, verbose_name='Address')),
                ('telephone', models.CharField(max_length=30, verbose_name='Telephone')),
                ('role_choose', models.CharField(choices=[('Administrador', 'Administrador'), ('Bibliotecario', 'Bibliotecario'), ('Estudiante', 'Estudiante')], max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_borrow', models.DateField()),
                ('date_agreed', models.DateField()),
                ('date_return', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.book')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.register')),
            ],
        ),
    ]
