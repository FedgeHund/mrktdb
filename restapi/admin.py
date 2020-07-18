from django.contrib import admin
from .models import Company, Filer, QuarterlyHolding, Security, QuarterlyOtherManagerDistribution, QuarterlySecurityHolding, QuarterlyOtherManager

# Register your models here.
admin.site.register(Company)
admin.site.register(Filer)
admin.site.register(Security)
admin.site.register(QuarterlyOtherManager)
admin.site.register(QuarterlyHolding)
admin.site.register(QuarterlySecurityHolding)
admin.site.register(QuarterlyOtherManagerDistribution)
