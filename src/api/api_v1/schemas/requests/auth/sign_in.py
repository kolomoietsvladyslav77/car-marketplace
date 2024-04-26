from pydantic import BaseModel, EmailStr, constr


class SignInRequestSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=6, max_length=40)
