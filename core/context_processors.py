from django.core.cache import cache

from .models import CompanyInfo, SiteSettings

_CACHE_KEY_COMPANY = "company_info_singleton"
_CACHE_KEY_SETTINGS = "site_settings_singleton"
_CACHE_TTL = 300  # 5 minutes


def company_info(request):
    company = cache.get(_CACHE_KEY_COMPANY)
    if company is None:
        company = CompanyInfo.get()
        cache.set(_CACHE_KEY_COMPANY, company, _CACHE_TTL)
    
    settings = cache.get(_CACHE_KEY_SETTINGS)
    if settings is None:
        settings = SiteSettings.get()
        cache.set(_CACHE_KEY_SETTINGS, settings, _CACHE_TTL)
    
    return {"company": company, "settings": settings}
