import hashlib


def snake_case_to_title(s: str, transformer=None) -> str:
    result = " ".join([part.capitalize() for part in s.split("_")])

    if transformer:
        return transformer(result)

    return result


def hash_string(s: str) -> str:
    return hashlib.sha512(s.encode()).hexdigest()


__all__ = ["hash_string", "snake_case_to_title"]
