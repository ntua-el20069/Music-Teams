import 'package:flutter/material.dart';

class CustomNavigationButton extends StatelessWidget {
  final String buttonText;
  final VoidCallback? onPressed;
  final Widget navigateTo;
  final double fem;
  final double ffem;

  const CustomNavigationButton({
    required this.buttonText,
    required this.navigateTo,
    required this.fem,
    required this.ffem,
    this.onPressed,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextButton(
      onPressed: onPressed ?? () => Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => navigateTo),
      ),
      style: TextButton.styleFrom(padding: EdgeInsets.zero),
      child: Container(
        width: double.infinity,
        height: 100 * fem,
        child: Stack(
          children: [
            Positioned(
              left: 15 * fem,
              top: 0 * fem,
              child: Align(
                child: SizedBox(
                  width: 384.7 * fem,
                  height: 80 * fem,
                  child: Image.asset(
                    'assets/prototype/images/back-button-bar-Ktx.png',
                    width: 384.7 * fem,
                    height: 80 * fem,
                  ),
                ),
              ),
            ),
            Positioned(
              left: 111 * fem,
              top: 15 * fem,
              child: Align(
                child: SizedBox(
                  width: 155 * fem,
                  height: 50 * fem,
                  child: Text(
                    buttonText,
                    style: TextStyle(
                      fontSize: 30 * ffem,
                      fontWeight: FontWeight.w700,
                      height: 1.3888888889 * ffem / fem,
                      color: Color(0xff451475),
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
