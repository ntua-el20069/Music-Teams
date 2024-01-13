import 'package:flutter/material.dart';
import 'package:myapp/components/button.dart';
import 'package:myapp/pages/add_recording.dart';
import 'package:http/http.dart' as http;
import 'package:myapp/url.dart';

class Addchords extends StatelessWidget {
  final String title;
  const Addchords({Key? key, required this.title}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Add Chords'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Your existing content goes here
          // If the page is empty, you can add a placeholder Text widget
          const Text('Your empty content'),

          // Expanded widget to make the button take up remaining space
          Expanded(
            child: Container(
              alignment: Alignment.bottomRight,
              padding: const EdgeInsets.all(16),
              child: CustomGradientButton(
                onPressed: () {
                  print(title);

                  Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => AddRecording(title: title)),
                  );
                },
                buttonText: 'Add chords',
                fontSize: 24,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
