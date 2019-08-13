from sqlalchemy.ext.declarative import declarative_base
from utils.exceptions import ModelAttrError


class ModelBase:
    def update(self, error_on_attr_not_found=True, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                if error_on_attr_not_found:
                    raise ModelAttrError(description='Model attribute %s not found' % key,
                                         errors={key: ['Attribute %s not exists' % key]})


Base = declarative_base(cls=ModelBase)
