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
        // rankingpagetmi (5:18)
        padding: EdgeInsets.fromLTRB(15*fem, 38*fem, 17*fem, 0*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttontextD3J (60:6311)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 13.3*fem, 49*fem),
              width: 384.7*fem,
              height: 80*fem,
              child: Stack(
                children: [
                  Positioned(
                    // backbuttonbarjXS (I60:6311;64:383)
                    left: 0*fem,
                    top: 0*fem,
                    child: Align(
                      child: SizedBox(
                        width: 384.7*fem,
                        height: 80*fem,
                        child: Image.asset(
                          'assets/prototype/images/back-button-bar.png',
                          width: 384.7*fem,
                          height: 80*fem,
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // textAse (I60:6311;64:372)
                    left: 96*fem,
                    top: 10*fem,
                    child: Align(
                      child: SizedBox(
                        width: 136*fem,
                        height: 50*fem,
                        child: Text(
                          'Ranking',
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
            Container(
              // linebuttonRoa (I80:1481;80:1334)
              margin: EdgeInsets.fromLTRB(80.38*fem, 0*fem, 81.62*fem, 72*fem),
              width: double.infinity,
              height: 171*fem,
              child: Stack(
                children: [
                  Positioned(
                    // rectangle785wX2 (I80:1481;80:1334;60:991)
                    left: 7.6150054932*fem,
                    top: 0*fem,
                    child: Align(
                      child: SizedBox(
                        width: 223*fem,
                        height: 171*fem,
                        child: Container(
                          decoration: BoxDecoration (
                            borderRadius: BorderRadius.circular(32*fem),
                            gradient: LinearGradient (
                              begin: Alignment(1, -1),
                              end: Alignment(-1, 1),
                              colors: <Color>[Color(0xffd527e9), Color(0xfffb9931)],
                              stops: <double>[0, 1],
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // rectangle786Pdv (I80:1481;80:1334;60:992)
                    left: 19.8800201416*fem,
                    top: 0*fem,
                    child: Align(
                      child: SizedBox(
                        width: 210.73*fem,
                        height: 144.28*fem,
                        child: Container(
                          decoration: BoxDecoration (
                            borderRadius: BorderRadius.circular(32*fem),
                            gradient: LinearGradient (
                              begin: Alignment(1.085, -0.951),
                              end: Alignment(-1, 1),
                              colors: <Color>[Color(0xffd01afe), Color(0xfffa6137), Color(0xffffa51e)],
                              stops: <double>[0, 0.725, 1],
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // bigmusicsymbolEuS (I80:1481;80:1477)
                    left: 49.6148834229*fem,
                    top: 23*fem,
                    child: Align(
                      child: SizedBox(
                        width: 117*fem,
                        height: 121*fem,
                        child: Image.asset(
                          'assets/prototype/images/big-music-symbol.png',
                          width: 117*fem,
                          height: 121*fem,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // youhave5musicpointscontinueadd (I60:282;60:241)
              margin: EdgeInsets.fromLTRB(1*fem, 0*fem, 0*fem, 74*fem),
              constraints: BoxConstraints (
                maxWidth: 397*fem,
              ),
              child: Text(
                'You have 5  Music Points!\nContinue adding songs \nTo increase your rank',
                textAlign: TextAlign.center,
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
              // simplelinetext2KW (I60:6047;61:1285)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 38*fem, 8*fem),
              child: Text(
                'Ranking',
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
              // menuHFS (121:6361)
              margin: EdgeInsets.fromLTRB(94*fem, 0*fem, 104*fem, 0*fem),
              padding: EdgeInsets.fromLTRB(0*fem, 8*fem, 0*fem, 0*fem),
              width: double.infinity,
              height: 690*fem,
              decoration: BoxDecoration (
                color: Color(0xfff3edf7),
                borderRadius: BorderRadius.circular(4*fem),
                boxShadow: [
                  BoxShadow(
                    color: Color(0x26000000),
                    offset: Offset(0*fem, 2*fem),
                    blurRadius: 3*fem,
                  ),
                  BoxShadow(
                    color: Color(0x4c000000),
                    offset: Offset(0*fem, 1*fem),
                    blurRadius: 1*fem,
                  ),
                ],
              ),
              child: Container(
                // menulistF5n (I121:6361;54061:36965)
                width: double.infinity,
                height: double.infinity,
                child: Container(
                  // autogroupy1241Kr (F9xKfoWwkHA4shV94gy124)
                  width: double.infinity,
                  height: 570*fem,
                  child: Stack(
                    children: [
                      Positioned(
                        // menulistitem19BA (I121:6361;54061:36966)
                        left: 0*fem,
                        top: 0*fem,
                        child: TextButton(
                          onPressed: () {},
                          style: TextButton.styleFrom (
                            padding: EdgeInsets.zero,
                          ),
                          child: Container(
                            padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 21*fem, 6*fem),
                            width: 200*fem,
                            height: 66*fem,
                            child: Container(
                              // statelayerrLU (I121:6361;54061:36966;54061:37028)
                              width: double.infinity,
                              height: double.infinity,
                              child: Container(
                                // autogroup1djlC9S (F9xKxDDGegMYm2huvt1dJL)
                                margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 14*fem, 0*fem),
                                width: 153*fem,
                                height: double.infinity,
                                child: Container(
                                  // contentYDJ (I121:6361;54061:36966;54116:34990)
                                  width: double.infinity,
                                  height: double.infinity,
                                  child: Text(
                                    '1 )  Andrew Petrovic',
                                    style: SafeGoogleFont (
                                      'Roboto',
                                      fontSize: 16*ffem,
                                      fontWeight: FontWeight.w400,
                                      height: 1.5*ffem/fem,
                                      letterSpacing: 0.5*fem,
                                      color: Color(0xff1d1b20),
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // menulistitem2R2C (I121:6361;54061:36967)
                        left: 0*fem,
                        top: 56*fem,
                        child: TextButton(
                          onPressed: () {},
                          style: TextButton.styleFrom (
                            padding: EdgeInsets.zero,
                          ),
                          child: Container(
                            padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 21*fem, 6*fem),
                            width: 200*fem,
                            height: 66*fem,
                            child: Container(
                              // statelayer68L (I121:6361;54061:36967;54061:37028)
                              width: double.infinity,
                              height: double.infinity,
                              child: Container(
                                // autogroupqeulfBS (F9xLF7tmFqF8CqbeLLQeUL)
                                margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 31*fem, 0*fem),
                                width: 136*fem,
                                height: double.infinity,
                                child: Container(
                                  // contentM4G (I121:6361;54061:36967;54116:34990)
                                  width: double.infinity,
                                  height: double.infinity,
                                  child: Text(
                                    '2 )  Peter Petrovic',
                                    style: SafeGoogleFont (
                                      'Roboto',
                                      fontSize: 16*ffem,
                                      fontWeight: FontWeight.w400,
                                      height: 1.5*ffem/fem,
                                      letterSpacing: 0.5*fem,
                                      color: Color(0xff1d1b20),
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // menulistitem3GS8 (I121:6361;54061:36968)
                        left: 0*fem,
                        top: 112*fem,
                        child: TextButton(
                          onPressed: () {},
                          style: TextButton.styleFrom (
                            padding: EdgeInsets.zero,
                          ),
                          child: Container(
                            padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 21*fem, 6*fem),
                            width: 200*fem,
                            height: 66*fem,
                            child: Container(
                              // statelayerahi (I121:6361;54061:36968;54061:37028)
                              width: double.infinity,
                              height: double.infinity,
                              child: Container(
                                // autogroupfhscYeY (F9xLV7VSvvbotCQTRkFhSc)
                                margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 47*fem, 0*fem),
                                width: 120*fem,
                                height: double.infinity,
                                child: Container(
                                  // contentG4k (I121:6361;54061:36968;54116:34990)
                                  width: double.infinity,
                                  height: double.infinity,
                                  child: Text(
                                    '3 ) Johny Joyce',
                                    style: SafeGoogleFont (
                                      'Roboto',
                                      fontSize: 16*ffem,
                                      fontWeight: FontWeight.w400,
                                      height: 1.5*ffem/fem,
                                      letterSpacing: 0.5*fem,
                                      color: Color(0xff1d1b20),
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
              ),
            ),
          ],
        ),
      ),
          );
  }
}