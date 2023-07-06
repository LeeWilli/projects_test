# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['video_path', 'server_ip', 'hr_server_url', 'Number', 'say_hello']

# %% ../nbs/00_core.ipynb 5
class Number:
    "A number."
    def __init__(self, num): self.num = num
    def __add__(self, other):
        "Sum of this and `other`."
        return Number(self.num + other.num)
    def __repr__(self): return f'Number({self.num})'

# %% ../nbs/00_core.ipynb 13
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# %% ../nbs/00_core.ipynb 16
video_path = "/home/wangli/projects/hr_detect_server/sample.mp4"  # a path for a smaple.
server_ip = "localhost:8293" # ip and port of the server.
hr_server_url = 'http://{}/'.format(server_ip) # url of the server.
