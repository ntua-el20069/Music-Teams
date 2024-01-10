import 'package:flutter/material.dart';
import 'package:myapp/components/disclaimer.dart';
import 'package:myapp/pages/add-song.dart';
import 'package:myapp/pages/team-home.dart';
import 'package:myapp/utils.dart';

class OptionsPage extends StatelessWidget {
  const OptionsPage({super.key});

  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: SizedBox(
      width: double.infinity,
      child: Container(
        // optionspagesXz (5:16)
        width: double.infinity,
        height: 932*fem,
        decoration: const BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Stack(
            children: [Positioned(
              // rectangle788Tbz (80:914)
              left: 0*fem,
              top: 0*fem,
              child: Align(
                child: SizedBox(
                  width: 450*fem,
                  height: 932*fem,
                  child: Container(
                    decoration: const BoxDecoration (
                      color: Color(0xff451475),
                    ),
                  ),
                ),
              ),
            ),
            Positioned(
              // optionsnPN (80:979)
              left: 0*fem,
              top: 249*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => const Disclaimer()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  padding: EdgeInsets.fromLTRB(70.5*fem, 12.5*fem, 69.5*fem, 12.5*fem),
                  width: 450*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: const Color(0xff000000)),
                    color: const Color(0xff451475),
                  ),
                  child: Center(
                    // textHL8 (I80:979;80:959)
                    child: Center(
                      child: SizedBox(
                        child: Container(
                          
                          child: Text(
                            'Disclaimer',
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
                ),
              ),
            ),
            Positioned(
              // optionsY1A (80:983)
              left: 0*fem,
              top: 333*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => const TeamHomePage()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: 450*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: const Color(0xff000000)),
                    color: const Color(0xff451475),
                  ),
                  child: Center(
                    child: Center(
                      child: Text(
                        'Team Home',
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
            ),
            Positioned(
              // optionsksv (80:973)
              left: 0*fem,
              top: 83*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => const AddSongPage()), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: 450*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: const Color(0xff000000)),
                    color: const Color(0xff451475),
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
                          color: const Color(0xffffffff),
                        ),
                      ),
                    ),
                  ),
                ),
              ),
            ),
            Positioned(
              // optionsEHJ (80:976)
              left: 0*fem,
              top: 166*fem,
              child: TextButton(
                onPressed: () {
                  Navigator.push( context, MaterialPageRoute(builder: (context) => const TeamHomePage(mode: 'SongDemand',)), );
                },
                style: TextButton.styleFrom (
                  padding: EdgeInsets.zero,
                ),
                child: Container(
                  width: 450*fem,
                  height: 83*fem,
                  decoration: BoxDecoration (
                    border: Border.all(color: const Color(0xff000000)),
                    color: const Color(0xff451475),
                  ),
                  child: Center(
                    child: Center(
                      child: Text(
                        'Song Demand',
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
            ),
            Positioned(
              // optionsERi (80:970)
              left: 0*fem,
              top: 0*fem,
              child: Container(
                width: 450*fem,
                height: 83*fem,
                decoration: BoxDecoration (
                  border: Border.all(color: const Color(0xff000000)),
                  color: const Color(0xff451475),
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
                        color: const Color(0xffffffff),
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        )
      )
    )
    );
  }
}
