<<<<<<< HEAD
# Generated by Django 3.1.1 on 2020-10-16 10:42
=======
<<<<<<< HEAD
# Generated by Django 3.1.1 on 2020-10-25 08:34

from django.db import migrations, models
=======
# Generated by Django 3.1.1 on 2020-10-05 10:41
>>>>>>> 020a4c814ae2449d0d76c08409f853a7e2eb467c

from django.db import migrations, models
import django.utils.timezone
>>>>>>> 5a10d5e265417f4264e06c140637426d53e0ba80


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        ('auth', '0012_alter_user_first_name_max_length'),
>>>>>>> 5a10d5e265417f4264e06c140637426d53e0ba80
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(default='Mobile', max_length=13)),
                ('status', models.CharField(choices=[('1', 'New Client'), ('2', 'Client In Progress'), ('3', 'Client Processed')], default='1', max_length=9)),
            ],
=======
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('mobile', models.CharField(default='Mobile', max_length=13)),
                ('progress', models.CharField(choices=[('1', 'New Client'), ('2', 'Client In Progress'), ('3', 'Client Processed')], default='1', max_length=9)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
>>>>>>> 5a10d5e265417f4264e06c140637426d53e0ba80
        ),
    ]
