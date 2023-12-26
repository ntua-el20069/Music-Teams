import 'package:flutter/material.dart';
import 'package:myapp/prototype/home-page.dart';
import 'package:myapp/utils.dart';

class CreateTeam extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // createanewteampopuptpC (5:21)
        padding: EdgeInsets.fromLTRB(12*fem, 0*fem, 12*fem, 361*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttonbarR3S (202:3502)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 21.3*fem, 73*fem),
              width: 384.7*fem,
              height: 168*fem,
              child: Stack(
                children: [
                  Positioned(
                    // backbuttonbarYdr (202:3503)
                    left: 0*fem,
                    top: 49*fem,
                    child: Container(
                      width: 384.7*fem,
                      height: 80*fem,
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Container(
                            // backbutton11e (I202:3503;59:380)
                            margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 258*fem, 10*fem),
                            child: TextButton(
                              onPressed: () {
                                Navigator.push( context, MaterialPageRoute(builder: (context) => Home()), );
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
                            // iconmenuPXz (I202:3503;61:2503)
                            margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                            width: 56.7*fem,
                            height: 70*fem,
                            child: Image.asset(
                              'assets/prototype/images/icon-menu-iMS.png',
                              width: 56.7*fem,
                              height: 70*fem,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  Positioned(
                    // signinFKJ (I202:3504;60:156)
                    left: 98.5*fem,
                    top: 0*fem,
                    child: Align(
                      child: SizedBox(
                        width: 217*fem,
                        height: 168*fem,
                        child: Text(
                          'MY TEAMS',
                          textAlign: TextAlign.center,
                          style: SafeGoogleFont (
                            'Zilla Slab',
                            fontSize: 48*ffem,
                            fontWeight: FontWeight.w700,
                            height: 3.5*ffem/fem,
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // popupwindowcreateteam76c (202:3316)
              margin: EdgeInsets.fromLTRB(53*fem, 0*fem, 41*fem, 0*fem),
              width: double.infinity,
              height: 330*fem,
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
                // basicdialogD9e (I64:293;61:1094;61:464)
                padding: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 3*fem),
                width: double.infinity,
                height: double.infinity,
                decoration: BoxDecoration (
                  color: Color(0xffece6f0),
                  borderRadius: BorderRadius.circular(28*fem),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Container(
                      // textcontentWeY (I64:293;61:1094;61:464;50723:10949)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 2*fem),
                      width: double.infinity,
                      height: 44*fem,
                      child: Stack(
                        children: [
                          Positioned(
                            // titledescriptionT3z (I64:293;61:1094;61:464;50723:10950)
                            left: 0*fem,
                            top: 0*fem,
                            child: Container(
                              width: 312*fem,
                              height: 44*fem,
                            ),
                          ),
                          Positioned(
                            // iconcloseyHE (I64:293;61:1080)
                            left: 266*fem,
                            top: 20*fem,
                            child: Align(
                              child: SizedBox(
                                width: 23*fem,
                                height: 24*fem,
                                child: Image.asset(
                                  'assets/prototype/images/icon-close-F5e.png',
                                  width: 23*fem,
                                  height: 24*fem,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                    Container(
                      // autogrouprsontQC (F9xUMUDNj9P1iCbYVwrSoN)
                      width: double.infinity,
                      height: 281*fem,
                      child: Stack(
                        children: [
                          Positioned(
                            // yournewteamhasbeencreatedshare (I64:293;61:506)
                            left: 22*fem,
                            top: 0*fem,
                            child: Align(
                              child: SizedBox(
                                width: 268*fem,
                                height: 140*fem,
                                child: Text(
                                  'Your new team has been created!\nShare the team code with your friends\nTeam code: \n',
                                  textAlign: TextAlign.center,
                                  style: SafeGoogleFont (
                                    'Zilla Slab',
                                    fontSize: 24*ffem,
                                    fontWeight: FontWeight.w400,
                                    height: 1.1666666667*ffem/fem,
                                    color: Color(0xff000000),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          Positioned(
                            // actionsRYY (I64:293;61:515)
                            left: 0*fem,
                            top: 209*fem,
                            child: Container(
                              width: 312*fem,
                              height: 72*fem,
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.end,
                                children: [
                                  Container(
                                    // primarybuttonLQc (I64:293;61:518)
                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 12*fem),
                                    child: TextButton(
                                      onPressed: () {
                                        Navigator.push( context, MaterialPageRoute(builder: (context) => Home()), );
                                      },
                                      style: TextButton.styleFrom (
                                        padding: EdgeInsets.zero,
                                      ),
                                      child: Container(
                                        width: double.infinity,
                                        height: 68*fem,
                                        decoration: BoxDecoration (
                                          borderRadius: BorderRadius.circular(100*fem),
                                        ),
                                        child: Center(
                                          child: Center(
                                            child: Text(
                                              'OK!',
                                              textAlign: TextAlign.center,
                                              style: SafeGoogleFont (
                                                'Roboto',
                                                fontSize: 14*ffem,
                                                fontWeight: FontWeight.w500,
                                                height: 1.4285714286*ffem/fem,
                                                letterSpacing: 0.1000000015*fem,
                                                color: Color(0xff6750a4),
                                              ),
                                            ),
                                          ),
                                        ),
                                      ),
                                    ),
                                  ),
                                  Container(
                                    // actionsoZ6 (I64:293;61:516)
                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 24*fem, 0*fem),
                                    width: 77*fem,
                                    height: 40*fem,
                                    child: TextButton(
                                      // secondarybutton6HJ (I64:293;61:517)
                                      onPressed: () {
                                        Navigator.push( context, MaterialPageRoute(builder: (context) => Home()), );
                                      },
                                      style: TextButton.styleFrom (
                                        padding: EdgeInsets.zero,
                                      ),
                                      child: Container(
                                        padding: EdgeInsets.fromLTRB(3*fem, 10*fem, 3*fem, 10*fem),
                                        width: double.infinity,
                                        height: double.infinity,
                                        decoration: BoxDecoration (
                                          borderRadius: BorderRadius.circular(100*fem),
                                        ),
                                        child: Center(
                                          child: Text(
                                            'Action 2',
                                            textAlign: TextAlign.center,
                                            style: SafeGoogleFont (
                                              'Roboto',
                                              fontSize: 14*ffem,
                                              fontWeight: FontWeight.w500,
                                              height: 1.4285714286*ffem/fem,
                                              letterSpacing: 0.1000000015*fem,
                                              color: Color(0xff6750a4),
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
                            // textfieldx4c (I64:293;61:524;60:136)
                            left: 41*fem,
                            top: 154*fem,
                            child: TextButton(
                              onPressed: () {
                                Navigator.push( context, MaterialPageRoute(builder: (context) => Home()), );
                              },
                              style: TextButton.styleFrom (
                                padding: EdgeInsets.zero,
                              ),
                              child: Container(
                                width: 230*fem,
                                height: 76*fem,
                                decoration: BoxDecoration (
                                  border: Border.all(color: Color(0xff4e36b0)),
                                  borderRadius: BorderRadius.only (
                                    topLeft: Radius.circular(4*fem),
                                    topRight: Radius.circular(4*fem),
                                  ),
                                  boxShadow: [
                                    BoxShadow(
                                      color: Color(0x3f000000),
                                      offset: Offset(0*fem, 4*fem),
                                      blurRadius: 2*fem,
                                    ),
                                  ],
                                ),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  children: [
                                    Container(
                                      // textfieldmnk (I64:293;61:524;60:136;52798:24375)
                                      width: double.infinity,
                                      height: 56*fem,
                                      decoration: BoxDecoration (
                                        color: Color(0xffe6e0e9),
                                        borderRadius: BorderRadius.only (
                                          topLeft: Radius.circular(4*fem),
                                          topRight: Radius.circular(4*fem),
                                        ),
                                      ),
                                      child: Container(
                                        // statelayerKJU (I64:293;61:524;60:136;52798:24376)
                                        padding: EdgeInsets.fromLTRB(16*fem, 8*fem, 15.07*fem, 8*fem),
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
                                              // contente5r (I64:293;61:524;60:136;52798:24377)
                                              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 59*fem, 8*fem),
                                              padding: EdgeInsets.fromLTRB(0*fem, 8*fem, 0*fem, 0*fem),
                                              child: Text(
                                                'wDj4kdPDie',
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
                                            Container(
                                              // autogroupbjucuXa (F9xUuncrqC5svPN8h4bJUC)
                                              width: 48.93*fem,
                                              height: 40*fem,
                                              child: Image.asset(
                                                'assets/prototype/images/auto-group-bjuc.png',
                                                width: 48.93*fem,
                                                height: 40*fem,
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                    Container(
                                      // autogroupkywiDYG (F9xUnD1A1S6kvpLwgYkywi)
                                      padding: EdgeInsets.fromLTRB(16*fem, 4*fem, 16*fem, 0*fem),
                                      width: double.infinity,
                                      child: Text(
                                        'Supporting text',
                                        style: SafeGoogleFont (
                                          'Roboto',
                                          fontSize: 12*ffem,
                                          fontWeight: FontWeight.w400,
                                          height: 1.3333333333*ffem/fem,
                                          color: Color(0xff49454f),
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
          ],
        ),
      ),
    ),
          );
  }
}