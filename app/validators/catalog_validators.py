from flask import jsonify, request

def validate_data(schema):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            errors = None
            if data:
                errors = schema.validate(data)
            if errors:
                return jsonify({'error': errors}), 400
            return func(data, *args, **kwargs) 
        return wrapper
    return decorator