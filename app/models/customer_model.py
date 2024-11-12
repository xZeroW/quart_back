from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import Base


class Customer(Base):
    __tablename__ = "customers"

    name: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    logo_image: Mapped[str | None] = mapped_column()
    status: Mapped[str] = mapped_column(default="active")
    commercial_manager: Mapped[str | None] = mapped_column()
    allow_new_organizations: Mapped[bool] = mapped_column(default=True)
    allow_update_company_branch: Mapped[bool] = mapped_column(default=False)
    period_to_enforce_password_change: Mapped[int | None] = mapped_column()
    allow_new_organization_without_cnpj: Mapped[bool] = mapped_column(default=False)
    allow_task_manager_access: Mapped[bool] = mapped_column(default=True)
    allow_domain_indicators_report: Mapped[bool] = mapped_column(default=False)
    task_send_email_to_all_department_users: Mapped[bool] = mapped_column(default=False)
    colors: Mapped[str | None] = mapped_column()
    allow_management_report: Mapped[bool] = mapped_column(default=False)
    use_gmail_sender: Mapped[bool] = mapped_column(default=False)
    concept_proof: Mapped[bool] = mapped_column(default=False)
    prof_concept_deadline: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    allow_old_passwords: Mapped[bool] = mapped_column(default=False)
