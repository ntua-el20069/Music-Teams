import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:myapp/components/back-title-options.dart';
import 'package:myapp/components/backpage-title.dart';
import 'package:myapp/components/button.dart';
import 'package:myapp/components/error.dart';
import 'package:myapp/components/options-button.dart';
import 'package:myapp/pages/live.dart';
import 'package:myapp/pages/options.dart';
import 'package:myapp/pages/song.dart';
import 'package:myapp/prototype/live-team-1.dart';
import 'package:myapp/prototype/options-page.dart';
import 'package:myapp/url.dart';

int returnValue = 1;

String finalUrl = baseUrl + '/API/home';
String demandUrl = baseUrl + '/API/make-song-demand';

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

Future<String> DemandSong(String title) async {
  try {
    http.Response response = await http.post(
      Uri.parse(demandUrl),
      headers: {
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode({'title': title}),
    );

    Map<String, dynamic> json = jsonDecode(response.body) as Map<String, dynamic>;
    print(json);
    if (response.statusCode == 200) {
        print("ok response");
        return 'OK';
    } else {
      // Handle cases for other response status codes
      print("Another status code");
      return json['error'] as String;
      //return 'Failed to find song. ${response.statusCode} status code. ${json['error']}';
    }
  } catch (e) {
    // Handle exceptions thrown during the HTTP request
    print('Catch:::${e}');
    return 'Exception occurred: ${e}';
  }
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
final String mode;

  // Constructor for TeamHomePage that accepts a mode parameter
  TeamHomePage({this.mode = 'TeamHome'});
  @override
  _TeamHomeState createState() => _TeamHomeState();
}

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
        filteredSongs = List.from(songs); // Show all songs if input is empty
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
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return Scaffold(
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
              if (_controller.text == '') filteredSongs = List.from(songs); // Initial population of filtered songs

              return Padding(
                padding: EdgeInsets.all(16.0),
                child: Column(
                  children: [
                    
                    CustomAppBarWithOptions(
                      text: (widget.mode == 'TeamHome') ? 'Team Home' : 'Song Demand', 
                      navigateTo: (widget.mode == 'TeamHome') ? TeamHomePage() : LivePage(), 
                      optionsNavigateTo: OptionsPage(), fem: fem, ffem: ffem
                    ),

                    CustomGradientButton(onPressed: () => Navigator.push(context,MaterialPageRoute(builder: (context) => LivePage()),), buttonText: 'Live', fontSize: 24),

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
                      child: ListView.builder(
                        itemCount: filteredSongs.length,
                        itemBuilder: (BuildContext context, int index) {
                          return ListTile(
                            title: Text(filteredSongs[index]),
                            onTap: () {
                              //_controller.text = filteredSongs[index];
                              final title = filteredSongs[index];
                              print(title);
                              if (widget.mode == 'TeamHome') {
                                  Navigator.push(context, MaterialPageRoute(builder: (context) => SongPage(songId: selectSong(title)),),);
                              }
                              else { // mode = 'SongDemand'
                                DemandSong(title).then((result)  {
                                    if (result == 'OK') Navigator.push(context, MaterialPageRoute(builder: (context) => LivePage(),),);
                                    else Navigator.push(context, MaterialPageRoute(builder: (context) => CustomError(errorText: result, navigateTo: TeamHomePage(mode: 'SongDemand'),),),);
                                });
                                
                              }
                              print('############################################');
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
