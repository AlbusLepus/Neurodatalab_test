from flask import Blueprint
from testservice.api.user.views import UserView

user_blueprint = Blueprint('public', __name__, url_prefix='/user')

user_view = UserView.as_view('user')
user_blueprint.add_url_rule('/',
                            view_func=user_view,
                            methods=['POST'])
