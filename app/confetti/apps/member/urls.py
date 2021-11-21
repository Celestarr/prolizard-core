from rest_framework.routers import SimpleRouter

from confetti.apps.member.views import (
    AcademicRecordViewSet,
    CertificationViewSet,
    HonorOrAwardViewSet,
    LanguageViewSet,
    MemberConfirmEmailViewSet,
    MemberSignInViewSet,
    MemberSignOutViewSet,
    MemberSignUpViewSet,
    MemberViewSet,
    ProjectViewSet,
    PublicationViewSet,
    SkillViewSet,
    WebLinkViewSet,
    WorkExperienceViewSet,
)

router = SimpleRouter()
router.register(r"confirm-email", MemberConfirmEmailViewSet, basename="confirm-email")
router.register(r"sign-in", MemberSignInViewSet, basename="sign-in")
router.register(r"sign-up", MemberSignUpViewSet, basename="sign-up")
router.register(r"sign-out", MemberSignOutViewSet, basename="sign-out")
router.register(r"profile-sections/academic-records", AcademicRecordViewSet)
router.register(r"profile-sections/certifications", CertificationViewSet)
router.register(r"profile-sections/honors-or-awards", HonorOrAwardViewSet)
router.register(r"profile-sections/languages", LanguageViewSet)
router.register(r"profile-sections/projects", ProjectViewSet)
router.register(r"profile-sections/publications", PublicationViewSet)
router.register(r"profile-sections/skills", SkillViewSet)
router.register(r"profile-sections/web-links", WebLinkViewSet)
router.register(r"profile-sections/work-experiences", WorkExperienceViewSet)
router.register(r"", MemberViewSet)

urlpatterns = router.urls
