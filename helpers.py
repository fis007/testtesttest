import stripe
from app import app

stripe.api_key = app.config.get("STRIPE_SECRET")

def calculate_order_amount(meals):
  return meals * 150