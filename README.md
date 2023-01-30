# cryptoax
F-Zero AX card save file decryption/encryption

Python rewrite of Crediars cryptoax.exe tool: https://crediar.dev/crediar/tools/-/tree/main/cryptoAX<br>
Added CRC recalc for convenience<br><br>
The script is designed to be run against an F-Zero AX card save file exported from emulators<br>
If run against an encrypted file it will decrypt it for examination or modification<br>
If run against a decrypted file it will encrypt it ready for play, calculating new CRC check bytes<br><br>
Usage: python3 cryptoax.py inputfile outputfile
