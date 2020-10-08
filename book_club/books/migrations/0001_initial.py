# Generated by Django 3.1.1 on 2020-09-29 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('date_of_birth', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('description', models.TextField(blank=True, verbose_name='Об авторе')),
                ('image', models.ImageField(blank=True, upload_to='authors/', verbose_name='Аватарка')),
            ],
            options={
                'verbose_name': 'Авторы и переводчики',
                'verbose_name_plural': 'Авторы и переводчики',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('tagline', models.CharField(blank=True, max_length=80, null=True, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='О книге')),
                ('cover', models.ImageField(upload_to='books/', verbose_name='Обложка')),
                ('year_of_writing', models.PositiveSmallIntegerField(blank=True, default=2020, verbose_name='Год написания')),
                ('year_of_publishing', models.PositiveSmallIntegerField(default=2020, verbose_name='Год издания')),
                ('date_receipt', models.DateField(default=datetime.date.today, verbose_name='Дата поступления')),
                ('isbn', models.IntegerField(blank=True, help_text='Международный стандартный номер книги ISBN (EAN)', null=True, verbose_name='Номер книги')),
                ('signs', models.FloatField(blank=True, help_text='Количество знаков (тысяч)', null=True, verbose_name='Знаков')),
                ('pages', models.PositiveSmallIntegerField(verbose_name='Количество страниц')),
                ('age', models.CharField(choices=[('0+', '0+'), ('6+', '6+'), ('12+', '12+'), ('14+', '14+'), ('16+', '16+'), ('18+', '18+')], default='0+', max_length=3, verbose_name='Возрастной ценз')),
                ('url', models.SlugField(max_length=120, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Категория')),
                ('description', models.CharField(max_length=300, verbose_name='Описание категории')),
                ('url', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Об издателе')),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звёзды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Подборка')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=10000, verbose_name='Сообщение')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Книга')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='BookExcerpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Отрывок из книги',
                'verbose_name_plural': 'Отрывки из книги',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='books.Genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='book',
            name='illustrator',
            field=models.ManyToManyField(blank=True, related_name='book_illustrator', to='books.Author', verbose_name='Иллюстратор'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(related_name='book_publisher', to='books.Publisher', verbose_name='Издательство'),
        ),
        migrations.AddField(
            model_name='book',
            name='topics',
            field=models.ManyToManyField(blank=True, to='books.Topic', verbose_name='Темы'),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(blank=True, related_name='book_translator', to='books.Author', verbose_name='Переводчик'),
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.ManyToManyField(related_name='book_writer', to='books.Author', verbose_name='Писатель'),
        ),
    ]