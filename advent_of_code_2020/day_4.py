import logging
import re
import numpy as np

from .utils import read_list_file


REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


OPTIONAL_FIELDS = [
    "cid"
]


logger = logging.getLogger(__name__)


class Validator(object):

    def __init__(self):
        pass

    def __call__(self, field):
        return self.validate(field)

    def validate(self, field):
        pass


class RangeValidator(Validator):
    def __init__(self, accepted_range):
        self.accepted_range = accepted_range

    def validate(self, field):
        field = int(field)
        if field < self.accepted_range[0] or field > self.accepted_range[1]:
            return False
        else:
            return True


class LengthValidator(Validator):
    def __init__(self, length):
        self.length = length

    def validate(self, field):
        if len(field) != self.length:
            return False
        else:
            return True

class RegexValidator(Validator):

    def __init__(self, pattern, group_validators=None):
        self.pattern = pattern
        self.group_validators = group_validators

    def validate(self, field):
        is_valid = True
        match = re.search(self.pattern, field)
        if match is None:
            is_valid = False

        try:
            if self.group_validators is not None:
                for i, validator in enumerate(self.group_validators):
                    if not validator(match.group(i + 1)):
                        is_valid = False
        except Exception as e:
            is_valid = False

        return is_valid


class PassportValidator(Validator):

    def __init__(self, validators=None, check_type="all"):
        self.validators = validators
        self.check_type = check_type

    def validate(self, field):
        if self.check_type == "any":
            is_valid = False

            if self.validators is not None:
                for validator in self.validators:
                    if validator(field):
                        is_valid = True

        elif self.check_type == "all":
            is_valid = True

            if self.validators is not None:
                for validator in self.validators:
                    if not validator(field):
                        is_valid = False

        else:
            raise ValueError("`check_type` not in ('any', 'all'). Check your inputs...")


        return is_valid


def read_passports(input_file):
    lines = read_list_file(input_file)

    passports = []
    passport_data = {}
    for line in lines:
        line = line.rstrip()
        key_value_pairs = re.findall("\S*:\S*", line)
        if len(key_value_pairs) > 0:
            for key_value_pair in key_value_pairs:
                key, value = key_value_pair.split(":")
                passport_data[key] = value
        else:
            passports.append(passport_data)
            passport_data = {}

    passports.append(passport_data)

    return passports


def validate_passport(
    passport_data,
    required_fields=REQUIRED_FIELDS,
    optional_fields=OPTIONAL_FIELDS,
    field_validators=None,
):
    passport_fields = set(passport_data.keys())
    is_valid_passport = True
    missing_fields = []
    for field in required_fields:
        if field not in passport_fields:
            missing_fields.append(field)
            is_valid_passport = False
        elif field_validators is not None and field in field_validators:
            field_value = passport_data[field]
            is_field_valid = field_validators[field](field_value)
            if not is_field_valid:
                is_valid_passport = False
    return is_valid_passport


def day_4(part, input_file):
    passports = read_passports(input_file)
    if part == 1:
        field_validators = {}
    elif part == 2:
        field_validators = {
            "byr": PassportValidator(
                validators=[RangeValidator([1920, 2002])]
            ),
            "iyr": PassportValidator(
                validators=[RangeValidator([2010, 2020])]
            ),
            "eyr": PassportValidator(
                validators=[RangeValidator([2020, 2030])]
            ),
            "hgt": PassportValidator(
                validators=[
                    RegexValidator(
                        "^(\d*)cm$",
                        group_validators=[
                            RangeValidator([150, 193]),
                        ]
                    ),
                    RegexValidator(
                        "^(\d*)in$",
                        group_validators=[
                            RangeValidator([59, 76]),
                        ]
                    ),
                ],
                check_type="any"
            ),
            "hcl": PassportValidator(
                validators=[RegexValidator("^#[0-9|a-f]{6}$")],
                check_type="any"
            ),
            "ecl": PassportValidator(
                validators=[RegexValidator("^(amb|blu|brn|gry|grn|hzl|oth)$")],
            ),
            "pid": PassportValidator(
                validators=[RegexValidator("^\d{9}$")],
            ),
        }

    num_passports = len(passports)
    valid_passport_count = sum([
        validate_passport(passport, field_validators=field_validators)
        for passport in passports
    ])

    logger.info(f"Out of {num_passports} passports, there are {valid_passport_count} valid passports")
