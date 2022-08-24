from class_gather.process_class import ProcessMemoryControl

class AC(ProcessMemoryControl):
    def __init__(self):
        super().__init__("ac_client")
        self.process_base_addr = super().base_addr()
    
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