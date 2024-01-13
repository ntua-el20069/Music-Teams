import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:myapp/components/button.dart';
import 'package:myapp/pages/team-home.dart';
import 'package:myapp/url.dart';
import 'package:record/record.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as p;
import 'dart:io';
import 'package:http/http.dart' as http;

void uploadFile(int songId, String recordingPath) async {
  try {
    var request = http.MultipartRequest(
      'POST',
      Uri.parse('$baseUrl/API/$songId/upload'),
    );

    // Attach the file to the request
    request.files.add(await http.MultipartFile.fromPath('file', recordingPath));

    // Send the request
    var response = await request.send();

    // Check the response status
    if (response.statusCode == 200) {
      print('File uploaded successfully!');
      print('Response: ${await response.stream.bytesToString()}');
    } else {
      print('Error uploading file. Status code: ${response.statusCode}');
      print('Response: ${await response.stream.bytesToString()}');
    }
  } catch (e) {
    print('Error uploading file: $e');
  }
}


class AddRecordingPage extends StatefulWidget {
  final int songId;
  final String title;
  const AddRecordingPage({Key? key, required this.songId,required this.title}) : super(key: key);

  @override
  AddRecordingState createState() => AddRecordingState();
}

class AddRecordingState extends State<AddRecordingPage> {
  late AudioRecorder audioRecorder;
  late AudioPlayer audioPlayer;
  bool isRecording = false;
  String audioPath = '';

  @override
  void initState() {
    audioPlayer = AudioPlayer();
    audioRecorder = AudioRecorder();
    super.initState();
  }

  @override
  void dispose() {
    audioRecorder.dispose();
    audioPlayer.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Add Recording'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (isRecording)
              const Text(
                'Recording now...',
                style: TextStyle(
                  fontSize: 20,
                ),
              ),
            ElevatedButton(
              onPressed: isRecording ? stopRecording : startRecording,
              child: isRecording
                  ? const Text('Stop Recording')
                  : const Text('Start Recording'),
            ),
            const SizedBox(
              height: 25,
            ),
            if (!isRecording)
              ElevatedButton(
                  onPressed: playRecording,
                  child: const Text('Play Recording')),
            Expanded(
              child: Container(
                alignment: Alignment.bottomRight,
                padding: const EdgeInsets.all(16),
                child: CustomGradientButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>  TeamHomePage()),
                    );
                  },
                  buttonText: 'Home Page',
                  fontSize: 24,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future<void> startRecording() async {
    try {
      if (await audioRecorder.hasPermission()) {
        String documentsDirectory =
            (await getApplicationDocumentsDirectory()).path;
            print('######################################################################################################  Documents Directory ${documentsDirectory}');
        //String recordingFilename = "${widget.title.replaceAll(' ', '_')}.mp3";
        String encodedTitle = Uri.encodeComponent(widget.title);
        String recordingFilename = "$encodedTitle.mp3";
        String filePath = p.join(documentsDirectory, recordingFilename);
        print('Audio filePath: $filePath'); // Add this line to check the path
        await audioRecorder.start(const RecordConfig(), path: filePath);
        setState(() {
          isRecording = true;
        });
      }
    } catch (e) {
      print('Error starting recording: $e');
    }
  }

  Future<void> stopRecording() async {
    try {
      String? path = await audioRecorder.stop();
      print('######################################################################################################  Path is ${path}');
      print('Audio Path: $path'); // Add this line to check the path
      setState(() {
        isRecording = false;
        audioPath = path!;
      });
    } catch (e) {
      print('Error stopping recording: $e');
    }
    // send recording to host
    try{
      uploadFile(widget.songId, audioPath);
    } catch(e){

    }
  }

  Future<void> playRecording() async {
    try {
      Source urlsource = UrlSource(audioPath);
      await audioPlayer.play(urlsource);
    } catch (e) {
      print('Error playing recording: $e');
    }
  }
}