# Generated by Django 2.1.5 on 2019-01-12 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=3000, null=True)),
                ('depth', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('visited', models.DateTimeField(null=True)),
                ('content_type', models.CharField(max_length=128, null=True)),
                ('crawl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='crawlapp.Crawl')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='crawlapp.Url')),
            ],
        ),
    ]