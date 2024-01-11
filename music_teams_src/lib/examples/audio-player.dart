import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:audioplayers/audioplayers.dart';

class AudioPlayerWidget extends StatefulWidget {
  final String apiUrl;

  AudioPlayerWidget({required this.apiUrl});

  @override
  _AudioPlayerWidgetState createState() => _AudioPlayerWidgetState();
}

class _AudioPlayerWidgetState extends State<AudioPlayerWidget> {
  late AudioPlayer _audioPlayer;
  bool _isPlaying = false;

  @override
  void initState() {
    super.initState();
    _audioPlayer = AudioPlayer();
  }

  Future<void> _fetchAndPlayAudio() async {
    try {
      final response = await http.get(Uri.parse(widget.apiUrl));

      if (response.statusCode == 200) {
        final audioUrl = widget.apiUrl; // You can use the apiUrl directly as a URL
        await _audioPlayer.play(UrlSource(audioUrl));
        setState(() {
          _isPlaying = true;
        });
      } else {
        print('Failed to fetch audio: ${response.statusCode}');
      }
    } catch (e) {
      print('Error fetching audio: $e');
    }
  }

  Future<void> _stopAudio() async {
    await _audioPlayer.stop();
    setState(() {
      _isPlaying = false;
    });
  }

  @override
  void dispose() {
    _audioPlayer.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return  Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
                      onPressed: _isPlaying ? _stopAudio : _fetchAndPlayAudio,
                      child: Text(_isPlaying ? 'Stop' : 'Play Recording'),
                    ),
          ],
        );
  }
}

void main() {
  runApp(MaterialApp(
    home: AudioPlayerWidget(
      apiUrl: 'https://nikolaospapa3.pythonanywhere.com/API/4/recording', // Replace with your Flask API endpoint
    ),
  ));
}
