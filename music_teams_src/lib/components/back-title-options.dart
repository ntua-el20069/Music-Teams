import 'package:flutter/material.dart';

class CustomAppBarWithOptions extends StatelessWidget {
  final String text;
  final Widget navigateTo;
  final Widget optionsNavigateTo;
  final double fem;
  final double ffem;

  const CustomAppBarWithOptions({
    required this.text,
    required this.navigateTo,
    required this.optionsNavigateTo,
    required this.fem,
    required this.ffem,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.fromLTRB(0 * fem, 0 * fem, 15.3 * fem, 10 * fem),
      width: 450 * fem,
      height: 85 * fem,
      child: Stack(
        children: [
          Positioned(
            left: 0 * fem,
            top: 5 * fem,
            child: Container(
              width: 450 * fem,
              height: 80 * fem,
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    margin: EdgeInsets.fromLTRB(0 * fem, 0 * fem, 258 * fem, 10 * fem),
                    child: GestureDetector(
                      onTap: () {
                        Navigator.push(context, MaterialPageRoute(builder: (context) => navigateTo));
                      },
                      child: Positioned(
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
                    ),
                  ),
                  GestureDetector(
                    onTap: () {
                      Navigator.push(context, MaterialPageRoute(builder: (context) => optionsNavigateTo));
                    },
                    child: Container(
                      margin: EdgeInsets.fromLTRB(0 * fem, 10 * fem, 0 * fem, 0 * fem),
                      width: 56.7 * fem,
                      height: 70 * fem,
                      child: Image.asset(
                        'assets/prototype/images/icon-menu.png',
                        width: 56.7 * fem,
                        height: 70 * fem,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          Positioned(
            left: 307 * fem,
            top: 0 * fem,
            child: GestureDetector(
              onTap: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) => optionsNavigateTo));
              },
              child: Container(
                padding: EdgeInsets.fromLTRB(9.62 * fem, 18.75 * fem, 9.62 * fem, 18.75 * fem),
                width: 76.93 * fem,
                height: 75 * fem,
                decoration: BoxDecoration(
                  image: DecorationImage(
                    fit: BoxFit.cover,
                    image: AssetImage(
                      'assets/prototype/images/vector.png',
                    ),
                  ),
                ),
                child: Center(
                  child: SizedBox(
                    width: 57.7 * fem,
                    height: 37.5 * fem,
                    child: Image.asset(
                      'assets/prototype/images/vector-gfv.png',
                      width: 57.7 * fem,
                      height: 37.5 * fem,
                    ),
                  ),
                ),
              ),
            ),
          ),
          Positioned(
            left: 100 * fem,
            top: 13 * fem,
            child: Align(
              child: SizedBox(
                width: 200 * fem,
                height: 50 * fem,
                child: Text(
                  text,
                  style: TextStyle(
                    fontSize: 36 * ffem,
                    fontWeight: FontWeight.w700,
                    height: 1.3888888889 * ffem / fem,
                    color: Color(0xff000000),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
