from asyncio import get_event_loop, set_event_loop
from quamash import QEventLoop
from PyQt5 import Qt
from sys import argv
from server.ui.windows import ServerMonitorWindow

class GuiServerApp:
"""Gui server"""
def __init__(self, parsed_args, db_path):
    self.args = parsed_args
    self.db_path = db_path
    self.ins = None
def main(self):
    connections = dict()
    users = dict()
    self.ins = ChatServerProtocol(self.db_path, connections, users)

    app = Qt.QApplication(argv)
    loop = QEventLoop(app)
    set_event_loop(loop)
    wnd = ServerMonitorWindow()
    wnd.show()
    with loop:
        coro = loop.create_server(lambda: self.ins,
                                     self.args["addr"], self.args["port"])
        server = loop.run_until_complete(coro)

        print('Serving on {}: {}'.format(*server.sockets[0].getsockname()))

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()

