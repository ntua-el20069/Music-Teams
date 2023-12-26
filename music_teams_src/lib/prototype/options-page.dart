import 'package:flutter/material.dart';
import 'package:myapp/prototype/add-song-page.dart';
import 'package:myapp/prototype/rename-page.dart';
import 'package:myapp/prototype/team-code-pop-up.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class Options extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // optionspagesXz (5:16)
        width: double.infinity,
        height: 932*fem,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Stack(
          children: [
            Positioned(
              // buttonelementNUk (80:5051)
              left: 115*fem,
              top: 778*fem,
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
                      // rectangle786prY (I80:5051;59:261)
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
                      // buttonK2c (I80:5051;59:262)
                      left: 78*fem,
                      top: 13*fem,
                      child: Center(
                        child: Align(
                          child: SizedBox(
                            width: 54*fem,
                            height: 29*fem,
                            child: Text(
                              'Live',
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
            Positioned(
              // backbuttonbarwpg (61:405)
              left: 15*fem,
              top: 39*fem,
              child: Container(
                width: 384.7*fem,
                height: 80*fem,
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Container(
                      // backbuttonQCU (I61:405;59:380)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 258*fem, 10*fem),
                      child: TextButton(
                        onPressed: () {
                          Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
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
                      // iconmenueMi (I61:405;61:2503)
                      margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                      width: 56.7*fem,
                      height: 70*fem,
                      child: Image.asset(
                        'assets/prototype/images/icon-menu-EgL.png',
                        width: 56.7*fem,
                        height: 70*fem,
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Positioned(
              // inputelementwbi (80:905)
              left: 29*fem,
              top: 245*fem,
              child: Container(
                width: 372*fem,
                height: 95*fem,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                      // passwordT4G (I80:905;60:121)
                      margin: EdgeInsets.fromLTRB(9*fem, 0*fem, 0*fem, 11.22*fem),
                      child: Text(
                        'Team 1',
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
                      // input9St (I80:905;60:122)
                      padding: EdgeInsets.fromLTRB(0*fem, 0*fem, 11*fem, 0*fem),
                      width: double.infinity,
                      decoration: BoxDecoration (
                        border: Border.all(color: Color(0xff4e36b0)),
                        borderRadius: BorderRadius.circular(5*fem),
                      ),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Container(
                            // input4pk (80:906)
                            margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 14*fem, 0*fem),
                            width: 319*fem,
                            height: 60*fem,
                            child: Image.asset(
                              'assets/prototype/images/input.png',
                              width: 319*fem,
                              height: 60*fem,
                            ),
                          ),
                          Container(
                            // iconarrowforwardiosQ7v (I80:905;61:355)
                            margin: EdgeInsets.fromLTRB(0*fem, 0.78*fem, 0*fem, 0*fem),
                            width: 28*fem,
                            height: 25*fem,
                            child: Image.asset(
                              'assets/prototype/images/icon-arrow-forward-ios-Evp.png',
                              width: 28*fem,
                              height: 25*fem,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Positioned(
              // rectangle788Tbz (80:914)
              left: 221*fem,
              top: 0*fem,
              child: Align(
                child: SizedBox(
                  width: 209*fem,
                  height: 932*fem,
                  child: Container(
                    decoration: BoxDecoration (
                      color: Color(0xff451475),
                    ),
                  ),
                ),
              ),
            ),
            Positioned(
              // optionsnPN (80:979)
              left: 221*fem,
              top: 249*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => TeamCode()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  padding: EdgeInsets.fromLTRB(70.5*fem, 12.5*fem, 69.5*fem, 12.5*fem),
                  width: 209*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: Color(0xff000000)),
                    color: Color(0xff451475),
                  ),
                  child: Center(
                    // textHL8 (I80:979;80:959)
                    child: Center(
                      child: SizedBox(
                        child: Container(
                          constraints: BoxConstraints (
                            maxWidth: 69*fem,
                          ),
                          child: Text(
                            'Team-code',
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
              ),
            ),
            Positioned(
              // optionsY1A (80:983)
              left: 221*fem,
              top: 333*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: 209*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: Color(0xff000000)),
                    color: Color(0xff451475),
                  ),
                  child: Center(
                    child: Center(
                      child: Text(
                        'Back',
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
            Positioned(
              // optionsksv (80:973)
              left: 221*fem,
              top: 83*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => AddSong()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: 209*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: Color(0xff000000)),
                    color: Color(0xff451475),
                  ),
                  child: Center(
                    child: Center(
                      child: Text(
                        'Add song',
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
            Positioned(
              // optionsEHJ (80:976)
              left: 221*fem,
              top: 166*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => Rename()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: 209*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: Color(0xff000000)),
                    color: Color(0xff451475),
                  ),
                  child: Center(
                    child: Center(
                      child: Text(
                        'Rename',
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
            Positioned(
              // optionsERi (80:970)
              left: 221*fem,
              top: 0*fem,
              child: Container(
                width: 209*fem,
                height: 83*fem,
                decoration: BoxDecoration (
                  border: Border.all(color: Color(0xff000000)),
                  color: Color(0xff451475),
                ),
                child: Center(
                  child: Center(
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
          );
  }
}