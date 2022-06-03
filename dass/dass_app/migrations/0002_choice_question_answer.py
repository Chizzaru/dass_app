# Generated by Django 4.0.4 on 2022-06-01 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dass_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_answered', models.DateTimeField(verbose_name='date answered')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dass_app.choice')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dass_app.users')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dass_app.question')),
            ],
        ),
    ]