import hashlib


def snake_case_to_title(data: str, transformer=None) -> str:
    result = " ".join([part.capitalize() for part in data.split("_")])

    if transformer:
        return transformer(result)

    return result


def hash_string(data: str) -> str:
    return hashlib.sha512(data.encode()).hexdigest()


__all__ = ["hash_string", "snake_case_to_title"]
