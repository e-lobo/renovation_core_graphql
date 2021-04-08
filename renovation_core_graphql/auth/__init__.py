from graphql import GraphQLSchema

from .login import login_resolver, pin_login_resolver
from .otp import generate_otp_resolver, verify_otp_resolver
from .change_pwd import change_pwd_resolver


def bind_schema(schema: GraphQLSchema):
    schema.mutation_type.fields["login"].resolve = login_resolver
    schema.mutation_type.fields["pin_login"].resolve = pin_login_resolver

    schema.mutation_type.fields["generate_otp"].resolve = generate_otp_resolver
    schema.mutation_type.fields["verify_otp"].resolve = verify_otp_resolver

    schema.mutation_type.fields["change_password"].resolve = change_pwd_resolver
