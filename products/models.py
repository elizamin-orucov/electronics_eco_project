from django.db import models
from services.mixin import DateMixin
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from services.uploader import Uploader
from services.choices import year_choice
from services.slugify import slugify
from services.generator import CodeGenerator


class ContactUs(DateMixin):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact us"


class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = RichTextField()
    order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "FAQ"
        verbose_name = "question"


class Category(DateMixin, MPTTModel):
    name = models.CharField(max_length=150, unique=True)
    icon = models.ImageField(upload_to=Uploader.category_uploader, blank=True, null=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Brand(DateMixin):
    brand = models.CharField(max_length=150)
    logo = models.ImageField(Uploader.brand_logo_uploader)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.brand


class Color(DateMixin):
    color = ColorField()

    def __str__(self):
        return self.color


class Product(DateMixin):
    name = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ManyToManyField(Color, blank=True)
    description = RichTextField()
    code = models.SlugField(unique=True, editable=False)
    slug = models.SlugField(unique=True, editable=False)
    dimension = models.CharField(max_length=150)
    weight = models.FloatField()
    price = models.FloatField()
    discount_interest = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(choices=year_choice())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.code = CodeGenerator().create_product_shortcode(size=8, model_=self.__class__)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"


class ProductImage(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.product_image_uploader)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = "Images"
        verbose_name = "Image"







