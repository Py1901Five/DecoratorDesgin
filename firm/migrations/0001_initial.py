# Generated by Django 2.2.1 on 2019-05-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Potential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pricing', models.IntegerField()),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('text3', models.TextField()),
                ('text4', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('span', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('title', models.CharField(max_length=80)),
                ('price', models.CharField(max_length=50)),
                ('new_price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('image', models.TextField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('image', models.TextField()),
                ('profession', models.CharField(max_length=50)),
                ('addr', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('span', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=80)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('time', models.TextField()),
                ('message', models.TextField()),
                ('teamid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firm.Team')),
            ],
        ),
    ]
