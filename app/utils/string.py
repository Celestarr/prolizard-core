import hashlib
import re

# Compile the regular expression
camel_case_pattern = re.compile(r"([A-Z][a-z]*)")


def camel_to_capitalized(camel_str: str) -> str:
    # Use the compiled regex to find all words
    words = camel_case_pattern.findall(camel_str)

    # Join the words with spaces and capitalize the first letter of each word
    capitalized_str = " ".join(word.capitalize() for word in words)

    return capitalized_str


def snake_case_to_title(data: str, transformer=None) -> str:
    result = " ".join([part.capitalize() for part in data.split("_")])

    if transformer:
        return transformer(result)

    return result


def snake_to_capitalized(snake_str: str) -> str:
    # Split the string by underscores
    words = snake_str.split("_")

    # Capitalize each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words with spaces
    capitalized_str = " ".join(capitalized_words)

    return capitalized_str


def hash_string(data: str) -> str:
    return hashlib.sha512(data.encode()).hexdigest()


__all__ = ["hash_string", "snake_case_to_title"]
