from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date",
        help_text="",
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date",
        help_text="",
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text="This is variable of the setting.",
    )
    description = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text="",
    )
    parameter = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Parameter",
        help_text="",
    )

    def __str__(self):
        return f"General Setting: {self.name}"

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering = ("id",)


class ImageSetting(AbstractModel):
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text="This is variable of the setting.",
    )
    description = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text="",
    )
    file = models.ImageField(
        default="",
        verbose_name="Image",
        help_text="",
        blank=True,
        upload_to="images"
    )

    def __str__(self):
        return f"Image Setting: {self.name}"

    class Meta:
        verbose_name = "Image Setting"
        verbose_name_plural = "Image Settings"
        ordering = ("id",)
class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text="This is variable of the setting.",
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name="Percentage",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    def __str__(self):
        return f"Skill: {self.name}"

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ("order",)
class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    link = models.URLField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Link",
    )
    icon = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Icon",
    )
    def __str__(self):
        return f"Social Media: {self.link}"

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"
        ordering = ("order",)