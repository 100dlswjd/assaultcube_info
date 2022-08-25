from class_gather.process_class import ProcessMemoryControl

class AC(ProcessMemoryControl):
    HP_OFFSET = 0xEC
    BEULLET_OFFSET = 0x140

    def __init__(self):
        super().__init__("ac_client")
        self.process_base_addr = super().base_addr()
        self.x_pos_addr = self.process_base_addr + 0x17E090
        self.y_pos_addr = self.process_base_addr + 0x17E094
        self.z_pos_addr = self.process_base_addr + 0x17E098
        self.undead_addr = self.process_base_addr + 0x1c223
        self.hp_addr = self.process_base_addr + 0x0017E0A8
        self.bullet_addr = self.process_base_addr + 0x0018AC00
    
    def x_pos(self):
        return super().read_float(self.x_pos_addr)

    def y_pos(self):
        return super().read_float(self.y_pos_addr)
        
    def z_pos(self):
        return super().read_float(self.z_pos_addr)

    def undead_on(self):
        nop_code = b'\x90\x90\x90'
        super().write(self.undead_addr, nop_code)

    def undead_off(self):
        org_code = b')s\x04'
        super().write(self.undead_addr, org_code)
    
    def hp(self):
        pointer_start = super().read_dword(self.hp_addr)
        hp = super().read_word(pointer_start + self.HP_OFFSET)
        return hp
    
    def hp_date(self):
        hp = 1000
        pointer_start = super().read_dword(self.hp_addr)
        super().write(pointer_start + self.HP_OFFSET, hp.to_bytes(4, "little"))

    def bullet(self):
        pointer_start = super().read_dword(self.bullet_addr)
        bullet = super().read_dword(pointer_start + self.BEULLET_OFFSET)
        return bullet

    def bullet_update(self):
        bullet = 500
        pointer_start = super().read_dword(self.bullet_addr)
        super().write(pointer_start + self.BEULLET_OFFSET, bullet.to_bytes(4, "little"))