from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, abort
from flask_httpauth import HTTPBasicAuth
import mysql.connector
#import psycopg2 

from help_routes import *

major = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def transpose(chords: str, transporto: int) -> str:
    transposed_chords = ''
    i = 0
    while (i < len(chords)):   # for each letter in chords string
        if chords[i:i+2] in major:      # check if it is A#, C#, ...
            k = major.index(chords[i:i+2])
            transposed_chords += major[(k + transporto) % 12]
            i += 2
        elif chords[i] in major:      # check if it is A, B, C, ...
            k = major.index(chords[i])
            transposed_chords += major[(k + transporto) % 12]
            i += 1
        else:                         # else write the same character
            transposed_chords += chords[i]
            i += 1
    return transposed_chords


def song_transpose(song_id, permanent = False, transporto = 0, live = False, live_id = -3):
    transporto = request.form.get('transporto') if request.method == 'POST' else 0
    type_transporto = "Permanent" if permanent else "Temporary"
    """
    title = "Αυτά τα δέντρα"
    composer = "Μίκης Θεοδωράκης"
    lyricist = "Γιάννης Ρίτσος"
    lyrics = '''Αυτά τα δέντρα δεν βολεύονται με λιγότερο ουρανό
Αυτές οι πέτρες δεν βολεύονται, κάτω απ' τα, απ' τα ξένα βήματα
Αυτά τα πρόσωπα δεν βολεύονται παρά μόνο στον η η η λιο
Αυτές οι καρδιές δεν βολεύονται παρά μόνο στο δί ι ι ι κιο'''
    chords = '''Dm      A#              C         Dm      C   Dm
Dm                  A#    C       Dm      C   Dm

'''
    """
    
    title, lyrics, chords, composers, lyricists = get_song_by_id(song_id)
    try:
        transporto = int(transporto)
        if chords: chords = transpose(chords, transporto)
        else: chords = '\n'.join( ( len(lyrics.split('\n')) ) * [''] )
    except:
        return "<h1> Please insert valid transporto number </h1>"
    if permanent:
        # here I should update the chords string into the Database...
        update_chords(song_id, chords)
        transporto = 0
    return render_template('song-transpose.html', title=title, composers=composers, lyricists=lyricists, lyrics=lyrics, chords=chords, zip=zip, transporto=transporto, song_id=song_id, type_transporto=type_transporto, live = live, live_id = live_id)
