from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성" # 저장되는 값, 보여지는 값
        FEMALE = "F", "여성"

    follower_set = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="following_set")
    # following_set = models.ManyToManyField("self", blank=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=14, blank=True, validators=[RegexValidator(r"^010-?[0-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d", help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.")
