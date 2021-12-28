from django.core.validators import RegexValidator

phone_number_validators = RegexValidator(
    regex="^(\+996)\d{9}$", message="Your phone number is not valid"
)
