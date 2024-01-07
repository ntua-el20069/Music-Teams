import 'package:flutter/material.dart';

class CustomGradientButton extends StatelessWidget {
  final VoidCallback onPressed;
  final String buttonText;
  final double fontSize; // New parameter for fontSize

  const CustomGradientButton({
    Key? key,
    required this.onPressed,
    required this.buttonText,
    required this.fontSize, // New parameter for fontSize
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    double fem = MediaQuery.of(context).size.width / 450; // Adjust as needed
    double ffem = fem * 0.97;

    return TextButton(
      onPressed: onPressed,
      style: TextButton.styleFrom(
        padding: EdgeInsets.zero,
      ),
      child: Container(
        width: 200 * fem,
        height: 64 * fem,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(32 * fem),
          gradient: LinearGradient(
            begin: Alignment(1, -1),
            end: Alignment(-1, 1),
            colors: <Color>[Color(0xfffe9a1a), Color(0xffc5087e)],
            stops: <double>[0, 1],
          ),
        ),
        child: Stack(
          children: [
            Positioned(
              left: 32.5 * fem,
              top: 13 * fem,
              child: Center(
                child: Align(
                  child: SizedBox(
                    width: 146 * fem,
                    height: 29 * fem,
                    child: Text(
                      buttonText,
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontFamily: 'Zilla Slab',
                        fontSize: fontSize * ffem, // Using the fontSize parameter
                        fontWeight: FontWeight.w700,
                        height: 1.2 * ffem / fem,
                        letterSpacing: 2.4 * fem,
                        color: Color(0xffffffff),
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
