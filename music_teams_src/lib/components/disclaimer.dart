import 'package:flutter/material.dart';
import 'package:myapp/components/dark-app-bar.dart';

class Disclaimer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;

    return Scaffold(
      appBar: PurpleAppBar(header: 'Disclaimer', onLeadingTap: () {  Navigator.of(context).pushReplacementNamed('/options');},),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        padding: EdgeInsets.all(16.0 * fem), // Adjust padding as needed
        color: Color(0xfff3edf7),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Disclaimer',
                style: TextStyle(
                  fontSize: 28.0 * ffem,
                  fontWeight: FontWeight.bold,
                  color: Colors.black, // Modify color as needed
                ),
              ),
              SizedBox(height: 20.0 * fem), // Add spacing between title and content
              Text(
                'This is a demo version of the app.',
                style: TextStyle(
                  fontSize: 18.0 * ffem,
                  color: Colors.black87, // Modify color as needed
                ),
              ),
              // Add more Text widgets or other widgets for your disclaimer content
            ],
          ),
        ),
      ),
    );
  }
}
