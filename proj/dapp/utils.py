from datetime import datetime

from .models import UploadImageModel
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile


class PlanBasic:
    def __init__(self, request, form):
        self.request = request
        self.form = form
        self.username = request.user.username
        self.fields = {}
        self.image = self.form.cleaned_data['image']
        self.img = Image.open(self.image)
        self.original = None

    def get_fields(self):
        return self.fields

    @staticmethod
    def compute_image(image, size):
        img = image.copy()
        img.thumbnail((size, size))

        img_file = BytesIO()
        img.save(img_file, format='JPEG')
        return ContentFile(img_file.getvalue())

    @staticmethod
    def file_name(username, size, extension='jpg'):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"{username}_{timestamp}_{size}.{extension}"

    def compute_fields(self):
        thumbnail_200 = UploadImageModel()
        thumbnail_200.image.save(self.file_name(self.username, 200), self.compute_image(self.img, 200))

        self.fields.update({
            "image_200_url": self.request.build_absolute_uri(thumbnail_200.image.url),
        })


class PlanPremium(PlanBasic):
    def __init__(self, request, form):
        super().__init__(request, form)

    def compute_fields(self):
        super().compute_fields()

        thumbnail_400 = UploadImageModel()
        thumbnail_400.image.save(self.file_name(self.username, 400), self.compute_image(self.img, 400))
        original = UploadImageModel()
        original.image.save(self.file_name(self.username, "original"), self.image)
        self.original_url = original.image.url
        self.fields.update({
            "image_400_url": self.request.build_absolute_uri(thumbnail_400.image.url),
            "image_original_url": self.request.build_absolute_uri(original.image.url),
        })


class PlanEnterprise(PlanPremium):
    def __init__(self, request, form):
        super().__init__(request, form)

    def compute_fields(self):
        super().compute_fields()

        self.fields.update({
            "image_download": self.request.build_absolute_uri(self.original_url)
        })
