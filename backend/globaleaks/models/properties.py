# -*- coding: utf-8 -*-
from sqlalchemy import Column, CheckConstraint, ForeignKeyConstraint, types
from sqlalchemy.types import Boolean, DateTime, Integer, String, UnicodeText
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.schema import ForeignKey

from globaleaks.utils.utility import uuid4 # pylint: disable=unused-import

import json
class JSON(types.TypeDecorator):
    """Stores and retrieves JSON as TEXT."""

    impl = types.UnicodeText

    def process_bind_param(self, value, dialect): 
        if value is not None:
            value = unicode(json.dumps(value))
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value
