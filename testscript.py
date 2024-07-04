import os
from assembler import Assembler

INPUT_FILE = 'testcode.asm'
OUT_FILE = 'testcode.mc'
MRI_FILE = 'mri.txt'
RRI_FILE = 'rri.txt'
IOI_FILE = 'ioi.txt'

def change_working_directory():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

if __name__ == "__main__":
    change_working_directory()

    if not os.path.exists(INPUT_FILE):
        print(f"Error: File '{INPUT_FILE}' not found.")
        exit()

    bin_text = ''
    asm = Assembler(asmpath=INPUT_FILE, mripath=MRI_FILE, rripath=RRI_FILE, ioipath=IOI_FILE)
    print('Assembling...')
    binaries = asm.assemble()
    
    bin_text = '\n'.join(f'{lc}\t{binaries[lc]}' for lc in binaries)

    with open(OUT_FILE, 'r', newline='') as f:
        f_content = f.read()
        print('Expected (repr):\n', repr(f_content))
        print("\nActual (repr):\n", repr(bin_text))

        if f_content.strip() == bin_text.strip():
            print('TEST PASSED')
        else:
            print('TEST FAILED. Expected:\n', f_content, '\nActual:\n', bin_text)
