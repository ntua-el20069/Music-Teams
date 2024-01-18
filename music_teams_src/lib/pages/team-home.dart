import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:myapp/components/button.dart';
import 'package:myapp/components/dark-app-bar.dart';
import 'package:myapp/components/error.dart';
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
    print(' json = $json \n');
    if (ids.isNotEmpty) {
      returnValue = ids[0] as int;
    } else {
      throw Exception('Failed to find Song, empty list of ids.');
    }
  } else {
    print('Title: "${title}"');
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
  try {
    final response = await http.get(Uri.parse(finalUrl));

    if (response.statusCode == 200) {
      return Album.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
    } else {
      return Album(ids: [], selected: '', songs: [], error: 'Failed to load album. HTTP Response Status code ${response.statusCode}');
      //throw Exception('Failed to load album');
    }
  } catch(e){
    return Album(ids: [], selected: '', songs: [], error: 'Ensure Internet Connection. \n\n $e');
  }
}

class Album {
  final List<dynamic> ids;
  final String selected;
  final List<dynamic> songs;
  final String error;

  const Album({
    required this.ids,
    required this.selected,
    required this.songs,
    this.error = ''
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
            } else if (snapshot.hasError || snapshot.data!.error != '') {
              return CustomError(
                errorText: (snapshot.data!.error == '') ? snapshot.error.toString() : snapshot.data!.error,
                navigateToRoute: '/', // Replace with the appropriate widget
                errorTitle: 'Error', // Customize error title if needed
              );
            } else if (snapshot.hasData) {
              songs = snapshot.data!.songs;
              if (_controller.text == '') filteredSongs = List.from(songs); // Initial population of filtered songs

              return Scaffold(
                appBar: PurpleAppBar(header: (widget.mode == 'TeamHome') ? 'Team Home' : 'Song Demand', onLeadingTap: () {  Navigator.of(context).pushReplacementNamed('/options');},),
                body: Padding(
                  padding: EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      
                     /* CustomAppBarWithOptions(
                        text: (widget.mode == 'TeamHome') ? 'Team Home' : 'Song Demand', 
                        navigateTo: (widget.mode == 'TeamHome') ? TeamHomePage() : LivePage(), 
                        optionsNavigateTo: OptionsPage(), fem: fem, ffem: ffem
                      ), */  

                      CustomGradientButton(onPressed: () => Navigator.of(context).pushReplacementNamed('/live'), buttonText: 'Live', fontSize: 24),

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
                                  
                                    selectSong(title).then((id) => { Navigator.of(context).pushReplacementNamed('/song/$id')/* print('/$id/song') */});
                                    //Navigator.push(context, MaterialPageRoute(builder: (context) => SongPage(songId: selectSong(title)),),);
                                }
                                else { // mode = 'SongDemand'
                                  DemandSong(title).then((result)  {
                                      if (result == 'OK') Navigator.of(context).pushReplacementNamed('/live');
                                      else Navigator.push(context, MaterialPageRoute(builder: (context) => CustomError(errorText: result, navigateToRoute: '/song-demand',),),);
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
                )
              );
            } else {
              return CustomError(
                errorText: 'Unexpected Error',
                navigateToRoute: 'team-home', // Replace with the appropriate widget
                errorTitle: 'Unexpected Error', // Customize error title if needed
              );
            }
          },
        ),
      ),
    );
  }
}
