import 'package:flutter/material.dart';
import 'package:myapp/prototype/home-page.dart';
import 'package:myapp/prototype/live-team-1.dart';
import 'package:myapp/prototype/options-page.dart';
import 'package:myapp/prototype/song-page.dart';
import 'package:myapp/utils.dart';

class TeamHome extends StatelessWidget {
  const TeamHome({super.key});

  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: SizedBox(
      width: double.infinity,
      child: Container(
        // teamhomepageFoJ (5:15)
        padding: EdgeInsets.fromLTRB(15*fem, 33*fem, 15*fem, 0*fem),
        width: double.infinity,
        decoration: const BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              // autogroup5fpaZJC (F9x8tcUfjuL9NrDDia5FPA)
              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 15.3*fem, 121*fem),
              width: 384.7*fem,
              height: 85*fem,
              child: Stack(
                children: [
                  Positioned(
                    // backbuttonbarS76 (60:6225)
                    left: 0*fem,
                    top: 5*fem,
                    child: SizedBox(
                      width: 384.7*fem,
                      height: 80*fem,
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Container(
                            // backbuttonxbE (I60:6225;59:380)
                            margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 258*fem, 10*fem),
                            child: TextButton(
                              onPressed: () {
                                Navigator.push( context, MaterialPageRoute(builder: (context) => const Home()), );
                              },
                              style: TextButton.styleFrom (
                                padding: EdgeInsets.zero,
                              ),
                              child: Container(
                                padding: EdgeInsets.fromLTRB(16.1*fem, 35*fem, 16.8*fem, 35*fem),
                                decoration: BoxDecoration (
                                  color: const Color(0xff451475),
                                  borderRadius: BorderRadius.circular(35*fem),
                                  boxShadow: [
                                    BoxShadow(
                                      color: const Color(0x3f000000),
                                      offset: Offset(0*fem, 4*fem),
                                      blurRadius: 2*fem,
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                          Container(
                            // iconmenuYZS (I60:6225;61:2503)
                            margin: EdgeInsets.fromLTRB(0*fem, 10*fem, 0*fem, 0*fem),
                            width: 56.7*fem,
                            height: 70*fem,
                            child: Image.asset(
                              'assets/prototype/images/icon-menu.png',
                              width: 56.7*fem,
                              height: 70*fem,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  Positioned(
                    // iconmenus5v (121:6345)
                    left: 307*fem,
                    top: 0*fem,
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => const Options()), );
                      },
                      style: TextButton.styleFrom (
                        padding: EdgeInsets.zero,
                      ),
                      child: Container(
                        padding: EdgeInsets.fromLTRB(9.62*fem, 18.75*fem, 9.62*fem, 18.75*fem),
                        width: 76.93*fem,
                        height: 75*fem,
                        decoration: const BoxDecoration (
                          image: DecorationImage (
                            fit: BoxFit.cover,
                            image: AssetImage (
                              'assets/prototype/images/vector.png',
                            ),
                          ),
                        ),
                        child: Center(
                          // vectorx7N (121:6344)
                          child: SizedBox(
                            width: 57.7*fem,
                            height: 37.5*fem,
                            child: Image.asset(
                              'assets/prototype/images/vector-gfv.png',
                              width: 57.7*fem,
                              height: 37.5*fem,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    // simplelinetexteVz (I121:6347;61:1285)
                    left: 119*fem,
                    top: 13*fem,
                    child: Align(
                      child: SizedBox(
                        width: 111*fem,
                        height: 50*fem,
                        child: Text(
                          'Team 1',
                          style: SafeGoogleFont (
                            'Zilla Slab',
                            fontSize: 36*ffem,
                            fontWeight: FontWeight.w700,
                            height: 1.3888888889*ffem/fem,
                            color: const Color(0xff000000),
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              // autogroupalqcJKe (F9x95Gqa4e5XKhCytDaLQc)
              margin: EdgeInsets.fromLTRB(15*fem, 0*fem, 16*fem, 0*fem),
              width: double.infinity,
              height: 754*fem,
              child: Stack(
                children: [
                  Positioned(
                    // frame1Ej6 (60:309)
                    left: 67*fem,
                    top: 439*fem,
                    child: SizedBox(
                      width: 100*fem,
                      height: 100*fem,
                    ),
                  ),
                  Positioned(
                    // buttonelementmU8 (80:871)
                    left: 85*fem,
                    top: 539*fem,
                    child: TextButton(// TextButton
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
                              // rectangle786ne8 (I80:871;59:261)
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
                              // button4rY (I80:871;59:262)
                              left: 78 * fem,
                              top: 13 * fem, // 13
                              child: GestureDetector(
                                onTap: () {
                                  // Navigate to the desired screen when the text is tapped
                                  Navigator.push(
                                    context,
                                    MaterialPageRoute(builder: (context) => const Live()), // Replace LiveScreen() with your desired screen
                                  );
                                },
                                child: Center(
                                  child: Align(
                                    child: SizedBox(
                                      width: 54 * fem,
                                      height: 29 * fem,
                                      child: Text(
                                        'Live',
                                        textAlign: TextAlign.center,
                                        style: TextStyle(
                                          fontFamily: 'Zilla Slab',
                                          fontSize: 24 * ffem,
                                          fontWeight: FontWeight.w700,
                                          height: 1.2 * ffem / fem,
                                          letterSpacing: 2.4 * fem,
                                          color: const Color(0xffffffff),
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
                  Positioned(
                    // searchsongYFv (60:6169)
                    left: 0*fem,
                    top: 0*fem,
                    child: TextButton(
                      onPressed: () {
                        
                      },
                      style: TextButton.styleFrom (
                        padding: EdgeInsets.zero,
                      ),
                      child: SizedBox(
                        width: 369*fem,
                        height: 754*fem,
                        child: Stack(
                          children: [
                            Positioned(
                              // textfield2Rz (I60:6169;60:4017)
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
                                      // textfieldXde (I60:6169;60:4017;52798:24695)
                                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 4*fem),
                                      width: double.infinity,
                                      height: 64*fem,
                                      decoration: BoxDecoration (
                                        border: Border.all(color: const Color(0xff6750a4)),
                                        borderRadius: BorderRadius.circular(4*fem),
                                      ),
                                      child: Container(
                                        // statelayerG5S (I60:6169;60:4017;52798:24696)
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
                                              // autogroupynxwxix (F9x9KMGT2C3tbTxcuAynXW)
                                              margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 264*fem, 8*fem),
                                              child: Column(
                                                crossAxisAlignment: CrossAxisAlignment.start,
                                                children: [
                                                  Container(
                                                    // labeltext4GC (I60:6169;60:4017;52798:24702)
                                                    margin: EdgeInsets.fromLTRB(8*fem, 0*fem, 0*fem, 0*fem),
                                                    width: 48*fem,
                                                    height: 16*fem,
                                                    decoration: const BoxDecoration (
                                                      color: Color(0xfffef7ff),
                                                    ),
                                                    child: Center(
                                                      child: Text(
                                                        'Team 1',
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
                                                    // leadingiconYSG (I60:6169;60:4017;52798:24697)
                                                    width: 40*fem,
                                                    height: 40*fem,
                                                    child: Image.asset(
                                                      'assets/prototype/images/leading-icon.png',
                                                      width: 40*fem,
                                                      height: 40*fem,
                                                    ),
                                                  ),
                                                ],
                                              ),
                                            ),
                                            Container(
                                              // iconarrowforwardiosSXe (I60:6169;61:8579)
                                              margin: EdgeInsets.fromLTRB(0*fem, 7*fem, 0*fem, 0*fem),
                                              width: 30.38*fem,
                                              height: 25*fem,
                                              child: Image.asset(
                                                'assets/prototype/images/icon-arrow-forward-ios.png',
                                                width: 30.38*fem,
                                                height: 25*fem,
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                    Container(
                                      // supportingtext77z (I60:6169;60:4017;52798:24706)
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
                              // menud6L (I60:6169;60:4018)
                              left: 2*fem,
                              top: 64*fem, // 64
                              child: Container(
                                padding: EdgeInsets.fromLTRB(0*fem, 8*fem, 0*fem, 0*fem),
                                width: 280*fem,
                                height: 300*fem, // 690
                                decoration: BoxDecoration (
                                  color: const Color(0xffe6e0e9),
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
                                  // menulistfoi (I60:6169;60:4019)
                                  width: double.infinity,
                                  height: double.infinity,
                                  child: Column(
                                    crossAxisAlignment: CrossAxisAlignment.center,
                                    children: [
                                      SizedBox(
                                        // autogroupjob2dEk (F9x9wFQJKyD7KQNjngjob2)
                                        width: double.infinity,
                                        height: 570*fem, // 570
                                        child: Stack(
                                          children: [
                                            Positioned(
                                              // menulistitem1joa (I60:6169;60:4020)
                                              left: 0*fem,
                                              top: 0*fem,
                                              child: TextButton(
                                                onPressed: () {
                                                  Navigator.push( context, MaterialPageRoute(builder: (context) => const Song()), );
                                                },
                                                style: TextButton.styleFrom (
                                                  padding: EdgeInsets.zero,
                                                ),
                                                child: Container(
                                                  padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 12*fem, 6*fem),
                                                  width: 280*fem,
                                                  height: 66*fem,
                                                  child: Container(
                                                    // statelayerpa8 (I60:6169;60:4020;54061:37028)
                                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 89*fem, 0*fem),
                                                    width: 167*fem,
                                                    height: double.infinity,
                                                    child: Container(
                                                      // autogroupxyp2Ym2 (F9xAJzH5PjnHBA6PjhXyP2)
                                                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 67*fem, 0*fem),
                                                      width: 100*fem,
                                                      height: double.infinity,
                                                      child: SizedBox(
                                                        // content5W4 (I60:6169;60:4020;54116:34990)
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
                                              // menulistitem2Rrk (I60:6169;60:4021)
                                              left: 0*fem,
                                              top: 56*fem,
                                              child: TextButton(
                                                onPressed: () {
                                                  Navigator.push( context, MaterialPageRoute(builder: (context) => const Song()), );
                                                },
                                                style: TextButton.styleFrom (
                                                  padding: EdgeInsets.zero,
                                                ),
                                                child: Container(
                                                  padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 12*fem, 6*fem),
                                                  width: 280*fem,
                                                  height: 66*fem,
                                                  child: Container(
                                                    // statelayerKx8 (I60:6169;60:4021;54061:37028)
                                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 89*fem, 0*fem),
                                                    width: 167*fem,
                                                    height: double.infinity,
                                                    child: Container(
                                                      // autogroupkqjesik (F9xAaKAscAytM82RbpKQjE)
                                                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 67*fem, 0*fem),
                                                      width: 100*fem,
                                                      height: double.infinity,
                                                      child: SizedBox(
                                                        // contentz2g (I60:6169;60:4021;54116:34990)
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
                                              // menulistitem3hxg (I60:6169;60:4022)
                                              left: 0*fem,
                                              top: 112*fem,
                                              child: TextButton(
                                                onPressed: () {
                                                  Navigator.push( context, MaterialPageRoute(builder: (context) => const Song()), );
                                                },
                                                style: TextButton.styleFrom (
                                                  padding: EdgeInsets.zero,
                                                ),
                                                child: Container(
                                                  padding: EdgeInsets.fromLTRB(12*fem, 16*fem, 12*fem, 6*fem),
                                                  width: 280*fem,
                                                  height: 66*fem,
                                                  child: Container(
                                                    // statelayernDS (I60:6169;60:4022;54061:37028)
                                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 89*fem, 0*fem),
                                                    width: 167*fem,
                                                    height: double.infinity,
                                                    child: Container(
                                                      // autogroup3fqgvqS (F9xAp97AiM7Cqewar93fQG)
                                                      margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 67*fem, 0*fem),
                                                      width: 100*fem,
                                                      height: double.infinity,
                                                      child: SizedBox(
                                                        // content5TS (I60:6169;60:4022;54116:34990)
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
                                        // autogroupjnzp16C (F9xBvMmAW9SXHxkdcejNzp)
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