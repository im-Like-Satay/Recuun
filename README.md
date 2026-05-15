## Recuun

pernah gak sih nyoba recon di bug bounty/vdp pake tool subfinder sama httpx dan lu nunggu hasilnya berjam-jam cuma buat nyari subdomain sementara laptop kentang lu udah mulai ngos ngosan, nah gw baru ngalamin, mangkanya daripada itu mending lu pake tool Recuun buatan gw, lu tinggal nyiapin vps/home server dan setup toolnya terus hint sekali subdomain yang mau dicari, dan tunggu hasilnya bakal kekirim lewat email.

lib : 
- fastapi
- redmail
- dotenv
- uvicorn
- plumbum

### Setup
1. Masukin email lu yang mau digunakan ke .env dan buat app password(ikuti petunjuk di .env.example) 
2. Download binary subfinder dan httpx di github dan masukan ke `core/tool/`
3. Lalukan instalasi dibawah

### Install : 
```bash
git clone https://github.com/im-Like-Satay/Recuun.git 

cd Recuun

pip install -r requirements.txt

uvicorn main:app --reload
```
## Change Flags:
- Pergi ke `core/cmd.py` di baris 14 untuk merubah/mengedit flag tool
```python
cmd = (
  subfinder["-d", domain, "-silent", "-all", "-nc"] | httpx["-silent", "-sc", "-nc"]
)
```
## API
Hint ke api `http://localhost:8000/scan?email=<emaillu@gmail.com>&domain=contoh.com`
