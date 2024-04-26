import datetime

from pydantic import BaseModel


class AuthUser(BaseModel):
    instance_id: str
    id: str
    aud: str
    role: str
    email: str
    encrypted_password: str
    email_confirmed_at: datetime.datetime | None = None
    invited_at: datetime.datetime | None
    confirmation_token: str | None = None
    confirmation_sent_at: datetime.datetime | None = None
    recovery_token: str | None = None
    recovery_sent_at: datetime.datetime | None = None
    email_change_token_new: str | None = None
    email_change: str | None = None
    email_change_sent_at: datetime.datetime | None = None
    last_sign_in_at: datetime.datetime | None = None
    raw_app_meta_data: dict | None = None
    raw_user_meta_data: dict
    is_super_admin: bool | None = None
    created_at: datetime
    updated_at: datetime
    phone: str | None = None
    phone_confirmed_at: datetime.datetime | None = None
    phone_change: str | None = None
    phone_change_token: str | None = None
    phone_change_sent_at: datetime.datetime | None = None
    confirmed_at: datetime
    email_change_token_current: str | None = None
    email_change_confirm_status: int
    banned_until: datetime.datetime | None = None
    reauthentication_token: str | None = None
    reauthentication_sent_at: datetime.datetime | None = None
    is_sso_user: bool
    deleted_at: datetime.datetime | None = None
    is_anonymous: bool
