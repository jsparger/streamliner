from lewis.devices import Device

from lewis.adapters.epics import EpicsInterface, PV
from lewis.adapters.stream import StreamInterface, Var


class ExampleDevice(Device):
    i = 7
    f = 9.9
    s = "hello world"
    def fcn(self, x):
        return 2*x

class ExampleEpicsInterface(EpicsInterface):
    pvs = {
        'I': PV('i', type='int'),
        'F': PV('f', type='float'),
        'S': PV('s', type='string'),
        'FCN': PV('fcn', type='')
    }

# automatically parse device
AutoExampleEpicsInterface = sl.AutoEpicsInterface(ExampleDevice)

class ExampleStreamInterface(StreamInterface):
    # commands = {
    #     Var('i', read_pattern=r'I\?$', write_pattern=r'I=(\d+)', argument_mappings=(int,),
    #         doc='An integer parameter.'),
    #     Cmd('get_i', pattern=r'I\?$'),
    #     Cmd('set_i', pattern=r'I=(\d+)')
    # }

    @cmd(pattern=r'I\?$')
    @return_format('I=%d')
    def get_i(self):
        return self.device.i

    @cmd(pattern=r'I=(\d+)')
    @return_format('previous=%d, now=%d')
    def set_i(self,x):
        previous = self.device.i
        self.device.i = x
        return (previous, self.device.i)

class ExampleEpicsStreamDeviceInterface(sl.EpicsStreamDeviceInterface(ExampleStreamInterface)):
    @pv('I')
    def get_i(self):
        self.i = self.stream.get_i()

    @pv('I_set')
    def set_i(self, x):
        self.stream.set_i(x)
