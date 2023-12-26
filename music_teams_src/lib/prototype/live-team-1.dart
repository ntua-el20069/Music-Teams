import 'package:flutter/material.dart';
import 'package:myapp/prototype/song-demand.dart';
import 'package:myapp/prototype/song-page.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class Live extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // liveteam1Nrg (5:23)
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // autogroupkuwq7pG (F9xXYo4F8AEtrnqyZbkUWQ)
              padding: EdgeInsets.fromLTRB(15*fem, 38*fem, 25*fem, 137*fem),
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // autogroupomgg2RS (F9xXR3n9jV2QgPw8hzoMgg)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 5.3*fem, 47*fem),
                    width: 384.7*fem,
                    height: 80*fem,
                    child: Stack(
                      children: [
                        Positioned(
                          // textMTi (61:2640)
                          left: 97*fem,
                          top: 10*fem,
                          child: Align(
                            child: SizedBox(
                              width: 186*fem,
                              height: 50*fem,
                              child: Text(
                                'Live-Team 1',
                                style: SafeGoogleFont (
                                  'Zilla Slab',
                                  fontSize: 36*ffem,
                                  fontWeight: FontWeight.w700,
                                  height: 1.3888888889*ffem/fem,
                                  color: Color(0xff451475),
                                ),
                              ),
                            ),
                          ),
                        ),
                        Positioned(
                          // backbuttontextDkp (202:3519)
                          left: 0 * fem,
                          top: 0 * fem,
                          child: GestureDetector(
                            onTap: () {
                              // Navigate to the desired screen when the image is tapped
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (context) => TeamHome()), // Replace BackScreen() with your desired screen
                              );
                            },
                            child: Container(
                              width: 384.7 * fem,
                              height: 80 * fem,
                              child: Center(
                                // backbuttonbarxTW (I202:3519;64:383)
                                child: SizedBox(
                                  width: 384.7 * fem,
                                  height: 80 * fem,
                                  child: Image.asset(
                                    'assets/prototype/images/back-button-bar-FAc.png',
                                    width: 384.7 * fem,
                                    height: 80 * fem,
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ),

                      ],
                    ),
                  ),
                  Container(
                    // simplelinetextT9N (I60:3891;61:1285)
                    margin: EdgeInsets.fromLTRB(35*fem, 0*fem, 0*fem, 87*fem),
                    child: Text(
                      'Recent Song Demands',
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
                    // buttonelementaDz (60:3929)
                    margin: EdgeInsets.fromLTRB(100*fem, 0*fem, 90*fem, 44*fem),
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => Song()), );
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
                              // rectangle786PSL (I60:3929;59:261)
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
                              // buttonfPr (I60:3929;59:262)
                              left: 53*fem,
                              top: 13*fem,
                              child: Center(
                                child: Align(
                                  child: SizedBox(
                                    width: 105*fem,
                                    height: 29*fem,
                                    child: Text(
                                      'Imagine',
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
                  Container(
                    // buttonelementYTe (60:3933)
                    margin: EdgeInsets.fromLTRB(100*fem, 0*fem, 90*fem, 44*fem),
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
                          // rectangle786RXS (I60:3933;59:261)
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
                          // buttonJbE (I60:3933;59:262)
                          left: 61*fem,
                          top: 13*fem,
                          child: Center(
                            child: Align(
                              child: SizedBox(
                                width: 88*fem,
                                height: 29*fem,
                                child: Text(
                                  'Zorbas',
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
                  Container(
                    // buttonelementoH6 (60:3937)
                    margin: EdgeInsets.fromLTRB(97*fem, 0*fem, 93*fem, 0*fem),
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
                          // rectangle786tJY (I60:3937;59:261)
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
                          // buttonxJQ (I60:3937;59:262)
                          left: 63*fem,
                          top: 13*fem,
                          child: Center(
                            child: Align(
                              child: SizedBox(
                                width: 84*fem,
                                height: 29*fem,
                                child: Text(
                                  'Money',
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
                ],
              ),
            ),
            Container(
              // backbuttonsDk8 (80:548)
              padding: EdgeInsets.fromLTRB(48*fem, 39*fem, 49*fem, 39*fem),
              width: double.infinity,
              height: 213*fem,
              decoration: BoxDecoration (
                color: Color(0xff451475),
                borderRadius: BorderRadius.circular(2*fem),
              ),
              child: TextButton(
                // linebuttonKoA (80:528)
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => SongDemand()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: double.infinity,
                  height: double.infinity,
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
                        // rectangle786FaL (I80:528;60:992)
                        left: 18.3150024414*fem,
                        top: 0*fem,
                        child: Align(
                          child: SizedBox(
                            width: 314.68*fem,
                            height: 113.91*fem,
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
                        // createanewteamKKJ (I80:528;60:993)
                        left: 85.8349609375*fem,
                        top: 39.3557128906*fem,
                        child: Center(
                          child: Align(
                            child: SizedBox(
                              width: 158*fem,
                              height: 58*fem,
                              child: Text(
                                'Make a song demand',
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