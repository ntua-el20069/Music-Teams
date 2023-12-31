import 'package:flutter/material.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class TeamCode extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // teamcodepopupCTE (61:1533)
        padding: EdgeInsets.fromLTRB(15*fem, 0*fem, 15*fem, 375*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttonbarU9r (61:2657)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 15.3*fem, 59*fem),
              width: 384.7*fem,
              height: 168*fem,
              child: Stack(
                children: [
                  Positioned(
                    // backbuttonbarz8C (61:2658)
                    left: 0*fem,
                    top: 49*fem,
                    child: Container(
                      width: 384.7*fem,
                      height: 80*fem,
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Container(
                            // backbuttonuW4 (I61:2658;59:380)
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
                            // iconmenuiyJ (I61:2658;61:2503)
                            margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                            width: 56.7*fem,
                            height: 70*fem,
                            child: Image.asset(
                              'assets/prototype/images/icon-menu-Gya.png',
                              width: 56.7*fem,
                              height: 70*fem,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  Positioned(
                    // signinqY8 (I61:2659;60:156)
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
              // shareteamcodepopup7Ek (202:3286)
              margin: EdgeInsets.fromLTRB(44*fem, 0*fem, 44*fem, 0*fem),
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
                // basicdialogRFS (I61:1820;61:464)
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
                      // textcontentjX2 (I61:1820;61:464;50723:10949)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 2*fem),
                      width: double.infinity,
                      height: 44*fem,
                      child: Stack(
                        children: [
                          Positioned(
                            // titledescriptionUDi (I61:1820;61:464;50723:10950)
                            left: 0*fem,
                            top: 0*fem,
                            child: Container(
                              width: 312*fem,
                              height: 44*fem,
                            ),
                          ),
                          Positioned(
                            // iconclosewd6 (61:1821)
                            left: 266*fem,
                            top: 20*fem,
                            child: Align(
                              child: SizedBox(
                                width: 23*fem,
                                height: 24*fem,
                                child: Image.asset(
                                  'assets/prototype/images/icon-close-xF6.png',
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
                      // herestheteamcodeRoA (61:1822)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 35*fem),
                      child: Text(
                        'Here’s the Team code: \n',
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
                    Container(
                      // autogroup2mqp7fz (F9xgA3iN4hrfFQrb522mQp)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 15*fem),
                      padding: EdgeInsets.fromLTRB(20.5*fem, 0*fem, 20.5*fem, 5*fem),
                      width: double.infinity,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Container(
                            // textfieldRgg (61:1876)
                            margin: EdgeInsets.fromLTRB(20.5*fem, 0*fem, 20.5*fem, 22*fem),
                            child: TextButton(
                              onPressed: () {
                                Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
                              },
                              style: TextButton.styleFrom (
                                padding: EdgeInsets.zero,
                              ),
                              child: Container(
                                width: double.infinity,
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
                                      // textfieldKfa (I61:1876;52798:24375)
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
                                        // statelayerqdv (I61:1876;52798:24376)
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
                                              // contentYHS (I61:1876;52798:24377)
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
                                              // autogroupcw12c2Q (F9xgb2zjCNRTFGSU2FcW12)
                                              width: 48.93*fem,
                                              height: 40*fem,
                                              child: Image.asset(
                                                'assets/prototype/images/auto-group-cw12.png',
                                                width: 48.93*fem,
                                                height: 40*fem,
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                    Container(
                                      // autogrouptnvqh3r (F9xgThscDzHP2wFknNTNvQ)
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
                          Text(
                            // shareitwithyourfriendsN9z (61:2070)
                            'Share it with your friends!',
                            textAlign: TextAlign.center,
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 24*ffem,
                              fontWeight: FontWeight.w400,
                              height: 1.1666666667*ffem/fem,
                              color: Color(0xff000000),
                            ),
                          ),
                        ],
                      ),
                    ),
                    Container(
                      // actionsJZS (61:1823)
                      width: double.infinity,
                      height: 72*fem,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: [
                          Container(
                            // primarybutton4Hi (61:1824)
                            margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 12*fem),
                            child: TextButton(
                              onPressed: () {
                                Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
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
                            // actionsV88 (61:1825)
                            margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 24*fem, 0*fem),
                            width: 77*fem,
                            height: 40*fem,
                            child: TextButton(
                              // secondarybuttonDK2 (61:1826)
                              onPressed: () {
                                Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
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