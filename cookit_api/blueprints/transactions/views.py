from flask import Blueprint, jsonify, request
import stripe
import helpers
from helpers import calculate_order_amount

transactions_api_blueprint = Blueprint('transactions_api',
                             __name__)

@transactions_api_blueprint.route('/new', methods=['POST'])
def create():
    try:
      data = request.json
      print(data)
      intent = stripe.PaymentIntent.create(
        amount=calculate_order_amount(data['numOfMeals']),
        currency='myr'
      )

      return jsonify({
        'clientSecret' : intent['client_secret']
      })
    
    except Exception as e:
      return jsonify(error=str(e))