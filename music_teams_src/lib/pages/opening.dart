import 'package:flutter/material.dart';
import 'package:myapp/pages/options.dart';
import 'package:myapp/pages/team-home.dart';
import 'package:myapp/prototype/options-page.dart';
import 'package:myapp/utils.dart';
import 'package:myapp/prototype/sign-in-page.dart';
import 'package:myapp/prototype/sign-up-page.dart';

class OpeningPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // openingpageuBS (5:2)
        padding: EdgeInsets.fromLTRB(29*fem, 59*fem, 28*fem, 387*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
          image: DecorationImage (
            fit: BoxFit.cover,
            image: AssetImage (
              'assets/prototype/images/image-1-bg.png',
            ),
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              'MUSIC TEAMS',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontFamily: 'Zilla Slab',
                fontSize: 64 * ffem,
                fontWeight: FontWeight.w700,
                height: 2.0 * ffem / fem,
                foreground: Paint()..shader = LinearGradient(
                  colors: [Color(0xfffe9a1a), Color(0xffc5087e)],
                ).createShader(Rect.fromLTWH(0.0, 0.0, 300.0, 50.0)),
              ),
            ),
            SizedBox(
              height: 95*fem,
            ),
            Container(
              // buttonelementDNU (60:816)
              margin: EdgeInsets.fromLTRB(86*fem, 0*fem, 87*fem, 0*fem),
              child: TextButton(
                onPressed: () {
                  // Navigate to the 'signin.dart' screen
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => TeamHomePage()),
                  );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: double.infinity,
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
                        // rectangle786vRJ (I60:816;59:261)
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
                        // buttonwbJ (I60:816;59:262)
                        left: 58.5*fem,
                        top: 13*fem,
                        child: Center(
                          child: Align(
                            child: SizedBox(
                              width: 93*fem,
                              height: 29*fem,
                              child: Text(
                                'Home',
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
            SizedBox(
              height: 95*fem,
            ),
            Container(
              // buttonelementbA4 (60:824)
              margin: EdgeInsets.fromLTRB(86*fem, 0*fem, 87*fem, 0*fem),
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => OptionsPage()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: double.infinity,
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
                        // rectangle786khA (I60:824;59:261)
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
                        // buttonQWp (I60:824;59:262)
                        left: 54.5*fem,
                        top: 13*fem,
                        child: Center(
                          child: Align(
                            child: SizedBox(
                              width: 101*fem,
                              height: 29*fem,
                              child: Text(
                                'Options',
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
    ),
          );
  }
}