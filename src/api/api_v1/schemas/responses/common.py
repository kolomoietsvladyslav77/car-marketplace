from pydantic import BaseModel


class SuccessResponseSchema(BaseModel):
    success: bool = True
