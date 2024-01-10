import 'package:flutter/material.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class Rename extends StatelessWidget {
  const Rename({super.key});

  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: SizedBox(
      width: double.infinity,
      child: Container(
        // renamepageoKA (80:1052)
        padding: EdgeInsets.fromLTRB(15*fem, 38*fem, 30*fem, 90*fem),
        width: double.infinity,
        decoration: const BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // backbuttontextih2 (80:5015)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0.3*fem, 219*fem),
              width: double.infinity,
              height: 80*fem,
              child: Stack(
                children: [
                  Positioned(
                    // backbuttonbareqa (I80:5015;64:383)
                    left: 0 * fem,
                    top: 0 * fem,
                    child: GestureDetector(
                      onTap: () {
                        // Navigate to the desired screen when the image is tapped
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => const TeamHome()), // Replace NextScreen() with your desired screen
                        );
                      },
                      child: Align(
                        child: SizedBox(
                          width: 384.7 * fem,
                          height: 80 * fem,
                          child: Image.asset(
                            'assets/prototype/images/back-button-bar-NuJ.png',
                            width: 384.7 * fem,
                            height: 80 * fem,
                          ),
                        ),
                      ),
                    ),
                  ),

                  Positioned(
                    // text9GY (I80:5015;64:372)
                    left: 96*fem,
                    top: 10*fem,
                    child: Align(
                      child: SizedBox(
                        width: 185*fem,
                        height: 50*fem,
                        child: Text(
                          'Team name',
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
              // renameteamort (80:1326)
              margin: EdgeInsets.fromLTRB(14*fem, 0*fem, 0*fem, 370*fem),
              padding: EdgeInsets.fromLTRB(11.97*fem, 20.19*fem, 10.97*fem, 21.11*fem),
              width: double.infinity,
              decoration: BoxDecoration (
                border: Border.all(color: const Color(0xff4e36b0)),
                borderRadius: BorderRadius.circular(4*fem),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // passwordrqA (I80:1326;80:1323;60:249)
                    margin: EdgeInsets.fromLTRB(0*fem, 1.19*fem, 255.14*fem, 0*fem),
                    child: Text(
                      'Team 1|',
                      style: SafeGoogleFont (
                        'Zilla Slab',
                        fontSize: 20*ffem,
                        fontWeight: FontWeight.w400,
                        height: 1.2*ffem/fem,
                        color: const Color(0xff4e36b0),
                      ),
                    ),
                  ),
                  SizedBox(
                    // autogroupbupgyun (F9xXAZCJMdydSZTN5Kbupg)
                    width: 27.92*fem,
                    height: 29.69*fem,
                    child: Image.asset(
                      'assets/prototype/images/auto-group-bupg.png',
                      width: 27.92*fem,
                      height: 29.69*fem,
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // buttonelementWPv (80:1067)
              margin: EdgeInsets.fromLTRB(100*fem, 0*fem, 85*fem, 0*fem),
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => const TeamHome()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: double.infinity,
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
                        // rectangle786KcG (I80:1067;59:261)
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
                        // buttonkSg (I80:1067;59:262)
                        left: 86*fem,
                        top: 13*fem,
                        child: Center(
                          child: Align(
                            child: SizedBox(
                              width: 38*fem,
                              height: 29*fem,
                              child: Text(
                                'OK',
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
          ],
        ),
      ),
    ),
          );
  }
}