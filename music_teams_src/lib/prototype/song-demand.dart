import 'package:flutter/material.dart';
import 'package:myapp/prototype/live-team-1.dart';
import 'package:myapp/utils.dart';

class SongDemand extends StatelessWidget {
  const SongDemand({super.key});

  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: SizedBox(
      width: double.infinity,
      child: Container(
        // songdemandazY (29:96)
        padding: EdgeInsets.fromLTRB(15*fem, 38*fem, 15*fem, 0*fem),
        width: double.infinity,
        decoration: const BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttontexthJU (80:3660)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 15.3*fem, 144*fem),
              width: 384.7*fem,
              height: 80*fem,
              child: Stack(
                children: [
                  Positioned(
                    // backbuttonbarQig (I80:3660;64:383)
                    left: 0 * fem,
                    top: 0 * fem,
                    child: GestureDetector(
                      onTap: () {
                        // Navigate to the desired screen when the image is tapped
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => const Live()), // Replace BackScreen() with your desired screen
                        );
                      },
                      child: Align(
                        child: SizedBox(
                          width: 384.7 * fem,
                          height: 80 * fem,
                          child: Image.asset(
                            'assets/prototype/images/back-button-bar-p5z.png',
                            width: 384.7 * fem,
                            height: 80 * fem,
                          ),
                        ),
                      ),
                    ),
                  ),

                  Positioned(
                    // textK4x (I80:3660;64:372)
                    left: 96*fem,
                    top: 10*fem,
                    child: Align(
                      child: SizedBox(
                        width: 217*fem,
                        height: 50*fem,
                        child: Text(
                          'Song demand',
                          style: SafeGoogleFont (
                            'Zilla Slab',
                            fontSize: 36*ffem,
                            fontWeight: FontWeight.w700,
                            height: 1.3888888889*ffem/fem,
                            color: const Color(0xff451475),
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // autogroupxe1ibYG (F9xYH7B5HGmgGX3iY1XE1i)
              margin: EdgeInsets.fromLTRB(15*fem, 0*fem, 16*fem, 0*fem),
              width: double.infinity,
              height: 754*fem,
              child: Stack(
                children: [
                  Positioned(
                    // buttonelement8YC (80:5176)
                    left: 165*fem,
                    top: 558*fem,
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => const Live()), );
                      },
                      style: TextButton.styleFrom (
                        padding: EdgeInsets.zero,
                      ),
                      child: Container(
                        width: 200*fem,
                        height: 64*fem,
                        decoration: BoxDecoration (
                          borderRadius: BorderRadius.circular(32*fem),
                          gradient: const LinearGradient (
                            begin: Alignment(1, -1),
                            end: Alignment(-1, 1),
                            colors: <Color>[Color(0xfffe9a1a), Color(0xffc5087e)],
                            stops: <double>[0, 1],
                          ),
                        ),
                        child: Stack(
                          children: [
                            Positioned(
                              // rectangle786a9J (I80:5176;59:261)
                              left: 11*fem,
                              top: 0*fem,
                              child: Align(
                                child: SizedBox(
                                  width: 189*fem,
                                  height: 54*fem,
                                  child: Container(
                                    decoration: BoxDecoration (
                                      borderRadius: BorderRadius.circular(32*fem),
                                      gradient: const LinearGradient (
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
                              // button3Hn (I80:5176;59:262)
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
                                        color: const Color(0xffffffff),
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
                  Positioned(
                    // searchsongHT2 (60:6113)
                    left: 0*fem,
                    top: 0*fem,
                    child: SizedBox(
                      width: 369*fem,
                      height: 754*fem,
                      child: Stack(
                        children: [
                          Positioned(
                            // textfieldd16 (I60:6113;60:4017)
                            left: 0*fem,
                            top: 0*fem,
                            child: Container(
                              width: 369*fem,
                              height: 84*fem,
                              decoration: BoxDecoration (
                                borderRadius: BorderRadius.only (
                                  topLeft: Radius.circular(4*fem),
                                  topRight: Radius.circular(4*fem),
                                ),
                              ),
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Container(
                                    // textfieldvF6 (I60:6113;60:4017;52798:24695)
                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 4*fem),
                                    width: double.infinity,
                                    height: 64*fem,
                                    decoration: BoxDecoration (
                                      border: Border.all(color: const Color(0xff6750a4)),
                                      borderRadius: BorderRadius.circular(4*fem),
                                    ),
                                    child: Container(
                                      // statelayereB6 (I60:6113;60:4017;52798:24696)
                                      padding: EdgeInsets.fromLTRB(4*fem, 0*fem, 14.62*fem, 0*fem),
                                      width: double.infinity,
                                      height: double.infinity,
                                      decoration: BoxDecoration (
                                        borderRadius: BorderRadius.only (
                                          topLeft: Radius.circular(4*fem),
                                          topRight: Radius.circular(4*fem),
                                        ),
                                      ),
                                      child: Row(
                                        crossAxisAlignment: CrossAxisAlignment.center,
                                        children: [
                                          Container(
                                            // autogroup54msYGU (F9xYY6k6MsWZ4qCShx54mS)
                                            margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 236*fem, 8*fem),
                                            child: Column(
                                              crossAxisAlignment: CrossAxisAlignment.start,
                                              children: [
                                                Container(
                                                  // labeltextf6C (I60:6113;60:4017;52798:24702)
                                                  margin: EdgeInsets.fromLTRB(8*fem, 0*fem, 0*fem, 0*fem),
                                                  width: 76*fem,
                                                  height: 16*fem,
                                                  decoration: const BoxDecoration (
                                                    color: Color(0xfffef7ff),
                                                  ),
                                                  child: Center(
                                                    child: Text(
                                                      'Search Song',
                                                      style: SafeGoogleFont (
                                                        'Roboto',
                                                        fontSize: 12*ffem,
                                                        fontWeight: FontWeight.w400,
                                                        height: 1.3333333333*ffem/fem,
                                                        color: const Color(0xff6750a4),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                                SizedBox(
                                                  // leadingiconKwS (I60:6113;60:4017;52798:24697)
                                                  width: 40*fem,
                                                  height: 40*fem,
                                                  child: Image.asset(
                                                    'assets/prototype/images/leading-icon-3bJ.png',
                                                    width: 40*fem,
                                                    height: 40*fem,
                                                  ),
                                                ),
                                              ],
                                            ),
                                          ),
                                          Container(
                                            // iconarrowforwardioseyi (I60:6113;61:8579)
                                            margin: EdgeInsets.fromLTRB(0*fem, 7*fem, 0*fem, 0*fem),
                                            width: 30.38*fem,
                                            height: 25*fem,
                                            child: Image.asset(
                                              'assets/prototype/images/icon-arrow-forward-ios-Ltc.png',
                                              width: 30.38*fem,
                                              height: 25*fem,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                  ),
                                  Container(
                                    // supportingtext9vU (I60:6113;60:4017;52798:24706)
                                    margin: EdgeInsets.fromLTRB(16*fem, 0*fem, 0*fem, 0*fem),
                                    child: Text(
                                      'Supporting text',
                                      style: SafeGoogleFont (
                                        'Roboto',
                                        fontSize: 12*ffem,
                                        fontWeight: FontWeight.w400,
                                        height: 1.3333333333*ffem/fem,
                                        color: const Color(0xff49454f),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                          Positioned(
                            // menuFic (I60:6113;60:4018)
                            left: 2*fem,
                            top: 64*fem,
                            child: Container(
                              padding: EdgeInsets.fromLTRB(0*fem, 8*fem, 0*fem, 0*fem),
                              width: 280*fem,
                              height: 690*fem,
                              decoration: BoxDecoration (
                                color: const Color(0xfff3edf7),
                                borderRadius: BorderRadius.circular(4*fem),
                                boxShadow: [
                                  BoxShadow(
                                    color: const Color(0x26000000),
                                    offset: Offset(0*fem, 2*fem),
                                    blurRadius: 3*fem,
                                  ),
                                  BoxShadow(
                                    color: const Color(0x4c000000),
                                    offset: Offset(0*fem, 1*fem),
                                    blurRadius: 1*fem,
                                  ),
                                ],
                              ),
                              child: SizedBox(
                                // menulistuHN (I60:6113;60:4019)
                                width: double.infinity,
                                height: double.infinity,
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  children: [
                                    SizedBox(
                                      // autogrouptgw83eU (F9xZBVqSmuk4UCdSDFtGW8)
                                      width: double.infinity,
                                      height: 570*fem,
                                      child: Stack(
                                        children: [
                                          Positioned(
                                            // menulistitem1nc4 (I60:6113;60:4020)
                                            left: 0*fem,
                                            top: 0*fem,
                                            child: TextButton(
                                              onPressed: () {
                                                
                                              },
                                              style: TextButton.styleFrom (
                                                padding: EdgeInsets.zero,
                                              ),
                                              child: Container(
                                                padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 12*fem, 6*fem),
                                                width: 280*fem,
                                                height: 66*fem,
                                                child: Container(
                                                  // statelayerVFa (I60:6113;60:4020;54061:37028)
                                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 89*fem, 0*fem),
                                                  width: 167*fem,
                                                  height: double.infinity,
                                                  child: Container(
                                                    // autogroupeqxyRuv (F9xZYVEUHYn5zEqerNeqxY)
                                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 67*fem, 0*fem),
                                                    width: 100*fem,
                                                    height: double.infinity,
                                                    child: SizedBox(
                                                      // contentxur (I60:6113;60:4020;54116:34990)
                                                      width: double.infinity,
                                                      height: double.infinity,
                                                      child: Text(
                                                        'Imagine',
                                                        style: SafeGoogleFont (
                                                          'Roboto',
                                                          fontSize: 16*ffem,
                                                          fontWeight: FontWeight.w400,
                                                          height: 1.5*ffem/fem,
                                                          letterSpacing: 0.5*fem,
                                                          color: const Color(0xff1d1b20),
                                                        ),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ),
                                          ),
                                          Positioned(
                                            // menulistitem2gL4 (I60:6113;60:4021)
                                            left: 0*fem,
                                            top: 56*fem,
                                            child: TextButton(
                                              onPressed: () {},
                                              style: TextButton.styleFrom (
                                                padding: EdgeInsets.zero,
                                              ),
                                              child: Container(
                                                padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 12*fem, 6*fem),
                                                width: 280*fem,
                                                height: 66*fem,
                                                child: Container(
                                                  // statelayermcQ (I60:6113;60:4021;54061:37028)
                                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 89*fem, 0*fem),
                                                  width: 167*fem,
                                                  height: double.infinity,
                                                  child: Container(
                                                    // autogroupx4kwth2 (F9xZr4ZXANb8BMHzeBX4KW)
                                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 67*fem, 0*fem),
                                                    width: 100*fem,
                                                    height: double.infinity,
                                                    child: SizedBox(
                                                      // contentdPi (I60:6113;60:4021;54116:34990)
                                                      width: double.infinity,
                                                      height: double.infinity,
                                                      child: Text(
                                                        'Hey Jude',
                                                        style: SafeGoogleFont (
                                                          'Roboto',
                                                          fontSize: 16*ffem,
                                                          fontWeight: FontWeight.w400,
                                                          height: 1.5*ffem/fem,
                                                          letterSpacing: 0.5*fem,
                                                          color: const Color(0xff1d1b20),
                                                        ),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ),
                                          ),
                                          Positioned(
                                            // menulistitem39sr (I60:6113;60:4022)
                                            left: 0*fem,
                                            top: 112*fem,
                                            child: TextButton(
                                              onPressed: () {},
                                              style: TextButton.styleFrom (
                                                padding: EdgeInsets.zero,
                                              ),
                                              child: Container(
                                                padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 12*fem, 6*fem),
                                                width: 280*fem,
                                                height: 66*fem,
                                                child: Container(
                                                  // statelayer4E8 (I60:6113;60:4022;54061:37028)
                                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 89*fem, 0*fem),
                                                  width: 167*fem,
                                                  height: double.infinity,
                                                  child: Container(
                                                    // autogroupvwsq19N (F9xa68zQ7vZVT83df8vWSQ)
                                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 67*fem, 0*fem),
                                                    width: 100*fem,
                                                    height: double.infinity,
                                                    child: SizedBox(
                                                      // contentLxL (I60:6113;60:4022;54116:34990)
                                                      width: double.infinity,
                                                      height: double.infinity,
                                                      child: Text(
                                                        'Zorbas',
                                                        style: SafeGoogleFont (
                                                          'Roboto',
                                                          fontSize: 16*ffem,
                                                          fontWeight: FontWeight.w400,
                                                          height: 1.5*ffem/fem,
                                                          letterSpacing: 0.5*fem,
                                                          color: const Color(0xff1d1b20),
                                                        ),
                                                      ),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                    SizedBox(
                                      // autogroupyuunTXA (F9xbNwB6x12WFrucfkYuun)
                                      width: double.infinity,
                                      height: 112*fem,
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