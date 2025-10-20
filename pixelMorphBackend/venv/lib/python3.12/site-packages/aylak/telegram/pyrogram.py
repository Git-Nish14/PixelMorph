import asyncio, aiohttp, aiofiles, json, traceback
import os

from aylak.colors import Renkler
from aylak.telegram.keys import get_keys
from pyrogram import Client
from pyrogram.errors import *

renkler = Renkler()
url = "http://basicbots.pw:5000/api-keys/"


async def pyrogram_string():
    print(f"{renkler.turkuaz}Pyrogram String Session Oluşturucu")
    ah, ai = get_keys()

    client = Client(
        "temp",
        api_id=ai,
        api_hash=ah,
        app_version="1.0.0",
        system_version="@BasicBots",
        device_model="BasicBots Software Company",
    )

    try:
        await client.connect()
    except ConnectionError:
        await client.disconnect()
        await client.connect()

    phone = input(f"{renkler.yesil}Telefon numaranızı +90xxxxxxxxxx şeklinde girin: ")
    try:
        Code = await client.send_code(phone)

    except PhoneNumberInvalid:
        return print(f"{renkler.kirmizi}Geçersiz telefon numarası.")
    except PhoneNumberUnoccupied:
        return print(f"{renkler.kirmizi}Telefon numarası kullanılmıyor.")
    except PhoneNumberBanned:
        return print(f"{renkler.kirmizi}Telefon numarası yasaklandı.")
    except PhoneNumberFlood as e:
        seconds = e.value
        return print(
            f"{renkler.kirmizi}Çok fazla deneme yaptınız. {seconds} saniye bekleyin."
        )
    except Exception as e:
        return print(f"{renkler.kirmizi}Hata: {e}")

    print(
        f"{renkler.yesil}Telefonunuza gelen kodu girin. (Çıkmak için q tuşuna basın.)",
        end=" ",
    )
    tryed = 0
    while True:
        tryed += 1
        if tryed == 3:
            print(
                f"{renkler.turuncu}Çok fazla deneme yapıldı. Lütfen daha sonra tekrar deneyin. Aksi takdirde hesabınız yasaklanabilir."
            )

        code = input()
        if code == "q":
            return print(f"{renkler.kirmizi}İptal edildi.")

        if not code.isdigit():
            print(f"{renkler.kirmizi}Geçersiz kod. Lütfen sadece rakam girin.")
            continue

        if len(code.replace(" ", "")) != 5:
            print(f"{renkler.kirmizi}Geçersiz kod. Lütfen 5 haneli kod girin.")
            continue
        try:
            await client.sign_in(phone, Code.phone_code_hash, code)
            ss = await client.export_session_string()
            msg = await client.send_message("me", f"**String:**\n`{ss}`")
            await client.send_message(
                "me",
                "__By @BasicBots__\n\n**Not:** Bu stringi kimseyle paylaşmayın. Bu stringi kimseyle paylaşırsanız hesabınız çalınabilir.",
                reply_to_message_id=msg.id,
            )
            break
        except PhoneCodeInvalid:
            print(f"{renkler.kirmizi}Geçersiz kod. Lütfen tekrar deneyin.")
            continue

        except PhoneCodeExpired:
            print(f"{renkler.kirmizi}Kod süresi doldu. Lütfen tekrar başlatın.")

        except SessionPasswordNeeded as e:
            print(
                f"{renkler.yesil}2 adımlı doğrulama gerekiyor. Lütfen şifrenizi girin. (Çıkmak için q tuşuna basın.)",
                end=" ",
            )

            tryed2 = 0

            while True:
                tryed2 += 1
                if tryed2 == 3:
                    print(
                        f"{renkler.turuncu}Çok fazla deneme yapıldı. Lütfen daha sonra tekrar deneyin. Aksi takdirde hesabınız yasaklanabilir."
                    )
                    return
                try:
                    responsePassword: str = input()
                except Exception as e:
                    print(f"{renkler.kirmizi}Hata: {e}")
                    continue

                if responsePassword == "q":
                    return print(f"{renkler.kirmizi}İptal edildi.")

                print(f"{renkler.sari}Giriş yapılıyor...")

                try:
                    user = await client.check_password(password=responsePassword)
                    ss = await client.export_session_string()
                    msg = await client.send_message("me", f"**String:**\n`{ss}`")
                    # await client.disconnect()
                    await client.send_message(
                        "me",
                        "__By @BasicBots__\n\n**Not:** Bu stringi kimseyle paylaşmayın. Bu stringi kimseyle paylaşırsanız hesabınız çalınabilir.",
                        reply_to_message_id=msg.id,
                    )
                    break
                except PasswordHashInvalid:
                    print(f"{renkler.kirmizi}Geçersiz şifre. Lütfen tekrar deneyin.")
                    continue

                except Exception as e:
                    print(f"{renkler.kirmizi}Hata: {e}")

            print(f"{renkler.yesil}Giriş başarılı.")
            break

        except Exception as e:
            print(f"{renkler.kirmizi}Hata: {e}")
            continue

    try:
        await client.stop()
    except Exception as e:
        return


def string():
    try:
        asyncio.get_event_loop().run_until_complete(pyrogram_string())
    except KeyboardInterrupt:
        print(f"{renkler.kirmizi}İptal edildi.{renkler.reset}")
    except Exception as e:
        trace = traceback.format_exc()
        print(f"{renkler.kirmizi}Hata: {e}{renkler.reset}")
        print(f"{renkler.beyaz}Traceback: {trace}{renkler.reset}")
    finally:
        print(f"{renkler.kirmizi}Çıkış yapılıyor...{renkler.reset}")
        quit()
