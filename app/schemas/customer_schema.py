from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from app.schemas.base_schema import BaseSchema


class CustomerResponseSchema(BaseSchema):
    id: UUID
    name: str
    description: Optional[str]
    logo_image: Optional[str]
    status: str = Field(default="active")
    commercial_manager: Optional[str]
    allow_new_organizations: bool = Field(default=True)
    allow_update_company_branch: bool = Field(default=False)
    period_to_enforce_password_change: int | None
    allow_new_organization_without_cnpj: bool = Field(default=False)
    allow_task_manager_access: bool = Field(default=True)
    allow_domain_indicators_report: bool = Field(default=False)
    task_send_email_to_all_department_users: bool = Field(default=False)
    colors: Optional[list]
    allow_management_report: bool = Field(default=False)
    use_gmail_sender: bool = Field(default=False)
    concept_proof: bool = Field(default=False)
    prof_concept_deadline: Optional[datetime]
    allow_old_passwords: bool = Field(default=False)
