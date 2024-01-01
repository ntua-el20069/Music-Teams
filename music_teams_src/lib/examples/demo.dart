import 'package:flutter/material.dart';
import 'package:myapp/examples/example-request.dart';

class Demo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: ElevatedButton(
        onPressed: () {
          addLyrics(); // Call the addLyrics function when the button is pressed
        },
        child: Text('Songs'),
      ),
    );
  }
}


