from flask import Blueprint, jsonify
from models.admin import Admin
from flask_jwt_extended import jwt_required, get_jwt_identity

admins_api_blueprint = Blueprint('admins_api',
                             __name__,
                             template_folder='templates')

@admins_api_blueprint.route('/', methods=['GET'])
def index():
    admins = Admin.select()
    return jsonify([{"name": admin.name,"id": admin.id, "email": admin.email} for admin in admins])

@admins_api_blueprint.route('/me', methods=['GET'])
@jwt_required
def me():
    admin_id = get_jwt_identity()
    admin = Admin.get_or_none(Admin.id == admin_id)
    if admin:
        return jsonify({
            "id": admin.id,
            "name": admin.name,
            "email": admin.email
        })
