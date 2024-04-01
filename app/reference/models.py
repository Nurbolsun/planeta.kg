from django.db import models
from ckeditor.fields import RichTextField


class AbstractClass(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name='Имя на русском')
    name_ky = models.CharField(max_length=100, verbose_name='Имя на кыргызском')
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


class Image(models.Model):
    image = models.ImageField(upload_to="images/ref", null=True, blank=True, verbose_name="Фото")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images', verbose_name="Категория")

    is_main = models.BooleanField(default=True)

    def __str__(self):
        return "Фотографии"

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


class RefCarFuelType(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Топливо"
        verbose_name_plural = "Топливы"


class RefCarGearBoxType(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Коробка передатчик"
        verbose_name_plural = "Коробка передатчик"


class RefCarSteeringWheelType(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Руль"
        verbose_name_plural = "Рулей"


class RefCarWheelDriveType(AbstractClass):

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Привод"
        verbose_name_plural = "Приводы"


class RefCarModel(AbstractClass):
    mark_id = models.ForeignKey(RefCarMark, on_delete=models.CASCADE, verbose_name="Марка ID")
    year = models.DateTimeField(verbose_name="Год выпуска")
    fuel = models.ForeignKey(RefCarFuelType, on_delete=models.CASCADE, verbose_name="Тип топливо")
    gearbox = models.ForeignKey(RefCarGearBoxType, on_delete=models.CASCADE, verbose_name="Коробка передатчик")
    steering_wheel = models.ForeignKey(RefCarSteeringWheelType, on_delete=models.CASCADE, verbose_name="Руль")
    engine_size = models.CharField(max_length=10, verbose_name="Обьем двигателя")
    wheel_drive = models.ForeignKey(RefCarWheelDriveType, on_delete=models.CASCADE, verbose_name="Привод")

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Модель машина"
        verbose_name_plural = "Модели машины"


class Product(AbstractClass):
    code = models.CharField(max_length=100, verbose_name="Код машины")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    car_model_id = models.ManyToManyField(RefCarModel, verbose_name='Модель машины')
    additional_ru = RichTextField(verbose_name="Информации RU")
    additional_ky = RichTextField(verbose_name="Информации KG")
    image_id = models.ManyToManyField(Image, verbose_name='Фото продукт')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Продукт / запчасть"
        verbose_name_plural = "Запчасты"

