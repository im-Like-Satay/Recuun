# from gmail import gmail
from plumbum import ProcessExecutionError, local

from core.gmail import gmail


def process(domain: str, email: str):
    current_dir = local.path(__file__).dirname

    subfinder = local[current_dir / "tool" / "subfinder.exe"]
    httpx = local[current_dir / "tool" / "httpx.exe"]

    try:
        cmd = (
            subfinder["-d", domain, "-silent", "-all", "-nc"]
            | httpx["-silent", "-sc", "-nc"]
        )

        output = cmd()

        if output.strip():
            print("[INFO] Hasil ditemukan, mengirim email...")
            gmail(email, output)
        else:
            print("[WARN] Tidak ada subdomain aktif yang ditemukan.")

    except ProcessExecutionError as e:
        print(f"[ERROR] Gagal mengeksekusi perintah: {e}")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan sistem: {e}")
