from app.utils.views.routers import HyphenatedSimpleRouter

from .views import (
    CountryViewSet,
    EmploymentTypeViewSet,
    GenderViewSet,
    LanguageProficiencyLevelViewSet,
    LocaleViewSet,
    ResumeTemplateViewSet,
    SkillProficiencyLevelViewSet,
    TimeZoneViewSet,
)

app_name = "core"  # pylint: disable=invalid-name

router = HyphenatedSimpleRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"genders", GenderViewSet, basename="gender")
router.register(r"locales", LocaleViewSet, basename="locale")
router.register(r"language-proficiency-levels", LanguageProficiencyLevelViewSet, basename="language-proficiency-level")
router.register(r"skill-proficiency-levels", SkillProficiencyLevelViewSet, basename="skill-proficiency-level")
router.register(r"time-zones", TimeZoneViewSet, basename="time-zone")
router.register(r"employment-types", EmploymentTypeViewSet, basename="employment-type")
router.register(r"resume-templates", ResumeTemplateViewSet, basename="resume-template")


urlpatterns = router.urls

urlpatterns += []
