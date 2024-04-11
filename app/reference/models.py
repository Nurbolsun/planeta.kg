from django.db import models
from ckeditor.fields import RichTextField
import datetime


class AbstractClass(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name='Имя на русском', blank=False)
    # name_ky = models.CharField(max_length=100, verbose_name='Имя на кыргызском', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновление")
    is_active = models.BooleanField(verbose_name="Активный", default=True)

    class Meta:
        abstract = True


class Category(AbstractClass):
    parentCategory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name="Имя категории")
    image = models.ImageField(upload_to="images/category", null=True, blank=True, verbose_name="Фото категории")

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории запчастей"


class PartImage(models.Model):
    image = models.ImageField(upload_to="images/part_images", verbose_name="Изображение")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии моделей"


class RefCarMark(AbstractClass):
    emblems = models.ImageField(upload_to="images/emblems", null=True, blank=True, verbose_name="Эмблема машин")

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Марка машина"
        verbose_name_plural = "Марки машины"


class RefCarFuel(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Топливо"
        verbose_name_plural = "Топливы"


class RefCarGearBox(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Коробка передатчик"
        verbose_name_plural = "Коробка передатчик"


class RefCarSteeringWheel(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Руль"
        verbose_name_plural = "Рулей"


class RefCarWheelDrive(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Привод"
        verbose_name_plural = "Приводы"


class RefCarBody(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Тип кузовы"


def year_choices():
    return [(r, r) for r in range(1990, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year


class RefCarModel(AbstractClass):
    mark_id = models.ForeignKey(RefCarMark, on_delete=models.CASCADE, verbose_name="Марка ID")
    year = models.IntegerField(choices=year_choices, default=current_year, verbose_name="Год выпуска")
    fuel = models.ForeignKey(RefCarFuel, on_delete=models.CASCADE, verbose_name="Тип двигателя")
    gearbox = models.ForeignKey(RefCarGearBox, on_delete=models.CASCADE, verbose_name="Коробка передач")
    car_body = models.ForeignKey(RefCarBody, on_delete=models.CASCADE, verbose_name="Тип кузова")
    steering_wheel = models.ForeignKey(RefCarSteeringWheel, on_delete=models.CASCADE, verbose_name="Руль")
    engine_size = models.CharField(max_length=10, verbose_name="Объем двигателя")
    wheel_drive = models.ForeignKey(RefCarWheelDrive, on_delete=models.CASCADE, verbose_name="Привод")

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Модель машина"
        verbose_name_plural = "Модели машины"


class Part(AbstractClass):
    code = models.CharField(max_length=100, verbose_name="Код машины", blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    car_model_id = models.ManyToManyField(RefCarModel, verbose_name='Модель машины', blank=True)
    additional_ru = RichTextField(verbose_name="Информации RU", blank=True)
    price = models.IntegerField(verbose_name="Цена")
    location = models.TextField(verbose_name="Город", default="Бишкек")
    # additional_ky = RichTextField(verbose_name="Информации KG", blank=True, null=True)
    images = models.ManyToManyField(PartImage, related_name='parts', verbose_name='Фото продукт')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Продукт / запчасть"
        verbose_name_plural = "Запчасти"

