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
        // homepagenGL (5:14)
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // autogroupdrncL2x (F9x7xogzRTuA69ZTM5DRNC)
              padding: EdgeInsets.fromLTRB(15*fem, 0*fem, 4*fem, 70*fem),
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // autogroup4rjar1J (F9x7dQ5fJYZ6qxJwFJ4Rja)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 102*fem),
                    width: double.infinity,
                    height: 168*fem,
                    child: Stack(
                      children: [
                        Positioned(
                          // musicsymbolxKE (62:1026)
                          left: 311*fem,
                          top: 18*fem,
                          child: TextButton(
                            onPressed: () {},
                            style: TextButton.styleFrom (
                              padding: EdgeInsets.zero,
                            ),
                            child: Container(
                              padding: EdgeInsets.fromLTRB(23*fem, 21*fem, 24*fem, 20.96*fem),
                              width: 100*fem,
                              height: 100*fem,
                              decoration: BoxDecoration (
                                color: Color(0xff451475),
                                borderRadius: BorderRadius.circular(50*fem),
                                boxShadow: [
                                  BoxShadow(
                                    color: Color(0x3f000000),
                                    offset: Offset(0*fem, 4*fem),
                                    blurRadius: 2*fem,
                                  ),
                                ],
                              ),
                              child: Center(
                                // group19pPN (I62:1026;62:1018)
                                child: SizedBox(
                                  width: 53*fem,
                                  height: 58.04*fem,
                                  child: Image.asset(
                                    'assets/prototype/images/group-19.png',
                                    width: 53*fem,
                                    height: 58.04*fem,
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ),
                        Positioned(
                          // signinWmz (I60:907;60:156)
                          left: 85.5*fem,
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
                          // backbuttonbarxP6 (150:1051)
                          left: 0*fem,
                          top: 37*fem,
                          child: Container(
                            width: 384.7*fem,
                            height: 80*fem,
                            child: Row(
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: [
                                Container(
                                  // backbuttonpgC (I150:1051;59:380)
                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 258*fem, 10*fem),
                                  child: TextButton(
                                    onPressed: () {},
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
                                  // iconmenuQeQ (I150:1051;61:2503)
                                  margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                                  width: 56.7*fem,
                                  height: 70*fem,
                                  child: Image.asset(
                                    'assets/prototype/images/icon-menu-SVz.png',
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
                    // buttonelementXU8 (60:204)
                    margin: EdgeInsets.fromLTRB(100*fem, 0*fem, 111*fem, 101*fem),
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
                          // rectangle786byn (I60:204;59:261)
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
                          // readyswJ (I60:204;59:262)
                          left: 64.5*fem,
                          top: 13*fem,
                          child: Center(
                            child: Align(
                              child: SizedBox(
                                width: 82*fem,
                                height: 29*fem,
                                child: Text(
                                  'Public',
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
                    // buttonelementzeY (80:5244)
                    margin: EdgeInsets.fromLTRB(100*fem, 0*fem, 111*fem, 106*fem),
                    child: TextButton(
                      onPressed: () {},
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
                              // rectangle786ptU (I80:5244;59:261)
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
                              // buttonVUp (I80:5244;59:262)
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
                  Container(
                    // buttonelement8ng (60:6084)
                    margin: EdgeInsets.fromLTRB(100*fem, 0*fem, 111*fem, 0*fem),
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
                          // rectangle786CXe (I60:6084;59:261)
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
                          // buttonHJC (I60:6084;59:262)
                          left: 59.5*fem,
                          top: 13*fem,
                          child: Center(
                            child: Align(
                              child: SizedBox(
                                width: 92*fem,
                                height: 29*fem,
                                child: Text(
                                  'Team 2',
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
              // backbuttonsNKe (80:546)
              padding: EdgeInsets.fromLTRB(171*fem, 23*fem, 159*fem, 36*fem),
              width: double.infinity,
              height: 213*fem,
              decoration: BoxDecoration (
                color: Color(0xff451475),
                borderRadius: BorderRadius.circular(5*fem),
              ),
              child: TextButton(
                // fabfpY (62:1007)
                onPressed: () {},
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: double.infinity,
                  height: double.infinity,
                  child: Stack(
                    children: [
                      Positioned(
                        // ellipse6RYp (I62:1007;60:130)
                        left: 0*fem,
                        top: 34*fem,
                        child: Align(
                          child: SizedBox(
                            width: 100*fem,
                            height: 100*fem,
                            child: Container(
                              decoration: BoxDecoration (
                                borderRadius: BorderRadius.circular(50*fem),
                                gradient: LinearGradient (
                                  begin: Alignment(0, -1),
                                  end: Alignment(0, 1),
                                  colors: <Color>[Color(0xffd01afe), Color(0xffec271b), Color(0xffffa825)],
                                  stops: <double>[0, 0.162, 0.953],
                                ),
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
                      ),
                      Positioned(
                        // EmA (I62:1007;60:131)
                        left: 17.5*fem,
                        top: 0*fem,
                        child: Center(
                          child: Align(
                            child: SizedBox(
                              width: 65*fem,
                              height: 154*fem,
                              child: Text(
                                '+',
                                textAlign: TextAlign.center,
                                style: SafeGoogleFont (
                                  'Zilla Slab',
                                  fontSize: 128*ffem,
                                  fontWeight: FontWeight.w700,
                                  height: 1.2*ffem/fem,
                                  letterSpacing: 12.8*fem,
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
          );
  }
}