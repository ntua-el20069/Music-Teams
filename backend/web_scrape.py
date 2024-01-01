import urllib.request
import urllib.error
import socket 
from bs4 import BeautifulSoup 
import re


greek = "ΑΆάαΒβΓγΔδΕΈέεΖζΗΉήηΘθΙΊΪίϊιΚκΛλΜμΝνΞξΟΌόοΠπΡρΣσΤτΥΎΫύϋυΦφΧχΨψΩΏώω"
#for c in greek:
#    print(f''' "{c}" : "",''')

# dictionary for greek -> greeklish
d = {"Α" : "a",
 "Ά" : "a",
 "ά" : "a",
 "α" : "a",
 "Β" : "b",
 "β" : "b",
 "Γ" : "g",
 "γ" : "g",
 "Δ" : "d",
 "δ" : "d",
 "Ε" : "e",
 "Έ" : "e",
 "έ" : "e",
 "ε" : "e",
 "Ζ" : "z",
 "ζ" : "z",
 "Η" : "h",
 "Ή" : "h",
 "ή" : "h",
 "η" : "h",
 "Θ" : "th",
 "θ" : "th",
 "Ι" : "i",
 "Ί" : "i",
 "Ϊ" : "i",
 "ί" : "i",
 "ϊ" : "i",
 "ι" : "i",
 "Κ" : "k",
 "κ" : "k",
 "Λ" : "l",
 "λ" : "l",
 "Μ" : "m",
 "μ" : "m",
 "Ν" : "n",
 "ν" : "n",
 "Ξ" : "ks",
 "ξ" : "ks",
 "Ο" : "o",
 "Ό" : "o",
 "ό" : "o",
 "ο" : "o",
 "Π" : "p",
 "π" : "p",
 "Ρ" : "r",
 "ρ" : "r",
 "Σ" : "s",
 "ς" : "s",
 "σ" : "s",
 "Τ" : "t",
 "τ" : "t",
 "Υ" : "u",
 "Ύ" : "u",
 "Ϋ" : "u",
 "ύ" : "u",
 "ϋ" : "u",
 "υ" : "u",
 "Φ" : "f",
 "φ" : "f",
 "Χ" : "x",
 "χ" : "x",
 "Ψ" : "ps",
 "ψ" : "ps",
 "Ω" : "w",
 "Ώ" : "w",
 "ώ" : "w",
 "ω" : "w",
 " " : "-",
 "0" : "0",
"1" : "1",
"2" : "2",
"3" : "3",
"4" : "4",
"5" : "5",
"6" : "6",
"7" : "7",
"8" : "8",
"9" : "9"
}

def find_html_from(url):
    # timeout : wait time in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout) 
    # The call of urllib.request.urlopen uses timeout
    # defined in library socket

    req = urllib.request.Request(url)
    try: 
        with urllib.request.urlopen(req) as response:
            char_set = response.headers.get_content_charset()
            html = response.read().decode(char_set)
        #print(html)
        return html
    
    except urllib.error.HTTPError as e:
        print('HTTP Error:', e.code)
        return "HTTP Error"
    except urllib.error.URLError as e:
        print('Cannot connect to the server')
        print('Cause: ', e)
        return "URL Error"
    else:
        print('Page loaded successfully')

def take_from_greeklyrics(search_title: str, show = False) -> (str, str, str, str):
    '''
    Takes as argument a search title (exact title in greek) e.g. "Ρόζα" 
    and returns (title, composer, lyricist, lyrics)
    using "www.greeklyrics.gr" 
    '''
    empty_result = ('','','','')  # return this in case of an error
    modified_title = ""
    for c in search_title:      
        modified_title += d[c]        # greek -> greeklish for the url(Ρόζα -> roza)
    url = "https://www.greeklyrics.gr/stixoi/"   
    html = find_html_from(url + modified_title)  
    if "Error"==html[-5:]: 
        print(f"Page cannot be reached due to {html}")
        return ("","","",f"{html}")
        
    soup = BeautifulSoup(html, 'html.parser') 

    # find title as <h1> element
    title = soup.find('h1', class_="elementor-heading-title elementor-size-default").text.strip()
    if title:
        if show: print(title)
    else:
        print("Title not found")
        
    # find composer     
    composer_tag = soup.find('b', string='Συνθέτης:')
    if composer_tag:
        composer_name = composer_tag.find_next('a').text.strip()
        if show: print(composer_name)
        #print(type(composer_name))
    else:
        print("Composer not found")

    # find lyricist
    lyricist_tag = soup.find('b', string='Στιχουργός:')
    if lyricist_tag:
        lyricist_name = lyricist_tag.find_next('a').text.strip()
        if show: print(lyricist_name)
    else:
        print("Lyricist not found")


    #find lyrics (div with specific classname) 
    class_name = "elementor-element elementor-element-a7a6650 elementor-widget elementor-widget-theme-post-content"
    div_bs4 = soup.find('div', class_ = class_name) 
    #print(type(div_bs4))
    lyrics = str(div_bs4)
    #lyrics = re.sub(r'<div[^>]*>', '', lyrics)
    lyrics = re.sub(r'</div>', '', lyrics)
    lyrics = re.sub(r'<div[^\n]*\n', '', lyrics)
    new_lines = ['<br>', '<br/>', '<br />', '<BR>', '<BR />', '</br>', '</BR>', '</p>']
    lyrics = lyrics.replace('<p>', '\n')

    for c in new_lines:
        lyrics = lyrics.replace(c, '')
    if lyrics:
        lyrics = "Intro\n" + lyrics
        if show: print(lyrics)
    else:
        print("Lyrics not found")
    
    return (title, composer_name, lyricist_name, lyrics)

#x = take_from_greeklyrics('Κιφ')
#print(x)