from src.errors.base_error import BaseError


class SignUpError(BaseError):
    code = 400
    message = "Sign up error"
    error_code = 400_02_001


class SignInError(BaseError):
    code = 400
    message = "Sign in error"
    error_code = 400_02_002


class RefreshTokensError(BaseError):
    code = 400
    message = "Refresh tokens error"
    error_code = 400_02_003
