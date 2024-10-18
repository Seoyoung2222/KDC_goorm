from django.contrib import admin

from lotto.models import GuessNumbers

# 같은 폴더라면 폴더명 생략 가능 (lotto)

# Register your models here.

admin.site.register(GuessNumbers)
