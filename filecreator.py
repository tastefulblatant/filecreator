import os
import time

print("""
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
""")
time.sleep(1)
name = input("Jak se bude jmenovat Váš soubor?\n")
time.sleep(1)
koncovka = input("Jaky typ souboru by jste chteli vytvorit?(py,txt,php,doxc)\n")
time.sleep(1)
with open(f"{name}.{koncovka}","w") as file:
    print(file.write("tady to je :)"))
os.system('cls')
print("Done")
