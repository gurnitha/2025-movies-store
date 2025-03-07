# 2025-movies-store
Membuat aplikasi Movies Store menggunakan Django versi 5


## 1. SETUP

#### 1.1. Membuat remote repositori (done)

#### 1.2. Membuat local workspace (done)

#### 1.3. Mengklon remote repositori (done)

#### 1.4. Git commit to local repositi (done)

#### 1.5. Upload local repositori ke remote repositori (done)

#### 1.6. Membuat lingkungan virtual dengan nama venv312516 (done)

#### 1.7. Mengaktifkan venv312516 (done)

#### 1.7. Menon-aktifkan venv312516 (done)

#### 1.8. Menginstal Django versi 5.1.6 

#### 1.9. Mengupgrade pip


## 2. PROYEK DJANGO

#### 2.1. Menginisiasi proyek django

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 2.2. Menjalankan django development server

        (venv312516) λ python manage.py runserver

#### 2.3. Tentang proyek Movies Store

#### 2.4. Django MVT (Models, Views, Templates)


## 2. STRUKTUR PROYEK DAN APLIKASI DJANGO

#### 2.1. Membuat aplikasi django

        modified:   README.md
        new file:   app/home/__init__.py
        new file:   app/home/admin.py
        new file:   app/home/apps.py
        new file:   app/home/migrations/__init__.py
        new file:   app/home/models.py
        new file:   app/home/tests.py
        new file:   app/home/views.py
        modified:   config/settings.py

#### 2.2. Mendaftarkan aplikasi pada config/settings.py

        modified:   README.md
        modified:   config/settings.py

#### 2.3. Membuat laman home

        modified:   README.md
        new file:   app/home/urls.py
        modified:   app/home/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/home/home.html

#### 2.4. Membuat laman about

        modified:   README.md
        modified:   app/home/urls.py
        modified:   app/home/views.py
        new file:   templates/home/about.html

#### 2.5. Membuat laman contact

        modified:   README.md
        modified:   app/home/urls.py
        modified:   app/home/views.py
        modified:   templates/home/about.html
        new file:   templates/home/contact.html


## 3. TEMPLATES

#### 3.1. Django template tags

#### 3.2. Membuat base template

        modified:   README.md
        new file:   templates/base.html

#### 3.3. Menggunakan base tempate pada laman home

        modified:   README.md
        modified:   templates/home/home.html

#### 3.4. Menggunakan base tempate pada laman about dan contact

        modified:   README.md
        modified:   templates/home/about.html
        modified:   templates/home/contact.html

#### 3.5. Menampilkan data untuk page title

        modified:   README.md
        modified:   app/home/views.py
        modified:   templates/base.html
        modified:   templates/home/about.html
        modified:   templates/home/contact.html
        modified:   templates/home/home.html

#### 3.6. Membuat navigasi dan menautkan halaman

        modified:   README.md
        modified:   templates/base.html

#### 3.7. Menambahkan dan mengunggah static files

        modified:   README.md
        modified:   config/settings.py
        new file:   static/assets/css/all.min.css
        new file:   static/assets/css/bootstrap.min.css
        new file:   static/assets/css/google-fonts.css
        new file:   static/assets/js/bootstrap.bundle.min.js
        modified:   templates/base.html

#### 3.8. Menata halaman (styling) 

        modified:   README.md
        new file:   static/assets/css/style.css
        new file:   static/assets/img/about.jpg
        new file:   static/assets/img/background.jpg
        new file:   static/assets/img/contact.png
        new file:   static/assets/img/logo.png
        modified:   templates/base.html
        modified:   templates/home/about.html
        modified:   templates/home/contact.html
        modified:   templates/home/home.html

#### 3.9. Template inheritance

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/inc/footer.html
        new file:   templates/inc/header.html


## 4. MOVIES APP

#### 4.1. Membuat aplikasi moviews

        modified:   README.md
        new file:   app/movies/__init__.py
        new file:   app/movies/admin.py
        new file:   app/movies/apps.py
        new file:   app/movies/migrations/__init__.py
        new file:   app/movies/models.py
        new file:   app/movies/tests.py
        new file:   app/movies/views.py
        modified:   config/settings.py