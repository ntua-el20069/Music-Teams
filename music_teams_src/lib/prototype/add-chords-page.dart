import 'package:flutter/material.dart';
import 'package:myapp/prototype/add-rec-page.dart';
import 'package:myapp/prototype/add-song-page.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class AddChords extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // addchordspageqZW (5:20)
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            TextButton(
              // backbuttontextKzU (80:3565)
              onPressed: () {
                Navigator.push( context, MaterialPageRoute(builder: (context) => AddSong()), );
              },
              style: TextButton.styleFrom (
                padding: EdgeInsets.zero,
              ),
              child: Container(
                width: double.infinity,
                height: 165*fem,
                child: Stack(
                  children: [
                    Positioned(
                      // backbuttonbarDa4 (I80:3565;64:383)
                      left: 15*fem,
                      top: 38*fem,
                      child: Align(
                        child: SizedBox(
                          width: 384.7*fem,
                          height: 80*fem,
                          child: Image.asset(
                            'assets/prototype/images/back-button-bar-Rn4.png',
                            width: 384.7*fem,
                            height: 80*fem,
                          ),
                        ),
                      ),
                    ),
                    Positioned(
                      // textGoE (I80:3565;64:372)
                      left: 111*fem,
                      top: 48*fem,
                      child: Align(
                        child: SizedBox(
                          width: 182*fem,
                          height: 50*fem,
                          child: Text(
                            'Add chords',
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
                  ],
                ),
              ),
            ),
            Container(
              // autogrouplhh6kTW (F9xGHUzPth65QcTe9DLHh6)
              padding: EdgeInsets.fromLTRB(24*fem, 33*fem, 25*fem, 48*fem),
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Container(
                    // chordinputqE4 (60:1167)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 45*fem),
                    width: double.infinity,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Container(
                          // input8yr (I60:1167;60:1146)
                          margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 17.34*fem),
                          padding: EdgeInsets.fromLTRB(26.5*fem, 9*fem, 26.5*fem, 2.66*fem),
                          width: double.infinity,
                          decoration: BoxDecoration (
                            border: Border.all(color: Color(0xff4e36b0)),
                            borderRadius: BorderRadius.circular(4*fem),
                          ),
                          child: Text(
                            '  F                Am                   Dm',
                            textAlign: TextAlign.center,
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 32*ffem,
                              fontWeight: FontWeight.w700,
                              height: 1.5625*ffem/fem,
                              color: Color(0xffff0202),
                            ),
                          ),
                        ),
                        Text(
                          // imagineallthepeopleBx8 (I60:1167;60:1148)
                          'Imagine all the people',
                          textAlign: TextAlign.center,
                          style: SafeGoogleFont (
                            'Zilla Slab',
                            fontSize: 32*ffem,
                            fontWeight: FontWeight.w700,
                            height: 1.5625*ffem/fem,
                            color: Color(0xff000000),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // chordinputWDi (60:1173)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 234*fem),
                    width: double.infinity,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Container(
                          // inputrHa (I60:1173;60:1146)
                          margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 17.34*fem),
                          padding: EdgeInsets.fromLTRB(0*fem, 9*fem, 0*fem, 2.66*fem),
                          width: double.infinity,
                          decoration: BoxDecoration (
                            border: Border.all(color: Color(0xff4e36b0)),
                            borderRadius: BorderRadius.circular(4*fem),
                          ),
                          child: Text(
                            'G                         G7                              ',
                            textAlign: TextAlign.center,
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 32*ffem,
                              fontWeight: FontWeight.w700,
                              height: 1.5625*ffem/fem,
                              color: Color(0xffff0202),
                            ),
                          ),
                        ),
                        Text(
                          // imagineallthepeople4eY (I60:1173;60:1148)
                          'Living life in peace',
                          textAlign: TextAlign.center,
                          style: SafeGoogleFont (
                            'Zilla Slab',
                            fontSize: 32*ffem,
                            fontWeight: FontWeight.w700,
                            height: 1.5625*ffem/fem,
                            color: Color(0xff000000),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // buttonelementBUG (202:3033)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 10*fem, 21*fem),
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => AddRecording()), );
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
                              // rectangle786Qrp (I202:3033;59:261)
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
                              // buttontGC (I202:3033;59:262)
                              left: 13*fem,
                              top: 13*fem,
                              child: Center(
                                child: Align(
                                  child: SizedBox(
                                    width: 185*fem,
                                    height: 29*fem,
                                    child: Text(
                                      'Add recording',
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
                    // buttonelementKcQ (80:515)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 10*fem, 0*fem),
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
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
                              // rectangle786Nag (I80:515;59:261)
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
                              // button4iQ (I80:515;59:262)
                              left: 59*fem,
                              top: 13*fem,
                              child: Center(
                                child: Align(
                                  child: SizedBox(
                                    width: 93*fem,
                                    height: 29*fem,
                                    child: Text(
                                      'Submit',
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