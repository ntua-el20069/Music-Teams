import 'package:flutter/material.dart';
import 'package:myapp/utils.dart';
import 'package:myapp/prototype/opening-page.dart';
import 'package:myapp/prototype/home-page.dart';

class SignUp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // signuppagek5r (5:13)
        padding: EdgeInsets.fromLTRB(18*fem, 38*fem, 27.3*fem, 48*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttonbarFHW (141:1031)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 135*fem),
              width: double.infinity,
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // backbuttonxxc (I141:1031;59:380)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 258*fem, 10*fem),
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => Opening()), );
                      },
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
                    // iconmenuRUp (I141:1031;61:2503)
                    margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                    width: 56.7*fem,
                    height: 70*fem,
                    child: Image.asset(
                      'assets/prototype/images/icon-menu-p7n.png',
                      width: 56.7*fem,
                      height: 70*fem,
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // youhave5musicpointscontinueadd (I80:5194;60:241)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 261.7*fem, 36*fem),
              child: Text(
                'Sign up',
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
              // inputelementRdE (80:5182)
              margin: EdgeInsets.fromLTRB(9.3*fem, 0*fem, 0*fem, 32*fem),
              width: 372*fem,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    // passwordwba (I80:5182;60:121)
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
                    // inputryS (I80:5182;60:122)
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
              // inputelementcBv (80:5187)
              margin: EdgeInsets.fromLTRB(9.3*fem, 0*fem, 0*fem, 32*fem),
              width: 372*fem,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    // passwordL7v (I80:5187;60:121)
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
                    // inputG1a (I80:5187;60:122)
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
              // inputelementmU8 (80:5196)
              margin: EdgeInsets.fromLTRB(9.3*fem, 0*fem, 0*fem, 132*fem),
              width: 372*fem,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    // password4y2 (I80:5196;60:121)
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
                    // inputwG8 (I80:5196;60:122)
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
              // autogroupz4pwGJQ (F9xTgaAXCr5DdQ9gNqz4PW)
              margin: EdgeInsets.fromLTRB(169.3*fem, 0*fem, 0*fem, 0*fem),
              width: 200*fem,
              height: 64*fem,
              child: Stack(
                children: [
                  Positioned(
                    // readyZoJ (27:27)
                    left: 72*fem,
                    top: 5*fem,
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
                  Positioned(
                    // buttonelement9mW (80:5165)
                    left: 0*fem,
                    top: 0*fem,
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => Home()), );
                      },
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
                              // rectangle786GzY (I80:5165;59:261)
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
                              // buttonibe (I80:5165;59:262)
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
          ],
        ),
      ),
    ),
          );
  }
}