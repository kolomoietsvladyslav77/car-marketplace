from src.models.common.models import GenericModel


class UserModel(GenericModel):
    super_id: str
    email: str
