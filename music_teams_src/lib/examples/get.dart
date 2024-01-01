import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:myapp/url.dart';

// HTTP GET Request example

Future<Album> fetchAlbum() async {
  final response = await http
      //.get(Uri.parse('https://jsonplaceholder.typicode.com/albums/1'));
      .get(Uri.parse(baseUrl + '/music-teams'));

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}

class Album {
  final List<dynamic> ids;
  final String selected;
  final List<dynamic> songs;

  const Album({
    required this.ids,
    required this.selected,
    required this.songs,
  });


  factory Album.fromJson(Map<String, dynamic> json) {
    if (json.containsKey('ids') &&
        json.containsKey('selected') &&
        json.containsKey('songs')) {
      return Album(
        ids: json['ids'] as List<dynamic>,
        selected: json['selected'] as String,
        songs: json['songs'] as List<dynamic>,
      );
    } else {
      throw FormatException('Failed to load album.');
    }
  }
}


void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  late Future<Album> futureAlbum;

  @override
  void initState() {
    super.initState();
    futureAlbum = fetchAlbum();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fetch Data Example',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Fetch Data Example'),
        ),
        body: Center(
          child: FutureBuilder<Album>(
            future: futureAlbum,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                //return Text(snapshot.data!.selected);
                List<dynamic> songs = snapshot.data!.songs; // Replace with your list of songs

                return ListView.builder(
                  itemCount: songs.length,
                  itemBuilder: (BuildContext context, int index) {
                    return Text(
                      songs[index],
                      style: TextStyle(fontSize: 16), // Customize the text style if needed
                    );
                  },
                );
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }
                else {
                  // Return some default widget if data is not available
                  return CircularProgressIndicator(); // Placeholder or loading indicator
                }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}