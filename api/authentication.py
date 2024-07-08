from tastypie.authentication import ApiKeyAuthentication


class CustomAuthentication(ApiKeyAuthentication):
    # Включение аутентификации для всех методов кроме GET
    def is_authenticated(self, request, **kwargs):
        if request.method == "GET":
            return True

        return super().is_authenticated(request, **kwargs)
