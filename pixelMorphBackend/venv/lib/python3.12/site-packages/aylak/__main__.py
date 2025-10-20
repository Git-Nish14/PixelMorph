import sys
from aylak.colors import Renkler

renkler = Renkler()


def main():
    argvs = sys.argv
    if len(argvs) == 1:
        print(f"{renkler.kirmizi}Kullanım: ")
        print(f"{renkler.kirmizi}pyrogram - Pyrogram String Session Oluşturucu")
        print(f"{renkler.kirmizi}telethon - Telethon String Session Oluşturucu")
        return
