import 'package:flutter/material.dart';
import 'package:myapp/prototype/add-chords-page.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class AddRecording extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // addrecpageS3v (61:1909)
        padding: EdgeInsets.fromLTRB(15*fem, 0*fem, 15*fem, 393*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttonbarZ8Y (61:2669)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 15.3*fem, 41*fem),
              width: 384.7*fem,
              height: 168*fem,
              child: Stack(
                children: [
                  Positioned(
                    // backbuttonbarq64 (61:2670)
                    left: 0*fem,
                    top: 49*fem,
                    child: Container(
                      padding: EdgeInsets.fromLTRB(328*fem, 10*fem, 0*fem, 0*fem),
                      width: 384.7*fem,
                      height: 80*fem,
                      child: Align(
                        // iconmenuxAg (I61:2670;61:2503)
                        alignment: Alignment.bottomRight,
                        child: SizedBox(
                          width: 56.7*fem,
                          height: 70*fem,
                          child: Image.asset(
                            'assets/prototype/images/icon-menu-uB2.png',
                            width: 56.7*fem,
                            height: 70*fem,
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // signint4L (I61:2671;60:156)
                    left: 97.5*fem,
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
                  Positioned(
                    // backbuttonbarLS8 (202:3482)
                    left: 0*fem,
                    top: 0*fem,
                    child: Container(
                      width: 384.7*fem,
                      height: 168*fem,
                      child: Stack(
                        children: [
                          Positioned(
                            // backbuttonbarfzC (202:3483)
                            left: 0*fem,
                            top: 49*fem,
                            child: Container(
                              width: 384.7*fem,
                              height: 80*fem,
                              child: Row(
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  Container(
                                    // backbutton1YG (I202:3483;59:380)
                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 258*fem, 10*fem),
                                    child: TextButton(
                                      onPressed: () {
                                        Navigator.push( context, MaterialPageRoute(builder: (context) => AddChords()), );
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
                                    // iconmenuCMr (I202:3483;61:2503)
                                    margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                                    width: 56.7*fem,
                                    height: 70*fem,
                                    child: Image.asset(
                                      'assets/prototype/images/icon-menu-Ptx.png',
                                      width: 56.7*fem,
                                      height: 70*fem,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                          Positioned(
                            // signinsD6 (I202:3484;60:156)
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
                  ),
                ],
              ),
            ),
            Container(
              // recpopupkXn (202:3253)
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
                // recpopup4YU (202:3180)
                width: double.infinity,
                height: double.infinity,
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
                  // basicdialogaWp (I202:3180;186:1144;61:1094;61:464)
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
                        // textcontentHw2 (I202:3180;186:1144;61:1094;61:464;50723:10949)
                        margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 2*fem),
                        width: double.infinity,
                        height: 44*fem,
                        child: Stack(
                          children: [
                            Positioned(
                              // titledescriptionpRA (I202:3180;186:1144;61:1094;61:464;50723:10950)
                              left: 0*fem,
                              top: 0*fem,
                              child: Container(
                                width: 312*fem,
                                height: 44*fem,
                              ),
                            ),
                            Positioned(
                              // iconclose9CY (I202:3180;186:1144;61:1080)
                              left: 266*fem,
                              top: 20*fem,
                              child: Align(
                                child: SizedBox(
                                  width: 23*fem,
                                  height: 24*fem,
                                  child: Image.asset(
                                    'assets/prototype/images/icon-close-AxL.png',
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
                        // yournewteamhasbeencreatedshare (I202:3180;186:1144;61:506)
                        margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 14*fem),
                        child: Text(
                          'Start recording',
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
                        // recordingYEg (I202:3180;186:1147)
                        margin: EdgeInsets.fromLTRB(126*fem, 0*fem, 126*fem, 4*fem),
                        padding: EdgeInsets.fromLTRB(16.98*fem, 13.42*fem, 17.56*fem, 13.67*fem),
                        width: double.infinity,
                        decoration: BoxDecoration (
                          border: Border.all(color: Color(0xff451475)),
                          color: Color(0x00ffffff),
                          borderRadius: BorderRadius.circular(30*fem),
                        ),
                        child: Center(
                          // vectorqzU (I202:3180;186:1147;60:1402)
                          child: SizedBox(
                            width: 25.46*fem,
                            height: 32.91*fem,
                            child: Image.asset(
                              'assets/prototype/images/vector-V16.png',
                              width: 25.46*fem,
                              height: 32.91*fem,
                            ),
                          ),
                        ),
                      ),
                      Container(
                        // autogroupnzclBYY (F9xhjW5yeZNCiimpiTNzcL)
                        width: double.infinity,
                        height: 175*fem,
                        child: Stack(
                          children: [
                            Positioned(
                              // actionsfic (I202:3180;186:1144;61:515)
                              left: 0*fem,
                              top: 103*fem,
                              child: Container(
                                width: 312*fem,
                                height: 72*fem,
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.end,
                                  children: [
                                    Container(
                                      // primarybuttonZZ6 (I202:3180;186:1144;61:518)
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
                                      // actionscGU (I202:3180;186:1144;61:516)
                                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 24*fem, 0*fem),
                                      width: 77*fem,
                                      height: 40*fem,
                                      child: TextButton(
                                        // secondarybuttonLiG (I202:3180;186:1144;61:517)
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
                            ),
                            Positioned(
                              // textfieldz28 (I202:3180;186:1144;61:524;60:136)
                              left: 41*fem,
                              top: 48*fem,
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
                                      // textfieldecU (I202:3180;186:1144;61:524;60:136;52798:24375)
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
                                        // statelayermwz (I202:3180;186:1144;61:524;60:136;52798:24376)
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
                                              // contentryS (I202:3180;186:1144;61:524;60:136;52798:24377)
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
                                              // autogroup5q3nADS (F9xiNjWwVgNLwGKANg5Q3n)
                                              width: 48.93*fem,
                                              height: 40*fem,
                                              child: Image.asset(
                                                'assets/prototype/images/auto-group-5q3n.png',
                                                width: 48.93*fem,
                                                height: 40*fem,
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                    Container(
                                      // autogroupf5xj6ct (F9xiF9uEfvPDwhHyNAF5XJ)
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
                            Positioned(
                              // primarybuttonDSc (I202:3180;186:1145)
                              left: 0*fem,
                              top: 103*fem,
                              child: TextButton(
                                onPressed: () {
                                  Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
                                },
                                style: TextButton.styleFrom (
                                  padding: EdgeInsets.zero,
                                ),
                                child: Container(
                                  width: 312*fem,
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
                            Positioned(
                              // uploadrecordingeXv (I202:3180;186:1148)
                              left: 65.5*fem,
                              top: 13*fem,
                              child: Align(
                                child: SizedBox(
                                  width: 181*fem,
                                  height: 28*fem,
                                  child: Text(
                                    'Upload recording',
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
                              // uploadbuttontSG (I202:3180;186:1149)
                              left: 126*fem,
                              top: 50*fem,
                              child: Container(
                                padding: EdgeInsets.fromLTRB(5.49*fem, 8.87*fem, 5.49*fem, 7.64*fem),
                                width: 60*fem,
                                height: 60*fem,
                                decoration: BoxDecoration (
                                  border: Border.all(color: Color(0xff451475)),
                                  color: Color(0x00ffffff),
                                  borderRadius: BorderRadius.circular(30*fem),
                                ),
                                child: Center(
                                  // iconuploadapt (I202:3180;186:1149;61:2014)
                                  child: SizedBox(
                                    width: 49.01*fem,
                                    height: 43.48*fem,
                                    child: Image.asset(
                                      'assets/prototype/images/icon-upload.png',
                                      width: 49.01*fem,
                                      height: 43.48*fem,
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
            ),
          ],
        ),
      ),
    ),
          );
  }
}