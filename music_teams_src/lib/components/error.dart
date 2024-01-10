import 'package:flutter/material.dart';

class CustomError extends StatelessWidget {
  final String errorTitle;
  final String errorText;
  final Widget navigateTo;

  CustomError({
    required this.errorText,
    this.errorTitle = 'Error',
    required this.navigateTo,
  });

  @override
  Widget build(BuildContext context) {
    double baseWidth = 450;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;

    return Scaffold(
      appBar: AppBar(
        title: Text(errorTitle),
        backgroundColor: Color(0xff451475),
      ),
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
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => navigateTo),
                  );
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
