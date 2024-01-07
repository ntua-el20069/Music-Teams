import 'package:flutter/material.dart';
import 'package:myapp/components/button.dart';
import 'package:myapp/functions/greekLyrics.dart';
import 'package:myapp/pages/team-home.dart';
import 'package:myapp/prototype/add-chords-page.dart';
import 'package:myapp/prototype/add-song-page.dart';
import 'package:myapp/utils.dart';
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:myapp/url.dart';


Future<Album> createAlbum(String title, String composer, String lyricist, String lyrics, ) async {
  final response = await http.post(
    Uri.parse(baseUrl + '/API/add-song'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'title': title,
      'composer' : composer,
      'lyricist' : lyricist,
      'lyrics' : lyrics,
      'search_title' : title,
      'button-info' : ''
    }),
  );

  if (response.statusCode == 201) {
    // If the server did return a 201 CREATED response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 201 CREATED response,
    // then throw an exception.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
    //throw Exception('Failed to create album.');
  }
}

Future<ScrapedSong> sendHTMLviaPostRequest({String title = 'Ρόζα'}) async {
  //String htmlContent = '<html><body><h1>Hello, World!</h1></body></html>'; // Replace this with your HTML content
  String? htmlContent = await takeFromGreekLyricsMobile(title);

  var url = Uri.parse(baseUrl + '/API/webscrape'); // Replace with your server endpoint

  try {
    var response = await http.post(
      url,
      headers: <String, String>{
        'Content-Type': 'text/html', // Set the content type to text/html
      },
      body: htmlContent,
    );

    if (response.statusCode == 200) {
      print('HTML sent successfully');
      print('Response: ${response.body}');
      return ScrapedSong.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
    } else {
      print('Failed to send HTML. Status code: ${response.statusCode}');
      return ScrapedSong.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
    }
  } catch (error) {
    print('Error sending HTML: $error');
    throw Exception('Error sending HTML: $error');
  }
}

class Album {
  final String message;
  final String error;

  const Album({required this.message, required this.error});

  factory Album.fromJson(Map<String, dynamic> json) {
    if (json.containsKey('message') ) {
      return Album(
        message: json['message'] as String,
        error: 'All OK'
      );
    } else if (json.containsKey('error')){
      return Album(
        message: 'Error',
        error: json['error'] as String
      );
    } else {
      throw FormatException('Failed to load album.');
    }
  }
}

class ScrapedSong {
  final String title;
  final String composer;
  final String lyricist;
  final String lyrics;
  final String error;

  const ScrapedSong({
    required this.title,
    required this.composer,
    required this.lyricist,
    required this.lyrics,
    required this.error,
  });

  factory ScrapedSong.fromJson(Map<String, dynamic> json) {
    if (json.containsKey('title') &&
        json.containsKey('composer') &&
        json.containsKey('lyricist') &&
        json.containsKey('lyrics')) {
      return ScrapedSong(
        title: json['title'] as String,
        composer: json['composer'] as String,
        lyricist: json['lyricist'] as String,
        lyrics: json['lyrics'] as String,
        error: json['error'] == '' ? 'All OK' : json['error'] as String,
      );
    } else {
      throw FormatException('Failed to load scraped song.');
    }
  }
}



class AddSongPage extends StatefulWidget {
  @override
  _AddSongPage createState() => _AddSongPage();
}

class _AddSongPage extends State<AddSongPage> {
  Future<Album>? _futureAlbum;
  Future<ScrapedSong>? _futureScrapedSong;

 @override
  Widget build(BuildContext context) {
    return MaterialApp(
  home: Scaffold(
    body: SingleChildScrollView(
      child: Container(
        alignment: Alignment.center,
        padding: const EdgeInsets.all(8),
        child: (_futureAlbum == null && _futureScrapedSong == null)
            ? buildColumn()
            : (_futureAlbum == null)
                ? buildColumn(futureScrapedSong: _futureScrapedSong)
                : buildFutureBuilder(),
      ),
    ),
  ),
);

  }

TextEditingController titleController = TextEditingController();
TextEditingController composerController = TextEditingController();
TextEditingController lyricistController = TextEditingController();
TextEditingController lyricsController = TextEditingController();



  Column buildColumn({Future<ScrapedSong>? futureScrapedSong}) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;

  if (futureScrapedSong != null) {
    futureScrapedSong.then((scrapedSong) {
      if (true) {
        titleController.text = scrapedSong.title;
        composerController.text = scrapedSong.composer;
        lyricistController.text = scrapedSong.lyricist;
        lyricsController.text = scrapedSong.lyrics;
      }
    });
  }
    return Column(
      
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[

        TextButton(
              // backbuttontextuNt (121:6397)
              onPressed: () {
                Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHomePage()), );
              },
              style: TextButton.styleFrom (
                padding: EdgeInsets.zero,
              ),
              child: Container(
                width: double.infinity,
                height: 100*fem,
                child: Stack(
                  children: [
                    Positioned(
                      // backbuttonbarr3E (I121:6397;64:383)
                      left: 15*fem,
                      top: 0*fem,
                      child: Align(
                        child: SizedBox(
                          width: 384.7*fem,
                          height: 80*fem,
                          child: Image.asset(
                            'assets/prototype/images/back-button-bar-Ktx.png',
                            width: 384.7*fem,
                            height: 80*fem,
                          ),
                        ),
                      ),
                    ),
                    Positioned(
                      // textXQG (I121:6397;64:372)
                      left: 111*fem,
                      top: 10*fem,
                      child: Align(
                        child: SizedBox(
                          width: 155*fem,
                          height: 50*fem,
                          child: Text(
                            'New song',
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 36*ffem,
                              fontWeight: FontWeight.w700,
                              height: 1.3888888889*ffem/fem,
                              color: Color(0xff451475),
                            ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
        /* Text(
          'Title',
          style: SafeGoogleFont (
            'Zilla Slab',
            fontSize: 20*ffem,
            fontWeight: FontWeight.w400,
            height: 1.2*ffem/fem,
            color: Color(0xff4e36b0),
          ),
        ), */

TextField(
  controller: titleController,
  decoration: const InputDecoration(
    hintText: 'Title',
    contentPadding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0), // Adjust top and bottom padding
  ),
),

        
        CustomGradientButton(
          onPressed: () {
            String title = titleController.text;
            setState(() {  
               _futureScrapedSong = sendHTMLviaPostRequest(title: title);
            });
          },
          buttonText: 'Find greek lyrics from title',
          fontSize: 14,
        ),

        /* Text(
          'Composer',
          style: SafeGoogleFont (
            'Zilla Slab',
            fontSize: 20*ffem,
            fontWeight: FontWeight.w400,
            height: 1.2*ffem/fem,
            color: Color(0xff4e36b0),
          ),
        ),     */   
        TextField(
          controller: composerController,
          decoration: const InputDecoration(hintText: 'Composer'),
        ),
        /* Text(
          'Lyricist',
          style: SafeGoogleFont (
            'Zilla Slab',
            fontSize: 20*ffem,
            fontWeight: FontWeight.w400,
            height: 1.2*ffem/fem,
            color: Color(0xff4e36b0),
          ),
        ),   */     
        TextField(
          controller: lyricistController,
          decoration: const InputDecoration(hintText: 'Lyricist'),
        ),
        /*Text(
          'Lyrics',
          style: SafeGoogleFont (
            'Zilla Slab',
            fontSize: 20*ffem,
            fontWeight: FontWeight.w400,
            height: 1.2*ffem/fem,
            color: Color(0xff4e36b0),
          ),
        ),  */
        TextField(
          controller: lyricsController,
          minLines: 10,
          maxLines: 1000,
          decoration: const InputDecoration(hintText: 'Lyrics'),
        ),
        
        CustomGradientButton(
            onPressed: () {
              String title = titleController.text;
              String composer = composerController.text;
              String lyricist = lyricistController.text;
              String lyrics = lyricsController.text;

              setState(() {
                _futureAlbum = createAlbum(title, composer, lyricist, lyrics);
                //sendHTMLviaPostRequest(title: title);
              });
            },
            buttonText: 'Add chords',
            fontSize: 24,
          ),
    
      ],
    );
  }

  FutureBuilder<Album> buildFutureBuilder() {
    return FutureBuilder<Album>(
      future: _futureAlbum,
      builder: (context, snapshot) {
        if (snapshot.hasData) {

          if (snapshot.data!.message == 'Successful Insertion!') {
            return AddChords(); 
          } else {
            // Handle other cases or show an error message
            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(snapshot.data!.message),
                  TextButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => AddSongPage()),
                      );
                    },
                    child: Text('Back'),
                  ),
                ],
              ),
            );

          }
        } else if (snapshot.hasError) {
          return Text('${snapshot.error}');
        }

        return const CircularProgressIndicator();
      },
    );
  }
}

