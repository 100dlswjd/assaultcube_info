from class_gather.process_class import ProcessMemoryControl

class AC(ProcessMemoryControl):
    def __init__(self):
        super().__init__("ac_client")
        self.process_base_addr = super().base_addr()
    
    def x_pos(self):
        target_addr = self.process_base_addr + 0x17E090
        x_pos = super().read_dword(target_addr, "float")
        return x_pos

    def y_pos(self):
        target_addr = self.process_base_addr + 0x17E094
        y_pos = super().read_dword(target_addr, "float")
        return y_pos

    def z_pos(self):
        target_addr = self.process_base_addr + 0x17E098
        z_pos = super().read_dword(target_addr, "float")
        return z_pos

    def undead_on(self):
        nop_code = b'\x90\x90\x90'
        target_addr = self.process_base_addr + 0x1c223
        super().write(target_addr, nop_code)

    def undead_off(self):
        org_code = b')s\x04'
        target_addr = self.process_base_addr + 0x1c223
        super().write(target_addr, org_code)
    
    def hp(self):
        HP_OFFSET = 0xEC
        pointer_start = super().read_dword(self.process_base_addr + 0x0017E0A8)
        hp = super().read_word(pointer_start + HP_OFFSET)
        return hp

    def bullet(self):
        BEULLET_OFFSET = 0x140
        pointer_start = super().read_dword(self.process_base_addr + 0x0018AC00)
        bullet = super().read_dword(pointer_start + BEULLET_OFFSET)
        return bullet