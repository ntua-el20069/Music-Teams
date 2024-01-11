import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:myapp/components/back-title-options.dart';
import 'package:myapp/components/backpage-title.dart';
import 'package:myapp/components/button.dart';
import 'package:myapp/components/error.dart';
import 'package:myapp/components/options-button.dart';
import 'package:myapp/pages/options.dart';
import 'package:myapp/pages/song.dart';
import 'package:myapp/pages/team-home.dart';
import 'package:myapp/url.dart';


String finalUrl = baseUrl + '/API/recent-song-demands';

Future<SongDemandAlbum> fetchAlbum() async {
  final response = await http.get(Uri.parse(finalUrl));

  if (response.statusCode == 200) {
    return SongDemandAlbum.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  } else {
    throw Exception('Failed to load album');
  }
}

class SongDemandAlbum {
  final List<dynamic> songs;

  const SongDemandAlbum({
    required this.songs,
  });

  factory SongDemandAlbum.fromJson(Map<String, dynamic> json) {
    if (json.containsKey('demanded-songs')) {
      return SongDemandAlbum(
        songs: json['demanded-songs'].split('\n') as List<dynamic>,
      );
    } else {
      throw FormatException('Failed to load album.');
    }
  }
}

class LivePage extends StatefulWidget {
  @override
  _LiveState createState() => _LiveState();
}

class _LiveState extends State<LivePage> {
  Future<SongDemandAlbum>? futureAlbum;
  List<dynamic> songs = [];

  @override
  void initState() {
    super.initState();
    // Delaying the fetch to ensure it happens after the initial build
    Future.delayed(Duration.zero, () {
      setState(() {
        futureAlbum = fetchAlbum();
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Live (Recent Song Demands)'),
        backgroundColor: Color(0xff451475),
      ),
      body: FutureBuilder<SongDemandAlbum>(
        future: futureAlbum,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (snapshot.hasData) {
            songs = snapshot.data!.songs;
            return ListView.builder(
              itemCount: songs.length,
              itemBuilder: (BuildContext context, int index) {
                String title = songs[index];
                return Container(
                  margin: EdgeInsets.symmetric(vertical: 8.0),
                  child: SizedBox(
                    width: 200, // Specify your desired width
                    height: 50, // Specify your desired height
                    child: CustomGradientButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => SongPage(songId: selectSong(title))),
                        );
                      },
                      buttonText: title,
                      fontSize: 14,
                      // Other button properties...
                    ),
                  ),
                );
              },
            );
          } else {
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }
}
