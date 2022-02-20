from rest_framework.routers import SimpleRouter

from .views import (
    AcademicRecordViewSet,
    CertificationViewSet,
    HonorOrAwardViewSet,
    LanguageViewSet,
    MemberViewSet,
    ProjectViewSet,
    PublicationViewSet,
    SkillViewSet,
    WebLinkViewSet,
    WorkExperienceViewSet,
)

router = SimpleRouter()
router.register(r"sections/academic-records", AcademicRecordViewSet)
router.register(r"sections/certifications", CertificationViewSet)
router.register(r"sections/honors-or-awards", HonorOrAwardViewSet)
router.register(r"sections/languages", LanguageViewSet)
router.register(r"sections/projects", ProjectViewSet)
router.register(r"sections/publications", PublicationViewSet)
router.register(r"sections/skills", SkillViewSet)
router.register(r"sections/web-links", WebLinkViewSet)
router.register(r"sections/work-experiences", WorkExperienceViewSet)
router.register(r"", MemberViewSet)

urlpatterns = router.urls
