from models.base_model import BaseModel
import peewee as pw
from playhouse.postgres_ext import *
from models.user import User
from models.meal import Meal

class Transaction(BaseModel):
    user = pw.ForeignKeyField(User, backref="payments", on_delete="CASCADE")
    meal = pw.ForeignKeyField(Meal, backref="payments", on_delete="CASCADE")
    amount = pw.DecimalField(null=False)