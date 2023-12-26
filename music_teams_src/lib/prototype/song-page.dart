import 'package:flutter/material.dart';
import 'package:myapp/prototype/live-team-1.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class Song extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: TextButton(
        // songpageVMv (5:22)
        onPressed: () {
          
        },
        style: TextButton.styleFrom (
          padding: EdgeInsets.zero,
        ),
        child: Container(
          padding: EdgeInsets.fromLTRB(11*fem, 37*fem, 15*fem, 38*fem),
          width: double.infinity,
          decoration: BoxDecoration (
            color: Color(0xfff3edf7),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                // autogroupht1eynt (F9xVyB2EyPVzCf3655HT1e)
                margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 15.3*fem, 21*fem),
                width: 388.7*fem,
                height: 81*fem,
                child: Stack(
                  children: [
                    Positioned(
                      // backbuttontextJqA (80:3736)
                      left: 0*fem,
                      top: 1*fem,
                      child: Container(
                        width: 384.7*fem,
                        height: 80*fem,
                        child: Stack(
                          children: [
                            Positioned(
                              // backbuttonbarcax (I80:3736;64:383)
                              left: 0*fem,
                              top: 0*fem,
                              child: Align(
                                child: SizedBox(
                                  width: 384.7*fem,
                                  height: 80*fem,
                                  child: Image.asset(
                                    'assets/prototype/images/back-button-bar-bqN.png',
                                    width: 384.7*fem,
                                    height: 80*fem,
                                  ),
                                ),
                              ),
                            ),
                            Positioned(
                              // textw7S (I80:3736;64:372)
                              left: 96*fem,
                              top: 10*fem,
                              child: Align(
                                child: SizedBox(
                                  width: 133*fem,
                                  height: 50*fem,
                                  child: Text(
                                    'Imagine',
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
                    Positioned(
                      // backbuttonbarMS4 (202:3528)
                      left: 4*fem,
                      top: 0*fem,
                      child: Container(
                        width: 384.7*fem,
                        height: 80*fem,
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            Container(
                              // backbuttonQfE (I202:3528;59:380)
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
                              // iconmenuDMn (I202:3528;61:2503)
                              margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                              width: 56.7*fem,
                              height: 70*fem,
                              child: Image.asset(
                                'assets/prototype/images/icon-menu-dpg.png',
                                width: 56.7*fem,
                                height: 70*fem,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                // transportjb2 (219:3574)
                margin: EdgeInsets.fromLTRB(11*fem, 0*fem, 10*fem, 29*fem),
                width: double.infinity,
                height: 51*fem,
                child: Stack(
                  children: [
                    Positioned(
                      // group27UYc (I219:3574;61:7832)
                      left: 0*fem,
                      top: 0*fem,
                      child: Container(
                        width: 383*fem,
                        height: 50*fem,
                        decoration: BoxDecoration (
                          boxShadow: [
                            BoxShadow(
                              color: Color(0x3f000000),
                              offset: Offset(0*fem, 4*fem),
                              blurRadius: 2*fem,
                            ),
                          ],
                        ),
                        child: Container(
                          // afafdzmr (I219:3574;61:7832;61:2456)
                          padding: EdgeInsets.fromLTRB(120*fem, 0*fem, 0*fem, 0*fem),
                          width: double.infinity,
                          height: double.infinity,
                          decoration: BoxDecoration (
                            color: Color(0xfff3edf7),
                          ),
                          child: Container(
                            // autogroupkzmwvfW (F9xWmKN2BcLAuNiqWWkZMW)
                            padding: EdgeInsets.fromLTRB(54.5*fem, 11*fem, 21.53*fem, 9*fem),
                            width: double.infinity,
                            height: double.infinity,
                            child: Row(
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: [
                                Container(
                                  // assistivechipDPi (I219:3574;61:7832;61:7678)
                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 73.65*fem, 0*fem),
                                  width: 33.99*fem,
                                  height: double.infinity,
                                  decoration: BoxDecoration (
                                    border: Border.all(color: Color(0xff451475)),
                                    borderRadius: BorderRadius.circular(2*fem),
                                  ),
                                  child: Center(
                                    child: Center(
                                      child: Text(
                                        '0',
                                        textAlign: TextAlign.center,
                                        style: SafeGoogleFont (
                                          'Roboto',
                                          fontSize: 14*ffem,
                                          fontWeight: FontWeight.w500,
                                          height: 1.4285714286*ffem/fem,
                                          letterSpacing: 0.1000000015*fem,
                                          color: Color(0xff451475),
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                                Container(
                                  // iconaddcircleoutlinerSg (I219:3574;61:7832;61:7622)
                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 11.33*fem, 0*fem),
                                  width: 33.99*fem,
                                  height: 30*fem,
                                  child: Image.asset(
                                    'assets/prototype/images/icon-add-circle-outline.png',
                                    width: 33.99*fem,
                                    height: 30*fem,
                                  ),
                                ),
                                Container(
                                  // iconremovecircleoutlinemZe (I219:3574;61:7832;61:7625)
                                  width: 33.99*fem,
                                  height: 30*fem,
                                  child: Image.asset(
                                    'assets/prototype/images/icon-remove-circle-outline.png',
                                    width: 33.99*fem,
                                    height: 30*fem,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ),
                    Positioned(
                      // transportW1S (I219:3574;61:7831)
                      left: 24.9289855957*fem,
                      top: 1*fem,
                      child: Align(
                        child: SizedBox(
                          width: 120*fem,
                          height: 50*fem,
                          child: Text(
                            'Transport',
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 27*ffem,
                              fontWeight: FontWeight.w500,
                              height: 1.8518518519*ffem/fem,
                              color: Color(0xff451475),
                            ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                // autogroupjmmvzBW (F9xW8LReBsB5U51ycvjMMv)
                margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 20*fem),
                width: double.infinity,
                height: 64*fem,
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Container(
                      // buttonelementitC (121:6354)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 4*fem, 0*fem),
                      child: TextButton(
                        onPressed: () {
                          Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
                        },
                        style: TextButton.styleFrom (
                          padding: EdgeInsets.zero,
                        ),
                        child: Container(
                          width: 200*fem,
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
                                // rectangle7868h2 (I121:6354;59:261)
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
                                // buttonbac (I121:6354;59:262)
                                left: 61*fem,
                                top: 13*fem,
                                child: Center(
                                  child: Align(
                                    child: SizedBox(
                                      width: 88*fem,
                                      height: 29*fem,
                                      child: Text(
                                        'Team 1',
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
                    TextButton(
                      // buttonelement4UC (121:6350)
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => Live()), );
                      },
                      style: TextButton.styleFrom (
                        padding: EdgeInsets.zero,
                      ),
                      child: Container(
                        width: 200*fem,
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
                              // rectangle786jqE (I121:6350;59:261)
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
                              // buttonDEc (I121:6350;59:262)
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
                  ],
                ),
              ),
              Container(
                // passwordURS (I141:1049;60:249)
                margin: EdgeInsets.fromLTRB(17*fem, 0*fem, 0*fem, 63*fem),
                child: Text(
                  '>> Drag from left to right for live page ',
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
                // chordslyrics1RN (60:4359)
                margin: EdgeInsets.fromLTRB(34.5*fem, 0*fem, 41.5*fem, 24*fem),
                width: double.infinity,
                height: 93*fem,
                child: Stack(
                  children: [
                    Positioned(
                      // imagineallthepeople8Vz (I60:4359;60:4328)
                      left: 9*fem,
                      top: 43*fem,
                      child: Align(
                        child: SizedBox(
                          width: 310*fem,
                          height: 50*fem,
                          child: Text(
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
                        ),
                      ),
                    ),
                    Positioned(
                      // famdmfPS (I60:4359;60:4327)
                      left: 0*fem,
                      top: 0*fem,
                      child: Align(
                        child: SizedBox(
                          width: 328*fem,
                          height: 50*fem,
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
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                // chordslyricsYy2 (60:6101)
                margin: EdgeInsets.fromLTRB(63*fem, 0*fem, 60*fem, 102*fem),
                width: double.infinity,
                height: 93*fem,
                child: Stack(
                  children: [
                    Positioned(
                      // imagineallthepeopleh5E (I60:6101;60:4328)
                      left: 6*fem,
                      top: 43*fem,
                      child: Align(
                        child: SizedBox(
                          width: 269*fem,
                          height: 50*fem,
                          child: Text(
                            'Living life in peace ',
                            textAlign: TextAlign.center,
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 32*ffem,
                              fontWeight: FontWeight.w700,
                              height: 1.5625*ffem/fem,
                              color: Color(0xff000000),
                            ),
                          ),
                        ),
                      ),
                    ),
                    Positioned(
                      // famdmAjW (I60:6101;60:4327)
                      left: 0*fem,
                      top: 0*fem,
                      child: Align(
                        child: SizedBox(
                          width: 281*fem,
                          height: 50*fem,
                          child: Text(
                            ' G                                G7     ',
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
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                // listenfAU (60:6104)
                margin: EdgeInsets.fromLTRB(54*fem, 0*fem, 38*fem, 0*fem),
                width: double.infinity,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text(
                      // simplelinetextPMN (I60:6104;60:4392;61:1285)
                      'Listen to Recording',
                      style: SafeGoogleFont (
                        'Zilla Slab',
                        fontSize: 36*ffem,
                        fontWeight: FontWeight.w700,
                        height: 1.3888888889*ffem/fem,
                        color: Color(0xff000000),
                      ),
                    ),
                    Container(
                      // group23Jz8 (I60:6104;60:4447)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 13.42*fem, 0*fem),
                      width: 148.25*fem,
                      height: 142*fem,
                      child: Image.asset(
                        'assets/prototype/images/group-23.png',
                        width: 148.25*fem,
                        height: 142*fem,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    ),
          );
  }
}