from oauth2_provider.oauth2_validators import OAuth2Validator


class RequestValidator(OAuth2Validator):
    def introspect_token(self, token, token_type_hint, request, *args, **kwargs) -> None:
        pass

    def validate_silent_authorization(self, request) -> None:
        pass

    def validate_silent_login(self, request) -> None:
        pass
