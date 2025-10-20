import asyncio
import json
import os
import sys

import aiofiles
import aiohttp
from telethon import TelegramClient, events, sync
from telethon.errors import *
from telethon.sessions import StringSession

from aylak.colors import Renkler
from aylak.telegram.keys import get_keys

renkler = Renkler()


async def telethon_string():
    api_hash, api_id = get_keys()
    client = TelegramClient(
        StringSession(),
        api_id,
        api_hash,
        device_model="BasicBots Software Company",
        system_version="@BasicBots",
        app_version="1.0.0",
    )

    try:
        await client.connect()
    except OSError:
        await client.disconnect()
        await client.connect()

    phone = input(f"{renkler.yesil}Telefon numaranızı +90xxxxxxxxxx şeklinde girin: ")
    try:
        Code = await client.send_code_request(phone)
    except PhoneNumberInvalidError:
        print(f"{renkler.kirmizi}Telefon numarası geçersiz.")
        print(f"{renkler.kirmizi}Tekrar deneyin.")
        return
    except PhoneNumberBannedError:
        print(f"{renkler.kirmizi}Telefon numarası yasaklandı.")
        print(f"{renkler.kirmizi}Tekrar deneyin.")
        return
    except Exception as e:
        print(f"{renkler.kirmizi}Hata: {e}")
        print(f"{renkler.kirmizi}Tekrar deneyin.")
        return

    print(
        f"{renkler.yesil}Telefon numarasına gelen kodu girin. (Çıkmak için q tuşuna basın.)",
        end=" ",
    )

    tryed = 0
    while True:
        if tryed == 3:
            print(f"{renkler.kirmizi}3 kere yanlış giriş yaptınız.")
            print(f"{renkler.kirmizi}Tekrar deneyin.")
            return
        code = input()
        if code == "q":
            return
        try:
            await client.sign_in(phone, code, phone_code_hash=Code.phone_code_hash)
            break
        except PhoneCodeInvalidError:
            print(f"{renkler.kirmizi}Geçersiz kod.")
            print(f"{renkler.kirmizi}Tekrar deneyin.")
            tryed += 1
            continue
        except PhoneCodeExpiredError:
            print(f"{renkler.kirmizi}Kod süresi doldu.")
            print(f"{renkler.kirmizi}Tekrar deneyin.")
            tryed += 1
            return

        except SessionPasswordNeededError:
            print(
                f"{renkler.kirmizi}2 adımlı doğrulama gerekiyor. Lütfen şifrenizi girin. (Çıkmak için q tuşuna basın.){renkler.turkuaz}",
                end=" ",
            )
            tryed = 0
            while True:
                if tryed == 3:
                    print(f"{renkler.kirmizi}3 kere yanlış giriş yaptınız.")
                    print(f"{renkler.kirmizi}Tekrar deneyin.")
                    return
                password = input()
                if password == "q":
                    return
                try:
                    await client.sign_in(password=password)
                    ss = client.session.save()
                    await client.send_message("me", f"**String:**\n`{ss}`")
                    await client.send_message(
                        "me",
                        "__By @BasicBots__\
                        \n\n**Not:** Bu stringi kimseyle paylaşmayın. Bu stringi kimseyle paylaşırsanız hesabınız çalınabilir.",
                    )
                    print(f"{renkler.yesil}String oluşturuldu.")
                    sys.exit()
                    return
                except PasswordHashInvalidError:
                    print(f"{renkler.kirmizi}Geçersiz şifre.")
                    print(f"{renkler.kirmizi}Tekrar deneyin.")
                    tryed += 1
                    continue
                except Exception as e:
                    print(f"{renkler.kirmizi}Hata: {e}")
                    print(f"{renkler.kirmizi}Tekrar deneyin.")
                    return


def string():
    try:
        asyncio.run(telethon_string())
    except KeyboardInterrupt:
        print(f"{renkler.kirmizi}\nÇıkış yapılıyor...{renkler.reset}")
        quit()
    except Exception as e:
        print(f"{renkler.kirmizi}Hata: {e}{renkler.reset}")
    finally:
        print(f"{renkler.reset}", end="")
