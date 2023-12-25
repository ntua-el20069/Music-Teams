import 'package:flutter/material.dart';
import 'package:myapp/utils.dart';

class Scene extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 430;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return Container(
      width: double.infinity,
      child: Container(
        // signinpageHgQ (5:12)
        padding: EdgeInsets.fromLTRB(13*fem, 38*fem, 13*fem, 48*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttonbarQFE (141:1025)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 19.3*fem, 135*fem),
              width: double.infinity,
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // backbuttonUVz (I141:1025;59:380)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 258*fem, 10*fem),
                    child: TextButton(
                      onPressed: () {},
                      style: TextButton.styleFrom (
                        padding: EdgeInsets.zero,
                      ),
                      child: Container(
                        padding: EdgeInsets.fromLTRB(16.1*fem, 35*fem, 16.8*fem, 35*fem),
                        decoration: BoxDecoration (
                          color: Color(0xff451475),
                          borderRadius: BorderRadius.circular(35*fem),
                          boxShadow: [
                            BoxShadow(
                              color: Color(0x3f000000),
                              offset: Offset(0*fem, 4*fem),
                              blurRadius: 2*fem,
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                  Container(
                    // iconmenu7J4 (I141:1025;61:2503)
                    margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                    width: 56.7*fem,
                    height: 70*fem,
                    child: Image.asset(
                      'assets/prototype/images/icon-menu-Ntt.png',
                      width: 56.7*fem,
                      height: 70*fem,
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // youhave5musicpointscontinueadd (I60:6280;60:241)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 254*fem, 36*fem),
              child: Text(
                'Sign in',
                style: SafeGoogleFont (
                  'Zilla Slab',
                  fontSize: 36*ffem,
                  fontWeight: FontWeight.w700,
                  height: 1.3888888889*ffem/fem,
                  color: Color(0xff000000),
                ),
              ),
            ),
            Container(
              // inputelementaqr (60:6091)
              margin: EdgeInsets.fromLTRB(16*fem, 0*fem, 16*fem, 32*fem),
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    // passwordVhv (I60:6091;60:121)
                    margin: EdgeInsets.fromLTRB(9*fem, 0*fem, 0*fem, 11.22*fem),
                    child: Text(
                      'Username',
                      style: SafeGoogleFont (
                        'Zilla Slab',
                        fontSize: 20*ffem,
                        fontWeight: FontWeight.w400,
                        height: 1.2*ffem/fem,
                        color: Color(0xff4e36b0),
                      ),
                    ),
                  ),
                  Container(
                    // inputmvL (I60:6091;60:122)
                    width: double.infinity,
                    height: 59.78*fem,
                    decoration: BoxDecoration (
                      border: Border.all(color: Color(0xff4e36b0)),
                      borderRadius: BorderRadius.circular(4*fem),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // inputelementWd2 (60:6096)
              margin: EdgeInsets.fromLTRB(16*fem, 0*fem, 16*fem, 259*fem),
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    // password2LU (I60:6096;60:121)
                    margin: EdgeInsets.fromLTRB(9*fem, 0*fem, 0*fem, 11.22*fem),
                    child: Text(
                      'Password',
                      style: SafeGoogleFont (
                        'Zilla Slab',
                        fontSize: 20*ffem,
                        fontWeight: FontWeight.w400,
                        height: 1.2*ffem/fem,
                        color: Color(0xff4e36b0),
                      ),
                    ),
                  ),
                  Container(
                    // input6r8 (I60:6096;60:122)
                    width: double.infinity,
                    height: 59.78*fem,
                    decoration: BoxDecoration (
                      border: Border.all(color: Color(0xff4e36b0)),
                      borderRadius: BorderRadius.circular(4*fem),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // buttonelementEBe (80:5161)
              margin: EdgeInsets.fromLTRB(160*fem, 0*fem, 0*fem, 0*fem),
              child: TextButton(
                onPressed: () {},
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: 200*fem,
                  height: 64*fem,
                  decoration: BoxDecoration (
                    borderRadius: BorderRadius.circular(32*fem),
                    gradient: LinearGradient (
                      begin: Alignment(1, -1),
                      end: Alignment(-1, 1),
                      colors: <Color>[Color(0xfffe9a1a), Color(0xffc5087e)],
                      stops: <double>[0, 1],
                    ),
                  ),
                  child: Stack(
                    children: [
                      Positioned(
                        // rectangle786rTv (I80:5161;59:261)
                        left: 11*fem,
                        top: 0*fem,
                        child: Align(
                          child: SizedBox(
                            width: 189*fem,
                            height: 54*fem,
                            child: Container(
                              decoration: BoxDecoration (
                                borderRadius: BorderRadius.circular(32*fem),
                                gradient: LinearGradient (
                                  begin: Alignment(1, -1),
                                  end: Alignment(-1, 1),
                                  colors: <Color>[Color(0xfffe9a1a), Color(0xffff1e74)],
                                  stops: <double>[0, 1],
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // button8wE (I80:5161;59:262)
                        left: 67*fem,
                        top: 13*fem,
                        child: Center(
                          child: Align(
                            child: SizedBox(
                              width: 77*fem,
                              height: 29*fem,
                              child: Text(
                                'Ready',
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
                    ],
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