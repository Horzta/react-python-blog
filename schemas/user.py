from schemas import ma


class UserSchema(ma.ModelSchema):
    username = ma.Str()
    posts = ma.Nested("PostSchema", many=True, only=['title'])

