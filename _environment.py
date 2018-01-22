server_and_port = "phoenix-uat.ihs.com:80"
user = "admin"
password = "none"

class Environment:

    def __init__(self, server_and_port):
        self.server_and_port = server_and_port
        self._user = None
        self._password = None

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @user.setter
    def user(self, value):
        self._user = value

    @password.setter
    def password(self, value):
        self._password = value

uat = Environment('phoenix-uat.ihs.com:80')
stage = Environment('sphoenix.ihsglobal.local:80')
prod = Environment('phoenix.ihsglobal.local:80')

environments = {}
environments['uat'] = uat
environments['stage'] = stage
environments['prod'] = prod