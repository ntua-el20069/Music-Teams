import 'package:flutter/material.dart';
import 'package:myapp/pages/team-home.dart';
import 'package:myapp/prototype/add-chords-page.dart';
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

class AddSongPage extends StatefulWidget {
  @override
  _AddSongPage createState() => _AddSongPage();
}

class _AddSongPage extends State<AddSongPage> {
  Future<Album>? _futureAlbum;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.all(8),
          child: (_futureAlbum == null) ? buildColumn() : buildFutureBuilder(),
        ),
      ),
    );
  }

TextEditingController titleController = TextEditingController();
TextEditingController composerController = TextEditingController();
TextEditingController lyricistController = TextEditingController();
TextEditingController lyricsController = TextEditingController();



  Column buildColumn() {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
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
                height: 250*fem,
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
          decoration: const InputDecoration(hintText: 'Title'),
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
        

                    TextButton(
                      onPressed: () {
                                    

                        String title = titleController.text;
                        String composer = composerController.text;
                        String lyricist = lyricistController.text;
                        String lyrics = lyricsController.text;

                        setState(() {
                          _futureAlbum = createAlbum(title, composer, lyricist, lyrics);
                        });
          
                        //Navigator.push( context, MaterialPageRoute(builder: (context) => AddChords()), );
                      },
                      style: TextButton.styleFrom (
                        padding: EdgeInsets.zero,
                      ),
                      child: Container(
                        width: 200*fem,
                        height: 64*fem,
                        decoration: BoxDecoration (
                          borderRadius: BorderRadius.circular(32*fem),
                          gradient: LinearGradient (
                            begin: Alignment(1, -1),
                            end: Alignment(-1, 1),
                            colors: <Color>[Color(0xfffe9a1a), Color(0xffc5087e)],
                            stops: <double>[0, 1],
                          ),
                        ),
                        child: Stack(
                          children: [
                            
                            Positioned(
                              // buttongzY (I80:519;59:262)
                              left: 32.5*fem,
                              top: 13*fem,
                              child: Center(
                                child: Align(
                                  child: SizedBox(
                                    width: 146*fem,
                                    height: 29*fem,
                                    child: Text(
                                      'Add chords',
                                      textAlign: TextAlign.center,
                                      style: SafeGoogleFont (
                                        'Zilla Slab',
                                        fontSize: 24*ffem,
                                        fontWeight: FontWeight.w700,
                                        height: 1.2*ffem/fem,
                                        letterSpacing: 2.4*fem,
                                        color: Color(0xffffffff),
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  
      ],
    );
  }

  FutureBuilder<Album> buildFutureBuilder() {
    return FutureBuilder<Album>(
      future: _futureAlbum,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return AddChords(); 
          /*Stack( 
            children: [
            Text(snapshot.data!.message) ,
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AddChords()),
              );
              
              },
              child: Container (child: Text('Add Chords'))
            )
            ]
          );*/
        } else if (snapshot.hasError) {
          return Text('${snapshot.error}');
        }

        return const CircularProgressIndicator();
      },
    );
  }
}

