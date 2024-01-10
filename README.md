# Music-Teams
Organize your own lyrics, chords, small recordings and share them with your musical partners.

# Web host Code

1. In the local code `lib/url.dart` change `baseUrl` for requests from `http://10.0.2.2:5001` to `https://nikolaospapa3.pythonanywhere.com` and git add, commit, push
2. In pythonanywhere, Open a console  and  remove `Music-Teams`
3. git clone the repo
4. Remove useless folders/files
5. Change `backend/__init__.py` in order to connect to the host Database 
6. Ensure that in WSGI file `project_home` is set to the right path, as well as `Source Code`.
7. Reload website

### Bash commands for 2,3,4
```bash
rm -r /home/nikolaospapa3/Music-Teams
git clone https://github.com/ntua-el20069/Music-Teams.git
cd Music-Teams
rm -r music_teams_src
```

# Restore Database from the backup In the host database console (MySQL interpreter) 
```bash
source ~/Music-Teams/backup_db_instance/musicteams-backup-2-11-2023.sql;
```
