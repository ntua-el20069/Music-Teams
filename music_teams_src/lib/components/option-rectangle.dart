import 'package:flutter/material.dart';
import 'package:myapp/utils.dart';

class OptionRectangle extends StatelessWidget {
  final double top;
  final String buttonText;
  final String navigateToRoute;

  OptionRectangle({
    required this.top,
    required this.buttonText,
    required this.navigateToRoute,
  });

  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return Positioned(
      left: 0 * fem,
      top: top * fem,
      child: TextButton(
        onPressed: () {
          Navigator.of(context).pushReplacementNamed(navigateToRoute);
        },
        style: TextButton.styleFrom(
          padding: EdgeInsets.zero,
        ),
        child: Container(
          padding: EdgeInsets.fromLTRB(70.5 * fem, 12.5 * fem, 69.5 * fem, 12.5 * fem),
          width: 450 * fem,
          height: 83 * fem,
          decoration: BoxDecoration(
            border: Border.all(color: Color(0xff000000)),
            color: Color(0xff451475),
          ),
          child: Center(
            child: SizedBox(
              child: Container(
                child: Text(
                  buttonText,
                  textAlign: TextAlign.center,
                  style: SafeGoogleFont (
                    'Zilla Slab',
                    fontSize: 24*ffem,
                    fontWeight: FontWeight.w700,
                    height: 1.2*ffem/fem,
                    letterSpacing: 2.4*fem,
                    color: Color(0xffffffff),
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
