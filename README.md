# cryptoax
F-Zero AX card save file decryption/encryption

Python rewrite of Crediars cryptoax.exe tool: https://crediar.dev/crediar/tools/-/tree/main/cryptoAX<br>
Added CRC recalc for convenience<br><br>
The script is designed to be run against an F-Zero AX card save file exported from emulators<br>
If run against an encrypted file it will decrypt it for examination or modification<br>
If run against a decrypted file it will encrypt it ready for play, calculating new CRC check bytes<br><br>
Usage: <b>python3 cryptoax.py inputfile outputfile</b><br><br>
For more information about how card reader emulation works see: https://docs.google.com/document/d/1aUQqpzLeWWvhQ4xr6t2vuMxbN-NrFbmf/edit?usp=share_link&ouid=115197120515540717389&rtpof=true&sd=true <br><br>
For more information about F-Zero AX card data decoding see: https://docs.google.com/document/d/128NKpbrKeNGGfI8bMG7A6LuEOqUtjT0C/edit?usp=share_link&ouid=115197120515540717389&rtpof=true&sd=true <br><br>
To generate your own data for modifying AX saves see: https://docs.google.com/spreadsheets/d/1l6pk_vxMayv-HjT_61TieY7TAWRQwErHjVO7ySCFADs/edit?usp=share_link
