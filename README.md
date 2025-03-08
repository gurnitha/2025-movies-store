# 2025-movies-store
Membuat aplikasi Movies Store menggunakan Django versi 5
Sumber: https://github.com/PacktPublishing/Django-5-for-the-Impatient-Second-Edition?tab=MIT-1-ov-file


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


## 3. STRUKTUR PROYEK DAN APLIKASI DJANGO

#### 3.1. Membuat aplikasi django

        modified:   README.md
        new file:   app/home/__init__.py
        new file:   app/home/admin.py
        new file:   app/home/apps.py
        new file:   app/home/migrations/__init__.py
        new file:   app/home/models.py
        new file:   app/home/tests.py
        new file:   app/home/views.py
        modified:   config/settings.py

#### 3.2. Mendaftarkan aplikasi pada config/settings.py

        modified:   README.md
        modified:   config/settings.py

#### 3.3. Membuat laman home

        modified:   README.md
        new file:   app/home/urls.py
        modified:   app/home/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/home/home.html

#### 3.4. Membuat laman about

        modified:   README.md
        modified:   app/home/urls.py
        modified:   app/home/views.py
        new file:   templates/home/about.html

#### 3.5. Membuat laman contact

        modified:   README.md
        modified:   app/home/urls.py
        modified:   app/home/views.py
        modified:   templates/home/about.html
        new file:   templates/home/contact.html


## 4. TEMPLATES

#### 4.1. Django template tags

#### 4.2. Membuat base template

        modified:   README.md
        new file:   templates/base.html

#### 4.3. Menggunakan base tempate pada laman home

        modified:   README.md
        modified:   templates/home/home.html

#### 4.4. Menggunakan base tempate pada laman about dan contact

        modified:   README.md
        modified:   templates/home/about.html
        modified:   templates/home/contact.html

#### 4.5. Menampilkan data untuk page title

        modified:   README.md
        modified:   app/home/views.py
        modified:   templates/base.html
        modified:   templates/home/about.html
        modified:   templates/home/contact.html
        modified:   templates/home/home.html

#### 4.6. Membuat navigasi dan menautkan halaman

        modified:   README.md
        modified:   templates/base.html

#### 4.7. Menambahkan dan mengunggah static files

        modified:   README.md
        modified:   config/settings.py
        new file:   static/assets/css/all.min.css
        new file:   static/assets/css/bootstrap.min.css
        new file:   static/assets/css/google-fonts.css
        new file:   static/assets/js/bootstrap.bundle.min.js
        modified:   templates/base.html

#### 4.8. Menata halaman (styling) 

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

#### 4.9. Template inheritance

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/inc/footer.html
        new file:   templates/inc/header.html


## 5. MOVIES APP

#### 5.1. Membuat aplikasi movies

        modified:   README.md
        new file:   app/movies/__init__.py
        new file:   app/movies/admin.py
        new file:   app/movies/apps.py
        new file:   app/movies/migrations/__init__.py
        new file:   app/movies/models.py
        new file:   app/movies/tests.py
        new file:   app/movies/views.py
        modified:   config/settings.py

#### 5.2. Membuat laman movies

        modified:   README.md
        new file:   app/movies/urls.py
        modified:   app/movies/views.py
        modified:   config/urls.py
        modified:   templates/inc/header.html
        new file:   templates/movies/movies.html

#### 5.3. Mengisi template untuk laman movies

        modified:   README.md
        modified:   templates/movies/movies.html

#### 5.4. Membuat dummy data movies

        modified:   README.md
        modified:   app/movies/views.py

#### 5.4. Merender movies data dummy

        modified:   README.md
        modified:   app/movies/views.py
        modified:   templates/movies/movies.html

#### 5.5. Merender singel movie data dummy

        modified:   README.md
        modified:   app/movies/urls.py
        modified:   app/movies/views.py
        new file:   templates/movies/movie.html
        modified:   templates/movies/movies.html

#### 5.6. Mencantumkan lisensi software

        new file:   MIT license.txt
        modified:   README.md


## 6. MODELS

#### 6.1. Membuat model Movie

        modified:   README.md
        new file:   app/movies/migrations/0001_initial.py
        modified:   app/movies/models.py

#### 6.2. Membuat superuser

        (venv312516) λ python manage.py createsuperuser
        
        (venv312516) λ python manage.py dbshell
        SQLite version 3.19.1 2017-05-24 13:08:33
        Enter ".help" for usage hints.
        sqlite>
        sqlite> .mode column
        sqlite> .header on
        sqlite>
        sqlite> .tables
        auth_group                  django_admin_log
        auth_group_permissions      django_content_type
        auth_permission             django_migrations
        auth_user                   django_session
        auth_user_groups            movies_movie
        auth_user_user_permissions
        sqlite>
        sqlite> pragma table_info('auth_user');
        cid         name        type        notnull     dflt_value  pk
        ----------  ----------  ----------  ----------  ----------  ----------
        0           id          integer     1                       1
        1           password    varchar(12  1                       0
        2           last_login  datetime    0                       0
        3           is_superus  bool        1                       0
        4           username    varchar(15  1                       0
        5           last_name   varchar(15  1                       0
        6           email       varchar(25  1                       0
        7           is_staff    bool        1                       0
        8           is_active   bool        1                       0
        9           date_joine  datetime    1                       0
        10          first_name  varchar(15  1                       0
        sqlite>
        sqlite> SELECT username, email FROM auth_user;
        username    email
        ----------  ------------------
        superuser   superuser@mail.com

#### 6.3. Mengkonfigursai path untuk unggahan gambar

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py

#### 6.4. Menambahkan model Movie ke panel admin dan membuat membuat sebuah movie

        modified:   README.md
        modified:   app/movies/admin.py
        modified:   config/settings.py
        new file:   media/movie_images/inception.jpg


## 7. MENGAMBIL DAN MENAMPILKAN DATA DARI DATABASE

#### 7.1. Menampilkan daftar movies pada laman movies

        modified:   README.md
        modified:   app/movies/views.py
        new file:   media/movie_images/avatar.jpg
        new file:   media/movie_images/dark.jpg
        new file:   media/movie_images/titanic.jpg
        modified:   static/assets/css/style.css
        modified:   templates/movies/movies.html

#### 7.2. Menampilkan singel movie pada laman movie

        modified:   README.md
        modified:   app/movies/views.py
        modified:   static/assets/css/style.css
        modified:   templates/movies/movie.html

#### 7.3. Membuat fungsi pencarian (search) movie

        modified:   README.md
        modified:   app/movies/views.py
        modified:   templates/movies/movies.html


## 8. DATABASE

#### 8.1. Menyesuaikan (customizing) panel admin Django Mengurutkan film berdasarkan nama

        modified:   README.md
        modified:   app/movies/admin.py

#### 8.2. Mendefinisikan pencarian berdasarkan nama

        modified:   README.md
        modified:   app/movies/admin.py

#### 8.3. Mengganti database Sqlite dengan database MySQL

        modified:   README.md
        modified:   app/movies/migrations/0001_initial.py
        modified:   config/settings.py
        new file:   media/movie_images/avatar_Wr3FVfI.jpg
        new file:   media/movie_images/dark_Xt9Fuoe.jpg
        new file:   media/movie_images/inception_zi0dd05.jpg
        new file:   media/movie_images/titanic_Crcqz5E.jp


## 9. MANAGEMEN USERS

#### 9.1. Membuat aplikasi accounts dan mengintegrasikannya dengan proyek

        modified:   README.md
        new file:   app/accounts/__init__.py
        new file:   app/accounts/admin.py
        new file:   app/accounts/apps.py
        new file:   app/accounts/migrations/__init__.py
        new file:   app/accounts/models.py
        new file:   app/accounts/tests.py
        new file:   app/accounts/views.py
        modified:   config/settings.py

#### 9.2. User signup basics (handing GET method)

        modified:   README.md
        new file:   app/accounts/urls.py
        modified:   app/accounts/views.py
        modified:   config/urls.py
        new file:   templates/accounts/signup.html
        modified:   templates/inc/header.html

#### 9.2. User signup add Post method)

        modified:   README.md
        modified:   app/accounts/urls.py
        modified:   app/accounts/views.py

        Note:

        Testing:
        Sukses membuat user baru. :)

#### 9.3. Membuat kustom CustomUserCreationForm

        modified:   README.md
        new file:   app/accounts/forms.py
        modified:   app/accounts/views.py

        Note:

        Testing:
        Sukses membuat user baru. :)

#### 9.4. Membuat cara menampilkan error

        modified:   README.md
        modified:   app/accounts/forms.py
        modified:   app/accounts/views.py

#### 9.5. User login

        modified:   README.md
        modified:   app/accounts/urls.py
        modified:   app/accounts/views.py
        new file:   templates/accounts/login.html
        modified:   templates/inc/header.html

 #### 9.6. Mengalihkan pengguna terdaftar ke halaman login

        modified:   README.md
        modified:   app/accounts/views.py

#### 9.7. User logout

        modified:   README.md
        modified:   app/accounts/urls.py
        modified:   app/accounts/views.py
        modified:   templates/inc/header.html


## 10. MOVIE REVIEWS: USER'S CRUD

#### 10.1. Membuat Review model

        modified:   README.md
        modified:   app/movies/admin.py
        new file:   app/movies/migrations/0002_review.py
        modified:   app/movies/models.py

#### 10.2. CRUD REVIEW: CREATE reviews

        modified:   README.md
        modified:   app/movies/urls.py
        modified:   app/movies/views.py
        modified:   templates/movies/movie.html

#### 10.3. CRUD REVIEW: READ reviews

        modified:   README.md
        modified:   app/movies/views.py
        modified:   templates/movies/movie.html