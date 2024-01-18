import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:myapp/components/dark-app-bar.dart';
import 'package:myapp/route-generator.dart';
import 'package:myapp/url.dart';
import 'package:audioplayers/audioplayers.dart';



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
  final int songId;

  SongPage({required this.songId, Key? key}) : super(key: key);

  @override
  State<SongPage> createState() => _SongState();
}

class _SongState extends State<SongPage> {
  late Future<Album> futureAlbum;
  TextEditingController transportoController = TextEditingController();
  Future<Album>? _futureAlbum;
  int? selectedSongId;
  bool _isPlaying = false;
  late AudioPlayer _audioPlayer;
  String? recordingUrl;
  String? initialButtonText;
  bool? recordingOK;
  bool mounted = true; // beacomes false after dispose
  bool existsRecording = false;

@override
void initState() {
  super.initState();

  //widget.songId.then((value) {
    if(mounted) setState(() {
      selectedSongId = widget.songId;
      futureAlbum = fetchAlbum(selectedSongId!);
      recordingUrl = baseUrl + '/API/' + selectedSongId.toString() + '/recording';
      _audioPlayer = AudioPlayer();
      }); 
        // Fetch recording asynchronously without blocking the main content
      seekForRecording().then((recordingOK) {
        if (mounted) setState(() {
          initialButtonText = recordingOK ? 'Play Recording' : 'No Recording';
          existsRecording = recordingOK;
        });
      });
    


}


// Function to load the main content







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
          //dispose();
          Navigator.of(context).pushReplacementNamed('/live');
        } else if (details.delta.dx < -sensitivity) {
          // Left Swipe
          //dispose();
          Navigator.of(context).pushReplacementNamed('/song-demand');
        }
      },
    child: MaterialApp(
      onGenerateRoute: RouteGenerator.onGenerateRoute,
      //navigatorKey: GlobalKey<NavigatorState>(),
      title: 'Song Page',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Color(0xFF451475)),
      ),
      home: Scaffold(
        body: Container(
          alignment: Alignment.center,
          padding: const EdgeInsets.all(0),
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
            appBar: PurpleAppBar(header: title, onLeadingTap: () {  Navigator.of(context).pushReplacementNamed('/options');},),
            body: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Padding(
                  padding: EdgeInsets.all(4.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'Swipe for Live >>',
                        textAlign: TextAlign.start,
                        style: TextStyle(
                          fontSize: 12,
                          fontFamily: 'monospace',
                          color: Color(0xff451475),
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(
                        '<< Swipe for Song Demand',
                        textAlign: TextAlign.start,
                        style: TextStyle(
                          fontSize: 12,
                          fontFamily: 'monospace',
                          color: Color(0xff451475),
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),

                Expanded(
                  child: ListView.builder(
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
                ),
              ],
            ),
            bottomNavigationBar: Padding(
              padding: EdgeInsets.all(0.0),
              child: Container(
                color: Colors.purple[100],
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    SizedBox(width: 4.0),
                    ElevatedButton(
                      onPressed: _isPlaying ? _stopAudio : _fetchAndPlayAudio,
                      child: Text(_isPlaying ? 'Stop' : (initialButtonText ?? 'Seeking for recording')),
                    ),
                    SizedBox(width: 4.0),
                    Expanded(
                      child: TextField(
                        controller: transportoController,
                        keyboardType: TextInputType.number,
                        decoration: InputDecoration(
                          hintText: 'Number',
                          border: OutlineInputBorder(),
                          contentPadding: EdgeInsets.symmetric(vertical: 10.0, horizontal: 12.0), // Adjust the values as needed
                        ),
                      ),
                    ),
                    SizedBox(width: 4.0),
                    ElevatedButton(
                      onPressed: () {
                        String transporto = transportoController.text;
                        setState(() {
                          _futureAlbum = createAlbum(selectedSongId ?? 0, transporto);
                        });
                      },
                      child: Text('Transporto'),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Color(0xff451475), // Set background color here
                      ),
                    ),
                    SizedBox(width: 4.0),
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

  Future<void> _stopAudio() async {
    await _audioPlayer.stop();
    setState(() {
      _isPlaying = false;
    });
  }

  @override
  void dispose() {
    try {
    mounted = false;
    _audioPlayer.dispose();
    super.dispose();
    }
    catch (e){
      print("Could not dispose audio.");
    }
  }

  Future<void> _fetchAndPlayAudio() async {
    try {
      if (!existsRecording) return ;
      String url = recordingUrl ?? '';
      /* final response = await http.get(Uri.parse(url));

      if (response.statusCode == 200) {*/
        final audioUrl = url; // You can use the apiUrl directly as a URL
        await _audioPlayer.play(UrlSource(audioUrl));
        setState(() {
          _isPlaying = true;
        });
      /*} else {
        print('Failed to fetch audio: ${response.statusCode}');
      }*/
    } catch (e) {
      print('Error fetching audio: $e');
    }
  }


  Future<bool> seekForRecording() async {
    try {
      if (!mounted) return false;
      String url = recordingUrl ?? '';
      final response = await http.get(Uri.parse(url));
      if (!mounted) return false;
      if (response.statusCode == 200) {
        print("ok recording");
        return true;  
      } else {
        print('Failed to fetch audio: ${response.statusCode}');
        return false;
      }
    } catch (e) {
      print('Error fetching audio: $e');
      return false;
    }
  }
}
