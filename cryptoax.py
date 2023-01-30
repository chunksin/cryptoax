import sys

def crc16(data: bytes, poly=0x8408):
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    return crc & 0xFFFF

print('-----------')
print('cryptoax.py - Python conversion by Chunksin of Crediars cryptoax.exe tool')
print('https://crediar.dev/crediar/tools/-/tree/main/cryptoAX')
print('-----------\n')
if len(sys.argv) != 3:
    print("""\
This script will decode/encode an F-Zero AX card data file
Usage:  cryptoax.py inputfile outputfile
""")
    sys.exit(1)

# Open the card file and read in the data minus the old CRC
raw = open(sys.argv[1], 'rb').read()
card = bytearray(raw[:205])
# Calculate the replacement CRC and add it
crc = crc16(card).to_bytes(2, byteorder='big')
print('New CRC is',crc.hex())
card += crc
# Identify the XOR seed byte
seed = bytearray(card[146:147])
# Split the first part of the card
firstpart = bytearray(card[:138])
# Split the SEGABGG4 text
segapart = bytearray(card[138:146])
# Split the last part of the card
lastpart = bytearray(card[147:])
print('Seed is',hex(seed[0]))
# Funky seed manipulation
seedA = seed[0] ^ 0xCAE87FB5
seedB = 0x676A4B6B
# Set the size of the file sections to process
firstsize = len(firstpart)
lastsize = len(lastpart)
# XOR the first part of the file
for i in range(firstsize):
    seedA = seedA * seedB + 0x33CB
    firstpart[i] ^= (seedA >> 16) & 0xFF
# XOR the last part of the file
for i in range(lastsize):
    seedA = seedA * seedB + 0x33CB
    lastpart[i] ^= (seedA >> 16) & 0xFF
# Stitch it back together
final = firstpart+segapart+seed+lastpart
# Write out the result to a new file
open(sys.argv[2], 'wb').write(final)
print('New card file written to',sys.argv[2],'\n')

