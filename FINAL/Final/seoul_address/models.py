from django.db import models

# Create your models here.
class DongID(models.Model):
    address_code  = models.CharField("지역코드", max_length=8, unique = True, primary_key = True)
    si_name = models.CharField("시 이름", max_length=5)
    gu_name = models.CharField("구 이름", max_length=10)
    dong_name = models.CharField("동 이름", max_length=10)
    x_cordinate = models.CharField("x좌표",  max_length=20)
    y_cordinate = models.CharField("y좌표",  max_length=20)

    def __str__(self):
        return f"{self.si_name}-{self.gu_name}-{self.dong_name}"