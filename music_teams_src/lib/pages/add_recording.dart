import 'package:flutter/material.dart';
import 'package:record/record.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as p;

class AddRecording extends StatefulWidget {
  final String title;
  const AddRecording({Key? key, required this.title}) : super(key: key);

  @override
  AddRecordingState createState() => AddRecordingState();
}

class AddRecordingState extends State<AddRecording> {
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
                  onPressed: playRecording, child: const Text('Play Recording'))
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
        String recordingFilename = "${widget.title.replaceAll(' ', '_')}.mp3";
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
      print('Audio Path: $path'); // Add this line to check the path
      setState(() {
        isRecording = false;
        audioPath = path!;
      });
    } catch (e) {
      print('Error stopping recording: $e');
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
