from dataclasses import dataclass


@dataclass(frozen=True)
class JWTTokensDTO:
    access_token: str
    refresh_token: str
