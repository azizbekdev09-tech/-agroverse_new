# 🌾 AgroVerse — Fermer Marketplace

Fermerlar va xaridorlar uchun to'liq ishlaydigan onlayn bozor.

**Versiya:** 4.0  
**Status:** ✅ Ishga tayyor

---

## 📦 Loyiha tuzilmasi

```
agroverse/
├── agroverse back/          # FastAPI Backend (Python + PostgreSQL)
│   ├── app/
│   │   ├── main.py         # Asosiy fayl (uvicorn app.main:app)
│   │   ├── auth.py         # JWT + bcrypt autentifikatsiya
│   │   ├── models.py       # SQLAlchemy modellari
│   │   └── routers/        # API yo'nalishlari
│   ├── requirements.txt
│   └── .env                # ⚠️ O'zingiz yarating (quyida ko'rsatilgan)
│
├── agroverse front/         # Frontend (HTML + Vanilla JS + CSS)
│   ├── index.html
│   ├── css/style.css        # Barcha stil (yashil #10B981 mavzusi)
│   ├── js/
│   │   ├── api.js           # API so'rovlari
│   │   ├── auth.js          # Login/logout logikasi
│   │   ├── router.js        # SPA yo'naltirish
│   │   ├── i18n.js          # Ko'p tillilik (uz/ru/en)
│   │   └── pages/           # Har bir sahifa
│   └── assets/
│
├── START.ps1               # ⭐ PowerShell bilan bir bosishda ishga tushirish
├── ЗАПУСК.bat              # ⭐ CMD bilan bir bosishda ishga tushirish
├── SETUP_GUIDE.md          # Batafsil qo'llanma
├── LOYIHA_HAQIDA_UZ.md     # Loyiha haqida (o'zbek tilida)
└── README.md               # Shu fayl
```

---

## 🚀 Tez ishga tushirish

### PowerShell (tavsiya):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\START.ps1
```

### CMD:
```
ЗАПУСК.bat ga ikki marta bosing
```

Brauzer avtomatik http://127.0.0.1:5500 da ochiladi.

---

## ⚙️ .env fayl (bir marta yarating)

`agroverse back/.env` faylini yarating:
```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/agroverse
SECRET_KEY=supersecretkey123
```

PostgreSQL da bazani yarating:
```sql
CREATE DATABASE agroverse;
```

Jadvallar birinchi ishga tushirishda avtomatik yaratiladi.

---

## 🔗 Manzillar

| Manzil | Tavsif |
|--------|--------|
| http://127.0.0.1:5500 | 🌐 Sayt |
| http://127.0.0.1:8000 | 🔧 Backend |
| http://127.0.0.1:8000/docs | 📚 Swagger API hujjatlari |

---

## 👥 Foydalanuvchi rollari

| Rol | Nima qila oladi |
|-----|-----------------|
| **Fermer** | Mahsulot qo'shish, sotish, buyurtmalarni boshqarish |
| **Xaridor** | Ko'rish, savatga qo'shish, buyurtma berish |
| **Admin** | Hamma narsani nazorat qilish |

**Admin kirish:** telefon → `админ123`, parol → `127845`

---

## 🧪 Test hisoblari

Ro'yxatdan o'tish orqali yangi hisob yarating yoki mavjud testlarni ishlating:

```
Fermer:   telefon: +998901111111 | parol: 123456
Xaridor:  telefon: +998902222222 | parol: 123456
Admin:    telefon: админ123      | parol: 127845
```

---

## 🌟 Asosiy funksiyalar

- ✅ Ro'yxatdan o'tish va kirish (JWT + bcrypt)
- ✅ Foydalanuvchi rollari (fermer / xaridor / admin)
- ✅ Mahsulotlar katalogi (Bozor)
- ✅ Mahsulot qo'shish va boshqarish (fermer)
- ✅ Savat va buyurtmalar (xaridor)
- ✅ Hamyon va bonus ballari
- ✅ Tariflar (Standart / Normal / Premium)
- ✅ Admin panel (moderatsiya, blok, hisobotlar)
- ✅ AI yordamchi (interfeys — logika keyinroq)
- ✅ Ko'p tillilik: 🇺🇿 O'zbek / 🇷🇺 Rus / 🇬🇧 Ingliz
- ✅ Bloklash tizimi (sabab bilan)
- ✅ Mobil moslashuvchan dizayn

---

## 🐛 Muammolar

| Muammo | Yechim |
|--------|--------|
| Connection refused :8000 | Backend ishlamayapti, START.ps1 qayta ishlating |
| CORS xatosi | Frontend `127.0.0.1:5500` da bo'lsin, Ctrl+F5 bosing |
| 500 xatosi ro'yxatdan o'tishda | `.env` fayl bor-yo'qligini va PostgreSQL ishlayotganini tekshiring |
| START.ps1 yopiladi | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` bajaring |

---

## ⚙️ Texnik stack

| Qatlam | Texnologiya |
|--------|-------------|
| Backend | FastAPI (Python 3.10+) |
| Frontend | Vanilla JS + HTML + CSS |
| Ma'lumotlar bazasi | PostgreSQL 14+ |
| Auth | JWT tokeni + bcrypt (passlivsiz) |
| API | REST + Swagger |

---

*AgroVerse v4.0 — 2026* 🌾
