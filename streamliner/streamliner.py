from lewis.adapters.stream import Cmd
import inspect

def calling_scope_variable(name):
  frame = inspect.stack()[1][0]
  while name not in frame.f_locals:
    frame = frame.f_back
    if frame is None:
      return None
  return frame.f_locals[name]

# A decorator to convert format a specified string using the functions output
def return_mapping(fmt):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return fmt.format(*func(*args,**kwargs))
        wrapper.return_mapping = fmt
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

def return_mapping_example(x):
    @return_mapping('{} times 2 = {}')
    def example(x):
        return (x,x*2)
    print example(x)
    print example.return_mapping

def cmd(*args, **kwargs):
    def decorator(func):
        commands = calling_scope_variable('commands')
        commands.append(Cmd(func.__name__, *args, **kwargs))
        return func
    return decorator

# def generate_proto(obj):
#     for command in obj.commands:
#         func = obj.getattr(command.func)
#         func.return_mapping
#         pattern = command.pattern
