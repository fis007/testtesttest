from flask import Blueprint, jsonify, request
from helpers import get_client_token, create_transaction
from braintree.successful_result import SuccessfulResult
from models.transaction import Transaction

transactions_api_blueprint = Blueprint('transactions_api',
                             __name__)

@transactions_api_blueprint.route('/new', methods=['GET'])
def new():
  client_token = get_client_token()
  return jsonify({
    'client_token': client_token
  })

@transactions_api_blueprint.route('/checkout', methods=['POST'])
def create():
  data = request.json
  nonce_from_the_client = data.get("payment_method_nonce")
  

  amount = (data.get("numOfMeals") * 15)
  nonce = data.get("payment_method_nonce")
  user = data.get("user")
  meal = data.get("meal")

  result = create_transaction(amount=amount, nonce=nonce)
  if type(result) == SuccessfulResult:
    new_transaction = Transaction(amount=amount, meal=meal, user=user)
    if new_transaction.save():
      return jsonify({
        "Payment Status": "Successful"
      })
    else:
      return jsonify({
        "Payment Status": "Failed",
        "Error": "Couldn't save transaction"
      })
  else:
    jsonify({
      "Payment Status": "Failed",
      "Error": "Couldn't create braintree transaction"
    })