from app.utils.views.routers import HyphenatedSimpleRouter

from .views import CountryViewSet, LocaleViewSet, ResumeTemplateViewSet, TimeZoneViewSet

app_name = "core"  # pylint: disable=invalid-name

router = HyphenatedSimpleRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"locales", LocaleViewSet, basename="locale")
router.register(r"time-zones", TimeZoneViewSet, basename="time-zone")
router.register(r"resume-templates", ResumeTemplateViewSet, basename="resume-template")


urlpatterns = router.urls

urlpatterns += []
