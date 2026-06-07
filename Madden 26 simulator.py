print("""
╔══════════════════════════════════════╗
║         MADDEN FOOTBALL '26          ║
║      Python Terminal Edition         ║
╚══════════════════════════════════════╝
""")
import time
from Colors import C

print(C.clr("Welcome to a Python Madden 26 simulator! "), C.GREEN, C.BG_GOLD, C.BOLD)
time.sleep(2)
print(C.clr("Here you will experience the game Madden 26 but in Python!"), C.GREEN, C.BG_GOLD, C.BOLD)
time.sleep(2)
print(C.clr("Now lets start of by choosing the teams"))
time.sleep(1)
print(str(input(C.clr("Do you want be HOME or AWAY: "))))
