from flask.views import MethodView
from flask import abort, jsonify

from testservice.models import User


class ItemSchema:
    action: str
    name: str
    email: str
    location: str
    reply_to: dict


class UserView(MethodView):
    def _validate_params_post(self, params, schema):

        if not isinstance(params, dict):
            return abort(jsonify(id=None, error_code=1,
                                 error_msg=f'Dict object is required: {params}'), 400)

        params_names = set(params.keys())
        required_params = set(schema.__annotations__.keys())
        unknown_params = params_names - required_params
        if unknown_params:
            return abort(jsonify(id=None, error_code=1,
                                 error_msg=f'Unknown params: {unknown_params}'), 400)
        missing_params = required_params - params_names
        if missing_params:
            return abort(jsonify(id=None, error_code=1,
                                 error_msg=f'Missing params: {missing_params}'), 400)
        return all(self._validate_param(k, v) for k, v in params.items())

    def _validate_param(self, name, value):
        param_type = self.schema_params.get(name)
        if not isinstance(value, param_type):
            return abort(jsonify(id=None, error_code=1,
                                 error_msg=f'Invalid param type: {name}={value} '
                                 f'({type(value)} != {param_type})'), 400)
        return True

    def post(self):
        if not self.data:
            return abort(jsonify(id=None, error_code=1,
                                 error_msg=f'Body is required'), 400)
        return_code = 201

        self._validate_params_post(self.data, ItemSchema)

        user = User(name=self.data['name'], email=self.data['email'], location=self.data['location'])

        # Check if already exists
        existing_user = self.session.query(User).filter(
            User.name==self.data['name'],
            User.email==self.data['email'],
            User.location==self.data['location'],
        ).first()
        if existing_user:
            return abort(jsonify(id=None, error_code=1,
                                 error_msg=f'User already exists'), 400)

        self.session.add(user)
        return jsonify(id=user.id, error_code=0, error_msg=''), return_code
