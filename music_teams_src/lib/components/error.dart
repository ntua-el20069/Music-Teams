import 'package:flutter/material.dart';
import 'package:myapp/components/dark-app-bar.dart';

class CustomError extends StatelessWidget {
  final String errorTitle;
  final String errorText;
  final String navigateToRoute;

  CustomError({
    required this.errorText,
    this.errorTitle = 'Error',
    required this.navigateToRoute,
  });

  @override
  Widget build(BuildContext context) {
    double baseWidth = 450;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;

    return Scaffold(
      appBar: PurpleAppBar(header: errorTitle, onLeadingTap: () {  Navigator.of(context).pushReplacementNamed('/options');},),
      body: Container(
        width: double.infinity,
        //height: double.infinity,
        padding: EdgeInsets.all(16.0 * fem),
        color: Color(0xfff3edf7),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                errorTitle,
                style: TextStyle(
                  fontSize: 28.0 * ffem,
                  fontWeight: FontWeight.bold,
                  color: Colors.black,
                ),
              ),
              SizedBox(height: 20.0 * fem),
              Text(
                errorText,
                style: TextStyle(
                  fontSize: 18.0 * ffem,
                  color: Colors.black87,
                ),
              ),
              SizedBox(height: 40.0 * fem), // Adjust spacing as needed
              ElevatedButton(
                onPressed: () {
                  /*Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => navigateToRoute),
                  );*/
                  Navigator.of(context).pushReplacementNamed(navigateToRoute);
                },
                child: Text('Return'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Color(0xff451475),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
