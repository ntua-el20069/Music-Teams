import 'dart:convert';
import 'package:http/http.dart' as http;

Map<String, String> d = {"Α" : "a",
 "Ά" : "a",
 "ά" : "a",
 "α" : "a",
 "Β" : "b",
 "β" : "b",
 "Γ" : "g",
 "γ" : "g",
 "Δ" : "d",
 "δ" : "d",
 "Ε" : "e",
 "Έ" : "e",
 "έ" : "e",
 "ε" : "e",
 "Ζ" : "z",
 "ζ" : "z",
 "Η" : "h",
 "Ή" : "h",
 "ή" : "h",
 "η" : "h",
 "Θ" : "th",
 "θ" : "th",
 "Ι" : "i",
 "Ί" : "i",
 "Ϊ" : "i",
 "ί" : "i",
 "ϊ" : "i",
 "ι" : "i",
 "Κ" : "k",
 "κ" : "k",
 "Λ" : "l",
 "λ" : "l",
 "Μ" : "m",
 "μ" : "m",
 "Ν" : "n",
 "ν" : "n",
 "Ξ" : "ks",
 "ξ" : "ks",
 "Ο" : "o",
 "Ό" : "o",
 "ό" : "o",
 "ο" : "o",
 "Π" : "p",
 "π" : "p",
 "Ρ" : "r",
 "ρ" : "r",
 "Σ" : "s",
 "ς" : "s",
 "σ" : "s",
 "Τ" : "t",
 "τ" : "t",
 "Υ" : "u",
 "Ύ" : "u",
 "Ϋ" : "u",
 "ύ" : "u",
 "ϋ" : "u",
 "υ" : "u",
 "Φ" : "f",
 "φ" : "f",
 "Χ" : "x",
 "χ" : "x",
 "Ψ" : "ps",
 "ψ" : "ps",
 "Ω" : "w",
 "Ώ" : "w",
 "ώ" : "w",
 "ω" : "w",
 " " : "-",
 "0" : "0",
"1" : "1",
"2" : "2",
"3" : "3",
"4" : "4",
"5" : "5",
"6" : "6",
"7" : "7",
"8" : "8",
"9" : "9"
};

Future<String?> takeFromGreekLyricsMobile(String searchTitle, {bool show = false}) async {
  // Return this in case of an error
  String emptyResult = '';



  String modifiedTitle = '';
  searchTitle.runes.forEach((int rune) {
    var character = String.fromCharCode(rune);
    modifiedTitle += (d[character] ?? character); // greek -> greeklish for the url (Ρόζα -> roza)
  });

  String url = 'https://www.greeklyrics.gr/stixoi/$modifiedTitle';
  int timeout = 10;

  try {
    http.Response response = await http.get(Uri.parse(url)).timeout(Duration(seconds: timeout));
    if (response.statusCode == 200) {
      return utf8.decode(response.bodyBytes);
    } else {
      print('HTTP Error: ${response.statusCode}');
      return 'HTTP Error';
    }
  } catch (e) {
    print('Error: $e');
    return 'Error: $e';
  }
}

void main() async {
  String? html = await takeFromGreekLyricsMobile('Ρόζα');
  print(html);
}
