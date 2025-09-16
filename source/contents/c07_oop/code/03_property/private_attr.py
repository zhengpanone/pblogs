class User:
    def __init__(self, password):
        self._password = password

    @property
    def password(self):
        raise AttributeError("密码不可直接访问")

    @password.setter
    def password(self, raw):
        self._password = raw  # 实际项目中一般会加密存储
