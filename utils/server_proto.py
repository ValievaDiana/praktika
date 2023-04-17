from functools import wraps
    def eof_received(self):
        self.transport.close()
    def connection_lost(self, exc):
        if isinstance(exc, ConnectionResetError):
            print('ConnectionResetError')
            print(self.connections)
            print(self.users)
        # remove closed connections
        rm_con = []
        for con in self.connections:
            if con._closing:
                rm_con.append(con)
        for i in rm_con:
            del self.connections[i]
        # remove from users
        rm_user = []
        for k, v in self.users.items():
            for con in rm_con:
                if v['transport'] == con:
                    rm_user.append(k)
        for u in rm_user:
            del self.users[u]
            self.set_user_offline(u)
            print('{} disconnected'.format(u))
    def _login_required(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            is_auth = self.get_user_status(self.user)
            if is_auth:
                result = func(self, *args, **kwargs)
                return result
            else:
                resp_msg = self.jim.response(code=501, error='login required')
                self.users[self.user]['transport'].write(
                self._dict_to_bytes(resp_msg))
        return wrapper
@_login_required
def action_msg(self, data):
    try:
        if data['from']:  # send msg to sender&#39;s chat
            print(data)
            # save msg to DB history messages
            self._cm.add_client_message(data['from'], data['to'],
                                                                data['message'])
            self.users[data['from']]['transport'].write(
                self._dict_to_bytes(data))
        if data['to'] and data['from'] != data['to']:
            try:
                self.users[data['to']]['transport'].write(
                    self._dict_to_bytes(data))
            except KeyError:
                print('{} is not connected yet'.format(data['to']))
    except Exception as e:
        resp_msg = self.jim.response(code=500, error=e)
        self.transport.write(self._dict_to_bytes(resp_msg))

def data_received(self, data):
    if _data:
            try:
                elif _data['action'] == 'msg':
                    self.user = _data['from']
                    self.action_msg(_data)