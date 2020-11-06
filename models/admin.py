from models.base_model import BaseModel
import peewee as pw
from werkzeug.security import generate_password_hash
import re


class Admin(BaseModel):
    name = pw.CharField(unique=False)
    email = pw.CharField(unique=True)
    password_hash = pw.CharField(unique=False)
    password = None

    def validate(self):
        duplicate_email = Admin.get_or_none(Admin.email == self.email)
        print("Admin validation in process")

        if duplicate_email and self.id != duplicate_email.id:
            self.errors.append("There is an existing account with this email address")

        if self.password:
            if len(self.password) < 6:
                self.errors.append("Password must consist of at least 6 characters")
            if len(self.errors) == 0:
                print("No errors detected")
                self.password_hash = generate_password_hash(self.password)
        elif not self.password_hash:
            self.errors.append("Password is required")