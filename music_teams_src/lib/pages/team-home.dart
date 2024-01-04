import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:myapp/pages/song.dart';
import 'package:myapp/prototype/song-page.dart';
import 'package:myapp/url.dart';

String finalUrl = baseUrl + '/API/home';

int returnValue = 1;

Future<int> selectSong(String title) async {
  http.Response response = await http.post(
    Uri.parse(finalUrl),
    headers: {
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode({
      'find': title,
    }),
  );

  if (response.statusCode == 200) {
    Map<String, dynamic> json = jsonDecode(response.body) as Map<String, dynamic>;
    List<dynamic> ids = json['ids'] as List<dynamic>;

    if (ids.isNotEmpty) {
      returnValue = ids[0] as int;
    } else {
      throw Exception('Failed to find Song, empty list of ids.');
    }
  } else {
    throw Exception('Failed to find Song. ${response.statusCode} status code.');
  }

  return returnValue;
}



Future<Album> fetchAlbum() async {
  final response = await http.get(Uri.parse(finalUrl));

  if (response.statusCode == 200) {
    return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
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

class TeamHomePage extends StatefulWidget {
  @override
  _TeamHomeState createState() => _TeamHomeState();
}

// ... (Other code remains the same)

class _TeamHomeState extends State<TeamHomePage> {
  late Future<Album> futureAlbum;
  TextEditingController _controller = TextEditingController();
  List<dynamic> songs = [];
  List<dynamic> filteredSongs = []; // Updated list based on search

  @override
  void initState() {
    super.initState();
    futureAlbum = fetchAlbum();
  }

  // Function to handle filtering
  void filterSongs(String value) {
    setState(() {
      if (value.isEmpty) {
        filteredSongs = songs; // Show all songs if input is empty
      } else {
        filteredSongs = songs
            .where((song) =>
                song.toLowerCase().startsWith(value.toLowerCase()))
            .toList();
            print(filteredSongs);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    String title;
    return Scaffold(
      /*appBar: AppBar(
        title: Text('Song Finder'),
      ),*/
      body: Center(
        child: FutureBuilder<Album>(
          future: futureAlbum,
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return CircularProgressIndicator();
            } else if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            } else if (snapshot.hasData) {
              songs = snapshot.data!.songs;
              filteredSongs = songs; // Initial population of filtered songs

              return Padding(
                padding: EdgeInsets.all(16.0),
                child: Column(
                  children: [
                    TextFormField(
                      controller: _controller,
                      decoration: InputDecoration(
                        labelText: 'Find Song',
                      ),
                      onChanged: (value) {
                        filterSongs(value); // Call filter function on input change
                      },
                    ),
                    Expanded(
                      child: Builder(
                        builder: (context) {
                          return ListView.builder(
                            itemCount: filteredSongs.length,
                            itemBuilder: (BuildContext context, int index) {
                              return ListTile(
                                title: Text(filteredSongs[index]),
                                onTap: () {
                                  //_controller.text = filteredSongs[index];
                                  title = filteredSongs[index];
                                  print(title);
                                  Navigator.push(context,MaterialPageRoute(builder: (context) => SongPage(songId: selectSong(title),)),);
                                  print('############################################');
                                },
                              );
                            },
                          );
                        },
                      ),
                    ),
                  ],
                ),
              );
            } else {
              return Container();
            }
          },
        ),
      ),
    );
  }
}
