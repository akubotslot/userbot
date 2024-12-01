from telethon import TelegramClient
import logging
import os

# Ganti dengan informasi Anda
API_ID = '28580876'         # API ID yang didapat dari https://my.telegram.org/auth
API_HASH = 'f9d3a1e1809bca3e4b996c662f6128b8'     # API Hash yang didapat dari https://my.telegram.org/auth
PHONE_NUMBER = '+6289509532829'   # Nomor telepon yang terhubung dengan akun Telegram Anda
GROUP_ID = '@semogabisayaaa'           # Ganti dengan username grup Anda, misal @grupku

# Setting log untuk debug
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Membuat objek client
client = TelegramClient('user_bot', API_ID, API_HASH)

# Fungsi untuk mengirimkan file ke grup
async def send_file_to_group():
    # Pastikan file yang ingin dikirim ada di server
    file_path = '1.jpg'  # Ganti dengan path file yang ada di komputer Anda

    if os.path.exists(file_path):
        try:
            # Mengirimkan file ke grup
            await client.send_file(GROUP_ID, file_path)
            logger.info("File berhasil dikirim ke grup!")
        except Exception as e:
            logger.error(f"Gagal mengirim file: {e}")
    else:
        logger.warning("File tidak ditemukan!")

# Menjalankan client dan mengirimkan file
async def main():
    try:
        logger.info("Memulai bot...")
        await client.start(PHONE_NUMBER)
        logger.info("Bot berhasil login!")
        await send_file_to_group()
    except Exception as e:
        logger.error(f"Error pada client start: {e}")

# Menjalankan event loop
client.loop.run_until_complete(main())
