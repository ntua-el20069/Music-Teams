# Music-Teams
Organize your own lyrics, chords, small recordings and share them with your musical partners.

# Web host Code

1. In the local code `lib/url.dart` change `baseUrl` for requests from `http://10.0.2.2:5001` to `https://nikolaospapa3.pythonanywhere.com` and git add, commit, push
2. In pythonanywhere, Remove folder `Music-Teams`
3. Open a console and git clone the repo
4. Remove useless folders/files
5. Change `backend/__init__.py` in order to connect to the host Database 
6. Ensure that in WSGI file `project_home` is set to the right path, as well as `Source Code`.
7. Reload website

