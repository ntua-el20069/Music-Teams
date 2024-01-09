import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:myapp/prototype/live-team-1.dart';
import 'package:myapp/url.dart';


// POST
Future<Album> createAlbum(int song_id, String transporto) async {
  String finalUrl = baseUrl + '/API/'+ song_id.toString() +'/song-transpose';
  final response = await http.post(
    Uri.parse(finalUrl),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'transporto': transporto
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




//  GET 
Future<Album> fetchAlbum(int song_id) async {
  String finalUrl = baseUrl + '/API/'+ song_id.toString() +'/song-transpose';
  final response = await http
      //.get(Uri.parse('https://jsonplaceholder.typicode.com/albums/1'));
      .get(Uri.parse(finalUrl));

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
  final String chords;
  final String composers;
  final String lyricists;
  final String lyrics;
  final String song_id;
  final String title;
  final int transporto;
  final String type_transporto;

  const Album({
    required this.chords,
    required this.composers,
    required this.lyricists,
    required this.lyrics,
    required this.song_id,
    required this.title,
    required this.transporto,
    required this.type_transporto
  });


  factory Album.fromJson(Map<String, dynamic> json) {
    if (json.containsKey('song_id') &&
        json.containsKey('lyrics') ) {
            return Album(
              chords: json['chords'] as String,
              composers: json['composers'] as String,
              lyricists: json['lyricists'] as String,
              lyrics: json['lyrics'] as String,
              song_id: json['song_id'] as String,
              title: json['title'] as String,
              transporto: json['transporto'] as int,
              type_transporto: json['type_transporto'] as String,
            );
    } else {
      throw FormatException('Failed to load album.');
    }
  }
}



class SongPage extends StatefulWidget {
  final Future<int> songId;

  SongPage({required this.songId, Key? key}) : super(key: key);

  @override
  State<SongPage> createState() => _SongState();
}

class _SongState extends State<SongPage> {
  late Future<Album> futureAlbum;
  TextEditingController transportoController = TextEditingController();
  Future<Album>? _futureAlbum;
  int? selectedSongId;

  @override
  void initState() {
    super.initState();
    // Get the integer value from the Future<int>
    widget.songId.then((value) {
      setState(() {
        selectedSongId = value;
        futureAlbum = fetchAlbum(selectedSongId!);
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    if (selectedSongId == null) {
      return Center(child: CircularProgressIndicator());
    }
    return GestureDetector(
      onHorizontalDragUpdate: (details) {
        // Sensitivity is used to determine the sensitivity of the swipe
        final double sensitivity = 10;
        if (details.delta.dx > sensitivity) {
          // Right Swipe
          Navigator.of(context).push(
            MaterialPageRoute(builder: (_) => Live()),
          );
        } else if (details.delta.dx < -sensitivity) {
          // Left Swipe
        }
      },
    child: MaterialApp(
      title: 'Create Data Example',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Color(0xFF451475)),
      ),
      home: Scaffold(
        body: Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.all(8),
          child: _futureAlbum == null ? buildFutureBuilder(futureAlbum) : buildFutureBuilder(_futureAlbum!),
        ),
      ),
    )
    );
  }

  Widget buildFutureBuilder(Future<Album> albumFuture) {
    return FutureBuilder<Album>(
      future: albumFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return CircularProgressIndicator();
        } else if (snapshot.hasData) {
          // Display fetched data
          List<String> lyrics = snapshot.data!.lyrics.split('\n');
          List<String> chords = snapshot.data!.chords.split('\n');
          String title = snapshot.data!.title;

          return Scaffold(
            appBar: AppBar(
              title: Text(title),
            ),
            body: ListView.builder(
              itemCount: lyrics.length,
              itemBuilder: (BuildContext context, int index) {
                return Padding(
                  padding: EdgeInsets.symmetric(horizontal: 10.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        chords[index],
                        style: TextStyle(
                          fontSize: 16,
                          color: Colors.red,
                          fontFamily: 'monospace',
                        ),
                      ),
                      Text(
                        lyrics[index],
                        style: TextStyle(
                          fontSize: 16,
                          fontFamily: 'monospace',
                        ),
                      ),
                    ],
                  ),
                );
              },
            ),
            bottomNavigationBar: Padding(
              padding: EdgeInsets.all(8.0),
              child: Container(
                color: Colors.purple[100],
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    Expanded(
                      child: TextField(
                        controller: transportoController,
                        keyboardType: TextInputType.number,
                        decoration: InputDecoration(
                          hintText: 'Number',
                          border: OutlineInputBorder(),
                        ),
                      ),
                    ),
                    SizedBox(width: 8.0),
                    ElevatedButton(
                      onPressed: () {
                        String transporto = transportoController.text;
                        setState(() {
                          _futureAlbum = createAlbum(selectedSongId ?? 0,transporto);
                        });
                      },
                      child: Text('Transporto'),
                    ),
                  ],
                ),
              ),
            ),
          );
        } else if (snapshot.hasError) {
          return Text('${snapshot.error}');
        } else {
          return Center(
            child: Text('No data available'),
          );
        }
      },
    );
  }
}
