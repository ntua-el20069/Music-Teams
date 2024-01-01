import 'package:flutter/material.dart';


/*class Template extends StatelessWidget {
  final String requestBody = '{"key": "value"}'; // Replace this with your actual request body

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Request Body Display',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Request Body Display'),
        ),
        body: RequestBodyDisplay(requestBody: requestBody),
      ),
    );
  }
}*/

class RequestBodyDisplay extends StatelessWidget {
  final String requestBody = "\u0391\u03bd\u03b4\u03c1\u03bf\u03bc\u03ad\u03b4\u03b1";

  //const RequestBodyDisplay({Key? key, required this.requestBody}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text(
              'Request Body:',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 10),
            Expanded(
              child: SingleChildScrollView(
                child: Text(
                  requestBody,
                  style: TextStyle(fontSize: 16),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}