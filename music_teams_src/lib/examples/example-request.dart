import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:typed_data';

Future<void> addLyrics() async {
  var url = 'http://10.0.2.2:5001/music-teams'; // Replace with your server URL
  //url = 'https://www.greeklyrics.gr/';

  var requestBody = {
    "title": "Your song title",
    "composer": "Composer name",
    "lyricist": "Lyricist name",
    "lyrics": "Your lyrics here\nHello\nFill a chord please\n",
    "button-info": "massive-submit" // Replace with your required button info
  };
  

  try {
    var response = await http.get(
      Uri.parse(url),
      //body: jsonEncode(requestBody),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
    );

    if (response.statusCode == 200) {
      print('Success: ${response.body}');

    String unicodeString = response.body;
    
    try {
      Map<String, dynamic> decodedMap = jsonDecode(unicodeString);

      // Assuming your response.body contains a key 'text' representing a list of strings
      List<dynamic> textList = decodedMap['text'];

      List<String> decodedStrings = textList.map<String>((item) {
        return item.toString(); // Converting each item to string
      }).toList();

      decodedStrings.forEach(print);
    } catch (e) {
      print('Error decoding JSON: $e');
    }
  
      // Handle success response from the server
    } else {
      print('Error: ${response.body}');
      // Handle error response from the server
    }
  } catch (error) {
    print('Error: $error');
    // Handle other types of errors (e.g., network issues)
  }
}
