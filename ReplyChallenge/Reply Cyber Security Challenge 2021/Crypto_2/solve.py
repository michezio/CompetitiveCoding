'''
Still cannot find the solution ¯\_(ツ)_/¯
'''

from enigma.machine import EnigmaMachine
import itertools

reflectors = ['B-Thin', 'C-Thin'] 
rotors = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'] 
greek = ['Gamma', 'Beta']

with open(f"result.txt", 'w') as f:
    for r in reflectors: 
        for g in greek:
            for r1, r2, r3 in itertools.combinations_with_replacement(rotors, 3): 
                machine = EnigmaMachine.from_key_sheet( 
                    rotors=' '.join([g, r1, r2, r3]), 
                    reflector=r, 
                    ring_settings=[21, 18, 16, 11], #[20, 17, 15, 10]
                    plugboard_settings='NH CW MK PO ZS QB FU TR') 
        
                machine.set_display("FLTG") 
                temp = machine.process_text('utogaaxgeonuvkegegddajktikdtvepnkolokj') 

                print(temp.lower(), g, r1, r2, r3, r) 