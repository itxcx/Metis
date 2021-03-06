# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/auth'


DefinitionsPassword = {'required': ['password'], 'properties': {'password': {'maxLength': 128, 'minLength': 6, 'type': 'string'}}}
DefinitionsOauthbind = {'required': ['auth_approach', 'identity', 'password'], 'description': '绑定登录后绑定第三方帐号', 'properties': {'auth_approach': {'enum': ['weibo', 'weixin', 'wxapp'], 'type': 'string', 'default': 'mobile', 'description': '绑定第三方帐号 微信 微信公众号 微信小程序'}, 'password': {'type': 'string', 'description': '微博token/微信token'}, 'identity': {'type': 'string', 'description': 'weibo/weixin uid'}}}
DefinitionsError = {'properties': {'text': {'type': 'string'}, 'error_code': {'format': 'int32', 'type': 'integer'}, 'message': {'type': 'string'}}}
DefinitionsApproach = {'required': ['approach'], 'properties': {'approach': {'type': 'string'}, 'is_verified': {'type': 'boolean'}, 'identity': {'type': 'string'}}}
DefinitionsCreatewxappaccount = {'required': ['username', 'password', 'code'], 'properties': {'code': {'type': 'string'}, 'username': {'type': 'string'}, 'password': {'type': 'string'}}}
DefinitionsScopes = {'required': ['scopes'], 'properties': {'scopes': {'items': {'type': 'string'}, 'type': 'array', 'description': 'token 类型'}}}
DefinitionsResetpassword = {'properties': {'old_password': {'maxLength': 128, 'minLength': 6, 'type': 'string'}, 'mobile': {'type': 'string'}, 'new_password': {'maxLength': 128, 'minLength': 6, 'type': 'string'}}}
DefinitionsToken = {'description': 'token', 'properties': {'access_token': {'type': 'string'}}}
DefinitionsUpdatepassword = {'properties': {'new_password': {'maxLength': 128, 'minLength': 6, 'type': 'string'}, 'password': {'maxLength': 128, 'minLength': 6, 'type': 'string'}}}
DefinitionsTokendetail = {'required': ['account_id', 'access_token', 'token_type'], 'description': '返回的token信息', 'properties': {'account_id': {'type': 'string'}, 'nickname': {'type': 'string'}, 'token_type': {'type': 'string', 'default': 'jwt'}, 'access_token': {'type': 'string'}}}
DefinitionsAccount = {'required': ['id'], 'description': 'account 基本信息', 'properties': {'date_created': {'format': 'datetime', 'type': 'string'}, 'id': {'type': 'string'}}}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsTokencode = {'required': ['code', 'grant_type'], 'properties': {'code': {'type': 'string'}, 'grant_type': {'enum': ['token_code'], 'type': 'string', 'default': 'token_code'}}}
DefinitionsNone = {'type': 'object'}
DefinitionsAuth_approach = {'properties': {'auth_approach': {'enum': ['mobile', 'wxapp', 'weixin', 'weixin_mp'], 'type': 'string', 'default': 'mobile', 'description': '登录方式 手机 微信 微信小程序'}}}
DefinitionsRefreshtoken = {'required': ['refresh_token', 'grant_type'], 'properties': {'refresh_token': {'type': 'string'}, 'grant_type': {'enum': ['refresh_token'], 'type': 'string', 'default': 'refresh_token'}}}
DefinitionsAuthentications = {'description': '用户详细授权数据', 'properties': {'wxapp': {'type': 'string'}, 'mobile': {'type': 'string'}}}
DefinitionsAuthentication = {'required': ['username', 'password'], 'allOf': [DefinitionsAuth_approach, {'type': 'object'}], 'properties': {'username': {'type': 'string', 'description': '手机号//微信open_id/email'}, 'password': {'type': 'string', 'description': '密码/微信token'}, 'grant_type': {'enum': ['password'], 'type': 'string', 'default': 'password', 'description': '认证类型 默认密码'}}, 'optional': ['grant_type', 'auth_approach'], 'type': 'object', 'description': '获取token 登录 使用'}
DefinitionsAccountdetail = {'required': ['id'], 'description': 'account 信息', 'properties': {'authentications': DefinitionsAuthentications, 'avatar': {'type': 'string'}, 'nickname': {'type': 'string'}, 'username': {'type': 'string'}, 'created_time': {'format': 'datetime', 'type': 'string'}, 'id': {'type': 'string'}}}

validators = {
    ('oauth_token_code', 'POST'): {'json': DefinitionsTokencode, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string', 'description': '格式 (Basic hashkey) 注 hashkey为client_id + client_secret 做BASE64处理'}}}},
    ('accounts_self', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('oauth_token', 'POST'): {'json': DefinitionsAuthentication, 'args': {'required': [], 'properties': {'code': {'required': False, 'type': 'string', 'description': 'code'}}}, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string', 'description': '格式 (Basic hashkey) 注 hashkey为client_id + client_secret 做BASE64处理'}}}},
    ('self_password_reset', 'POST'): {'json': DefinitionsResetpassword, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string', 'description': '格式 (Basic hashkey) 注 hashkey为client_id + client_secret 做BASE64处理'}}}},
    ('self_password', 'POST'): {'json': DefinitionsPassword, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('self_password', 'PUT'): {'json': DefinitionsUpdatepassword, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('oauth_token_refresh', 'POST'): {'json': DefinitionsRefreshtoken, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string', 'description': '格式 (Basic hashkey) 注 hashkey为client_id + client_secret 做BASE64处理'}}}},
    ('accounts_wxapp', 'POST'): {'json': DefinitionsCreatewxappaccount, 'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
}

filters = {
    ('oauth_token_code', 'POST'): {200: {'schema': DefinitionsTokendetail, 'headers': None}},
    ('accounts_self', 'GET'): {200: {'schema': DefinitionsAccountdetail, 'headers': None}},
    ('oauth_token', 'POST'): {201: {'schema': DefinitionsTokendetail, 'headers': None}},
    ('self_password_reset', 'POST'): {200: {'schema': DefinitionsSuccess, 'headers': None}},
    ('self_password', 'POST'): {201: {'schema': DefinitionsPassword, 'headers': None}},
    ('self_password', 'PUT'): {200: {'schema': DefinitionsSuccess, 'headers': None}},
    ('oauth_token_refresh', 'POST'): {200: {'schema': DefinitionsTokendetail, 'headers': None}},
    ('accounts_wxapp', 'POST'): {201: {'schema': DefinitionsAccount, 'headers': None}},
}

scopes = {
    ('oauth_token_code', 'POST'): ['login'],
    ('accounts_self', 'GET'): ['open'],
    ('oauth_token', 'POST'): ['login', 'register'],
    ('self_password_reset', 'POST'): ['login'],
    ('self_password', 'POST'): ['open'],
    ('self_password', 'PUT'): ['open'],
    ('oauth_token_refresh', 'POST'): ['login'],
    ('accounts_wxapp', 'POST'): ['login'],
}


class Current(object):

    request = None


current = Current()


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda x: []

    @property
    def scopes(self):
        return self._loader(current.request)

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):

    import six

    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

