import 'package:flutter/material.dart';
import 'package:myapp/prototype/create-a-new-team-pop-up.dart';
import 'package:myapp/prototype/home-page.dart';
import 'package:myapp/utils.dart';

class NewTeam extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // newteampagepopupAgL (5:17)
        padding: EdgeInsets.fromLTRB(15*fem, 36*fem, 15*fem, 149*fem),
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttonbarEw6 (61:409)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 15.3*fem, 93*fem),
              width: double.infinity,
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // backbuttonwqW (I61:409;59:380)
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
                    // iconmenuLMr (I61:409;61:2503)
                    margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                    width: 56.7*fem,
                    height: 70*fem,
                    child: Image.asset(
                      'assets/prototype/images/icon-menu-fcx.png',
                      width: 56.7*fem,
                      height: 70*fem,
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // entercodepopupqpQ (202:3420)
              margin: EdgeInsets.fromLTRB(44*fem, 0*fem, 44*fem, 140*fem),
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
                // basicdialogxe8 (I61:1404;61:1094;61:464)
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
                      // textcontentqxp (I61:1404;61:1094;61:464;50723:10949)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 2*fem),
                      width: double.infinity,
                      height: 44*fem,
                      child: Stack(
                        children: [
                          Positioned(
                            // titledescriptionBFz (I61:1404;61:1094;61:464;50723:10950)
                            left: 0*fem,
                            top: 0*fem,
                            child: Container(
                              width: 312*fem,
                              height: 44*fem,
                            ),
                          ),
                          Positioned(
                            // iconcloseHZv (I61:1404;61:1080)
                            left: 266*fem,
                            top: 20*fem,
                            child: Align(
                              child: SizedBox(
                                width: 23*fem,
                                height: 24*fem,
                                child: Image.asset(
                                  'assets/prototype/images/icon-close.png',
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
                      // yournewteamhasbeencreatedshare (I61:1404;61:506)
                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 26*fem),
                      child: Text(
                        'Enter Team code',
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
                      // autogrouphm6ufKa (F9xQwpPiLDU6kWSpomHM6U)
                      padding: EdgeInsets.fromLTRB(0*fem, 28.55*fem, 0*fem, 0*fem),
                      width: double.infinity,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Container(
                            // inputmtQ (I60:983;60:122)
                            margin: EdgeInsets.fromLTRB(18*fem, 0*fem, 18*fem, 78*fem),
                            padding: EdgeInsets.fromLTRB(247.06*fem, 14.41*fem, 8.16*fem, 13.78*fem),
                            width: double.infinity,
                            decoration: BoxDecoration (
                              border: Border.all(color: Color(0xff4e36b0)),
                              borderRadius: BorderRadius.circular(4*fem),
                            ),
                            child: Align(
                              // iconarrowforwardiosEX6 (I60:983;61:355)
                              alignment: Alignment.centerRight,
                              child: SizedBox(
                                width: 20.77*fem,
                                height: 20.26*fem,
                                child: TextButton(
                                  onPressed: () {
                                    Navigator.push( context, MaterialPageRoute(builder: (context) => Home()), );
                                  },
                                  style: TextButton.styleFrom (
                                    padding: EdgeInsets.zero,
                                  ),
                                  child: Image.asset(
                                    'assets/prototype/images/icon-arrow-forward-ios-Bo2.png',
                                    width: 20.77*fem,
                                    height: 20.26*fem,
                                  ),
                                ),
                              ),
                            ),
                          ),
                          Container(
                            // actionsLq2 (I61:1404;61:515)
                            width: double.infinity,
                            height: 72*fem,
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.end,
                              children: [
                                Container(
                                  // primarybuttontrY (I61:1404;61:518)
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
                                  // actions7zC (I61:1404;61:516)
                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 24*fem, 0*fem),
                                  width: 77*fem,
                                  height: 40*fem,
                                  child: TextButton(
                                    // secondarybuttonGMJ (I61:1404;61:517)
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
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Container(
              // linebuttontda (60:1001)
              margin: EdgeInsets.fromLTRB(94*fem, 0*fem, 106*fem, 0*fem),
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => CreateTeam()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: double.infinity,
                  height: 104*fem,
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
                        // rectangle786hL8 (I60:1001;60:992)
                        left: 11*fem,
                        top: 0*fem,
                        child: Align(
                          child: SizedBox(
                            width: 189*fem,
                            height: 87.75*fem,
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
                        // createanewteamXpx (I60:1001;60:993)
                        left: 38*fem,
                        top: 17*fem,
                        child: Center(
                          child: Align(
                            child: SizedBox(
                              width: 122*fem,
                              height: 58*fem,
                              child: Text(
                                'Create a new team',
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