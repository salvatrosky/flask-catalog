from marshmallow import Schema, fields, validate

class PrizeFilterSchema(Schema):
    id = fields.Integer(validate=validate.Range(min=1))
    description = fields.Str(validate=validate.Length(max=255))

class PaginationSchema(Schema):
    page = fields.Integer(validate=validate.Range(min=1))
    per_page = fields.Integer(validate=validate.Range(min=1, max=100))

class GetPrizesSchema(Schema):
    filter = fields.Nested(PrizeFilterSchema)
    pagination = fields.Nested(PaginationSchema)
