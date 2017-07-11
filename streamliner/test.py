# from lewis.devices import Device
# from lewis.adapters.stream import StreamInterface, Cmd, Var
from streamliner import return_mapping, cmd
# from scanf import scanf

# class TestDevice(Device):
#     x = 10

commands = []

class TestStreamInterface(object):
    commands = commands

    @cmd(pattern=r"x\\?")
    @return_mapping('x = {}')
    def get_x(self):
        return self.device.x

    @cmd(pattern=r'x=(\d+)')
    @return_mapping('old x = {}, new x = {}')
    def set_x(self, new):
        old = self.device.x
        self.device.x = new
        return (old, self.device.x)
