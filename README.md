# Simple-Assembler-for-Custom-Instruction-Set-Architecture
This project implements a simple assembler for a custom Instruction Set Architecture (ISA). The assembler reads assembly code, processes it in two passes, and outputs the corresponding binary machine code. It supports memory-reference instructions (MRI), register-reference instructions (RRI), and input-output instructions (IOI).

Features:

Assembly Code Parsing: Reads and parses assembly code, handling comments and labels.
Two-Pass Assembly Process:
   First Pass: Scans for labels and stores their locations.
   Second Pass: Converts assembly instructions to binary machine code using predefined tables.
Support for MRI, RRI, and IOI: Loads and uses predefined tables for memory-reference, register-reference, and input-output instructions.
Flexible File Input: Accepts file paths for assembly code and instruction tables as arguments.

Usage:
  Initialization: Create an instance of the Assembler class, optionally providing paths to assembly code and instruction tables.
  Assembly: Call the assemble method to process the assembly code and retrieve the binary machine code.

Code Structure:
Assembler Class:
Initialization (__init__): Initializes important properties and loads files if paths are provided.
read_code Method: Reads the assembly code from a file.
assemble Method: Main method to run the two-pass assembly process.
Private Methods:
  __load_table: Loads instruction tables from files.
  __islabel: Checks if a string is a label.
  __rm_comments: Removes comments from the assembly code.
  __format2bin: Converts numbers to binary format.
  __first_pass: First pass to process labels.
  __second_pass: Second pass to convert instructions to binary.

Contributing:
Contributions are welcome! Please fork the repository and submit a pull request.

License:
This project is licensed under the MIT License.
