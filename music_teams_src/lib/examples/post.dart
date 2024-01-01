import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:myapp/url.dart';

// HTTP POST Request example

Future<Album> createAlbum(String title, String composer, String lyricist, String lyrics, ) async {
  final response = await http.post(
    Uri.parse(baseUrl + '/music-teams/add-song'),
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

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() {
    return _MyAppState();
  }
}

class _MyAppState extends State<MyApp> {
  Future<Album>? _futureAlbum;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Create Data Example',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Create Data Example'),
        ),
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
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        TextField(
          controller: titleController,
          decoration: const InputDecoration(hintText: 'Title'),
        ),
        TextField(
          controller: composerController,
          decoration: const InputDecoration(hintText: 'Composer'),
        ),
        TextField(
          controller: lyricistController,
          decoration: const InputDecoration(hintText: 'Lyricist'),
        ),
        TextField(
          controller: lyricsController,
          minLines: 10,
          maxLines: 1000,
          decoration: const InputDecoration(hintText: 'Lyrics'),
        ),
        ElevatedButton(
          onPressed: () {

            String title = titleController.text;
            String composer = composerController.text;
            String lyricist = lyricistController.text;
            String lyrics = lyricsController.text;

            setState(() {
              _futureAlbum = createAlbum(title, composer, lyricist, lyrics);
            });
          },
          child: const Text('Create Data'),
        ),
      ],
    );
  }

  FutureBuilder<Album> buildFutureBuilder() {
    return FutureBuilder<Album>(
      future: _futureAlbum,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text(snapshot.data!.message);
        } else if (snapshot.hasError) {
          return Text('${snapshot.error}');
        }

        return const CircularProgressIndicator();
      },
    );
  }
}