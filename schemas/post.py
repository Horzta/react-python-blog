from schemas import ma


class PostSchema(ma.ModelSchema):
    title = ma.Str()
    content = ma.Str()
    author = ma.Nested('UserSchema', only=['username'])
