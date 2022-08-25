import win32process
import win32api
import win32con
import struct

from tool import addrtool

class ProcessMemoryControl:
    PROCESS_ALL_ACCESS = win32con.PROCESS_ALL_ACCESS
    OpenProcess = win32api.OpenProcess
    CloseHandle = win32api.CloseHandle
    ReadProcessMemory = win32process.ReadProcessMemory
    WritePocessMemory = win32process.WriteProcessMemory

    def __init__(self, process_name : str):
        self.name = process_name
        self.pid = addrtool.getpid(process_name)
        self.process_base_addr = addrtool.get_base_addr(process_name)
        self.process = self.OpenProcess(self.PROCESS_ALL_ACCESS, False, self.pid)
    
    def base_addr(self):
        return self.process_base_addr

    def read(self, addr : int, read_bytes : int) -> int:
        read_data : bytes = self.ReadProcessMemory(self.process, addr, read_bytes)
        read_data = int.from_bytes(read_data, "little")
        return read_data
    
    def read_float(self, addr : int):
        read_data = self.read(addr, 4)
        read_data = read_data.to_bytes(4, 'little')
        read_data = struct.unpack('f', read_data)
        return read_data[0]

    def read_byte(self, addr : int):
        return self.read(addr, 1)

    def read_word(self, addr : int):
        return self.read(addr, 2)

    def read_dword(self, addr : int):
        return self.read(addr, 4)

    def write(self, addr : int, write_data : bytes) -> bool:
        result = self.WritePocessMemory(self.process, addr, write_data)
        return bool(result)
        # return True if result == 2 else False

    def close(self):
        self.CloseHandle(self.process)
        pass

    def __del__(self):
        self.close()