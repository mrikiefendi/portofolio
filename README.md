# M Riki Efendi Portfolio — Django

Website portfolio dark theme dengan aksen cyan/red, responsive, serta dashboard CRUD.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install -r requirements.txt
python manage.py makemigrations portfolio
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Buka:
- Website: http://127.0.0.1:8000/
- Dashboard custom: http://127.0.0.1:8000/dashboard/
- Django Admin: http://127.0.0.1:8000/admin/

Login dashboard memakai akun superuser yang dibuat saat `createsuperuser`.

## 2. Mengisi konten
Login ke `/dashboard/`, lalu kelola Profile, Skills, Projects, Education, Experience, dan Leadership.
Untuk foto profil dan gambar proyek, unggah melalui form. File masuk ke folder `media/`.

## 3. Catatan
- Database bawaan menggunakan SQLite agar langsung bisa dijalankan tanpa memasang MySQL.
- Tampilan mengikuti referensi screenshot yang diberikan. Foto dan gambar proyek belum disertakan; unggah aset milikmu sendiri dari dashboard.
- Isi pendidikan, pengalaman, organisasi, kontak, dan project contoh perlu kamu masukkan sendiri agar tidak memakai data yang belum tentu benar.
- Sebelum deploy, ubah `SECRET_KEY`, matikan `DEBUG`, atur `ALLOWED_HOSTS`, dan siapkan penyimpanan media.