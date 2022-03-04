import factory
import pycountry
from faker import Faker

from .models import Country

faker = Faker()
default_country = pycountry.countries.get(alpha_2="BD")


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    iso_3166_1_alpha_2_code = default_country.alpha_2
    iso_3166_1_alpha_3_code = default_country.alpha_3
    iso_3166_1_numeric_code = default_country.alpha_2
    name = default_country.name
    formal_name = getattr(default_country, "official_name", default_country.name)

    @classmethod
    def create_batch(cls, size, **kwargs):
        items = []

        for item in pycountry.countries:
            items.append(
                {
                    "iso_3166_1_alpha_2_code": item.alpha_2,
                    "iso_3166_1_alpha_3_code": item.alpha_3,
                    "iso_3166_1_numeric_code": item.numeric,
                    "name": item.name,
                    # Fallback to short/display name if official name is
                    # not provided.
                    "formal_name": getattr(item, "official_name", item.name),
                }
            )

        return [cls.create(**item) for item in items]
