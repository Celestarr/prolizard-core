from .employment_type import EmploymentTypeAdmin
from .preference import MemberPreferenceAdmin
from .proficiency_level import LanguageProficiencyLevelAdmin, SkillProficiencyLevelAdmin
from .profile_section import (
    AcademicRecordAdmin,
    CertificationAdmin,
    HonorOrAwardAdmin,
    LanguageAdmin,
    ProjectAdmin,
    PublicationAdmin,
    SkillAdmin,
    WebLinkAdmin,
    WorkExperienceAdmin,
)
from .template import PortfolioTemplateAdmin, ResumeTemplateAdmin

__all__ = [
    "EmploymentTypeAdmin",
    "MemberPreferenceAdmin",
    "SkillProficiencyLevelAdmin",
    "LanguageProficiencyLevelAdmin",
    "AcademicRecordAdmin",
    "SkillAdmin",
    "WebLinkAdmin",
    "WorkExperienceAdmin",
    "CertificationAdmin",
    "HonorOrAwardAdmin",
    "LanguageAdmin",
    "ProjectAdmin",
    "PublicationAdmin",
    "PortfolioTemplateAdmin",
    "ResumeTemplateAdmin",
]
