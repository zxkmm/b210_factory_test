import numpy as np
from gnuradio import gr
import time

class blk(gr.basic_block):
    def __init__(self, freq_list=[433e6, 915e6, 1800e6, 2400e6, 2450e6, 5800e6], dwell_time=5.0):
        gr.basic_block.__init__(self,
            name="Frequency Selector",
            in_sig=[],
            out_sig=[])
        
        self.freq_list = freq_list
        self.dwell_time = dwell_time
        self.freq_index = 0
        self.last_change_time = time.time()
        
    def get_freq(self):
        current_time = time.time()
        if current_time - self.last_change_time >= self.dwell_time:
            self.freq_index = (self.freq_index + 1) % len(self.freq_list)
            self.last_change_time = current_time
            print(f"Switching to frequency: {self.freq_list[self.freq_index]/1e6:.0f} MHz")
        
        return self.freq_list[self.freq_index]
