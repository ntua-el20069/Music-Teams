import 'package:flutter/material.dart';
import 'package:myapp/prototype/add-chords-page.dart';
import 'package:myapp/prototype/team-home-page.dart';
import 'package:myapp/utils.dart';

class AddSong extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // addsongpageZK2 (5:19)
        width: double.infinity,
        decoration: BoxDecoration (
          color: Color(0xfff3edf7),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            TextButton(
              // backbuttontextuNt (121:6397)
              onPressed: () {
                Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
              },
              style: TextButton.styleFrom (
                padding: EdgeInsets.zero,
              ),
              child: Container(
                width: double.infinity,
                height: 165*fem,
                child: Stack(
                  children: [
                    Positioned(
                      // backbuttonbarr3E (I121:6397;64:383)
                      left: 15*fem,
                      top: 38*fem,
                      child: Align(
                        child: SizedBox(
                          width: 384.7*fem,
                          height: 80*fem,
                          child: Image.asset(
                            'assets/prototype/images/back-button-bar-Ktx.png',
                            width: 384.7*fem,
                            height: 80*fem,
                          ),
                        ),
                      ),
                    ),
                    Positioned(
                      // textXQG (I121:6397;64:372)
                      left: 111*fem,
                      top: 48*fem,
                      child: Align(
                        child: SizedBox(
                          width: 155*fem,
                          height: 50*fem,
                          child: Text(
                            'New song',
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
            ),
            Container(
              // autogroupngjnCmJ (F9xHcH7mXnKUTG1TJtNGjN)
              padding: EdgeInsets.fromLTRB(13*fem, 0*fem, 13*fem, 48*fem),
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    // inputelementJpL (60:1071)
                    margin: EdgeInsets.fromLTRB(16*fem, 0*fem, 16*fem, 32*fem),
                    width: double.infinity,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          // passworddbi (I60:1071;60:121)
                          margin: EdgeInsets.fromLTRB(9*fem, 0*fem, 0*fem, 11.22*fem),
                          child: Text(
                            'Title',
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 20*ffem,
                              fontWeight: FontWeight.w400,
                              height: 1.2*ffem/fem,
                              color: Color(0xff4e36b0),
                            ),
                          ),
                        ),
                        Container(
                          // inputMXi (I60:1071;60:122)
                          width: double.infinity,
                          height: 59.78*fem,
                          decoration: BoxDecoration (
                            border: Border.all(color: Color(0xff4e36b0)),
                            borderRadius: BorderRadius.circular(4*fem),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // inputelementgpt (60:1064)
                    margin: EdgeInsets.fromLTRB(16*fem, 0*fem, 16*fem, 39*fem),
                    width: double.infinity,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          // passwordS3N (I60:1064;60:121)
                          margin: EdgeInsets.fromLTRB(9*fem, 0*fem, 0*fem, 11.22*fem),
                          child: Text(
                            'Composer',
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 20*ffem,
                              fontWeight: FontWeight.w400,
                              height: 1.2*ffem/fem,
                              color: Color(0xff4e36b0),
                            ),
                          ),
                        ),
                        Container(
                          // inputhjz (I60:1064;60:122)
                          width: double.infinity,
                          height: 59.78*fem,
                          decoration: BoxDecoration (
                            border: Border.all(color: Color(0xff4e36b0)),
                            borderRadius: BorderRadius.circular(4*fem),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // inputelementrMz (60:1078)
                    margin: EdgeInsets.fromLTRB(16*fem, 0*fem, 16*fem, 44*fem),
                    width: double.infinity,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          // passwordySc (I60:1078;60:121)
                          margin: EdgeInsets.fromLTRB(9*fem, 0*fem, 0*fem, 11.22*fem),
                          child: Text(
                            'Lyricist',
                            style: SafeGoogleFont (
                              'Zilla Slab',
                              fontSize: 20*ffem,
                              fontWeight: FontWeight.w400,
                              height: 1.2*ffem/fem,
                              color: Color(0xff4e36b0),
                            ),
                          ),
                        ),
                        Container(
                          // inputsXz (I60:1078;60:122)
                          width: double.infinity,
                          height: 59.78*fem,
                          decoration: BoxDecoration (
                            border: Border.all(color: Color(0xff4e36b0)),
                            borderRadius: BorderRadius.circular(4*fem),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // autogroupppu4d1N (F9xH3dPWHu9ssRTZRbPpU4)
                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 16*fem, 57*fem),
                    width: 388*fem,
                    height: 198*fem,
                    child: Stack(
                      children: [
                        Positioned(
                          // textfieldxJY (I61:2193;61:2156)
                          left: 16*fem,
                          top: 0*fem,
                          child: TextButton(
                            onPressed: () {
                              Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
                            },
                            style: TextButton.styleFrom (
                              padding: EdgeInsets.zero,
                            ),
                            child: Container(
                              width: 372*fem,
                              height: 155*fem,
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
                                    // textfieldcdz (I61:2193;61:2156;52798:24375)
                                    width: double.infinity,
                                    height: 135*fem,
                                    decoration: BoxDecoration (
                                      color: Color(0xffe6e0e9),
                                      borderRadius: BorderRadius.only (
                                        topLeft: Radius.circular(4*fem),
                                        topRight: Radius.circular(4*fem),
                                      ),
                                    ),
                                    child: Container(
                                      // statelayerYGk (I61:2193;61:2156;52798:24376)
                                      padding: EdgeInsets.fromLTRB(16*fem, 0*fem, 0*fem, 0*fem),
                                      width: double.infinity,
                                      height: double.infinity,
                                      decoration: BoxDecoration (
                                        borderRadius: BorderRadius.only (
                                          topLeft: Radius.circular(4*fem),
                                          topRight: Radius.circular(4*fem),
                                        ),
                                      ),
                                      child: Row(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          Container(
                                            // autogroupl5pz4kt (F9xHH3ApynCnPteb4CL5Pz)
                                            margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 255*fem, 0*fem),
                                            padding: EdgeInsets.fromLTRB(0*fem, 3*fem, 0*fem, 0*fem),
                                            child: Column(
                                              crossAxisAlignment: CrossAxisAlignment.start,
                                              children: [
                                                Container(
                                                  // passwordBqW (I61:2193;61:2174)
                                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 5*fem),
                                                  child: Text(
                                                    'Lyrics',
                                                    style: SafeGoogleFont (
                                                      'Zilla Slab',
                                                      fontSize: 20*ffem,
                                                      fontWeight: FontWeight.w400,
                                                      height: 1.2*ffem/fem,
                                                      color: Color(0xff4e36b0),
                                                    ),
                                                  ),
                                                ),
                                                Text(
                                                  // inputtextGrx (I61:2193;61:2156;52798:24381)
                                                  '|',
                                                  style: SafeGoogleFont (
                                                    'Roboto',
                                                    fontSize: 16*ffem,
                                                    fontWeight: FontWeight.w400,
                                                    height: 1.5*ffem/fem,
                                                    letterSpacing: 0.5*fem,
                                                    color: Color(0xff1d1b20),
                                                  ),
                                                ),
                                              ],
                                            ),
                                          ),
                                          Container(
                                            // trailingiconPRn (I61:2193;61:2156;52798:24382)
                                            margin: EdgeInsets.fromLTRB(0*fem, 4*fem, 0*fem, 0*fem),
                                            child: TextButton(
                                              onPressed: () {
                                                Navigator.push( context, MaterialPageRoute(builder: (context) => TeamHome()), );
                                              },
                                              style: TextButton.styleFrom (
                                                padding: EdgeInsets.zero,
                                              ),
                                              child: Container(
                                                width: 48*fem,
                                                height: 48*fem,
                                                child: Image.asset(
                                                  'assets/prototype/images/trailing-icon.png',
                                                  width: 48*fem,
                                                  height: 48*fem,
                                                ),
                                              ),
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                  ),
                                  Container(
                                    // activeindicatorSur (I61:2193;61:2156;52798:24383)
                                    margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 0*fem, 3*fem),
                                    width: double.infinity,
                                    height: 1*fem,
                                    decoration: BoxDecoration (
                                      color: Color(0xff49454f),
                                    ),
                                  ),
                                  Container(
                                    // supportingtextBcY (I61:2193;61:2156;52798:24385)
                                    margin: EdgeInsets.fromLTRB(16*fem, 0*fem, 0*fem, 0*fem),
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
                        Positioned(
                          // publicconsentUbe (60:5905)
                          left: 0*fem,
                          top: 150*fem,
                          child: Container(
                            width: 292*fem,
                            height: 48*fem,
                            child: Row(
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: [
                                Container(
                                  // checkboxes1ba (I60:5905;60:5891)
                                  margin: EdgeInsets.fromLTRB(0*fem, 0*fem, 1*fem, 0*fem),
                                  child: TextButton(
                                    onPressed: () {},
                                    style: TextButton.styleFrom (
                                      padding: EdgeInsets.zero,
                                    ),
                                    child: Container(
                                      width: 48*fem,
                                      height: 48*fem,
                                      child: Image.asset(
                                        'assets/prototype/images/checkboxes.png',
                                        width: 48*fem,
                                        height: 48*fem,
                                      ),
                                    ),
                                  ),
                                ),
                                Text(
                                  // passwordhDW (I60:5905;60:5899;60:249)
                                  'I want this song to be public',
                                  style: SafeGoogleFont (
                                    'Zilla Slab',
                                    fontSize: 20*ffem,
                                    fontWeight: FontWeight.w400,
                                    height: 1.2*ffem/fem,
                                    color: Color(0xff4e36b0),
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
                    // buttonelementSB6 (80:519)
                    margin: EdgeInsets.fromLTRB(160*fem, 0*fem, 0*fem, 0*fem),
                    child: TextButton(
                      onPressed: () {
                        Navigator.push( context, MaterialPageRoute(builder: (context) => AddChords()), );
                      },
                      style: TextButton.styleFrom (
                        padding: EdgeInsets.zero,
                      ),
                      child: Container(
                        width: 200*fem,
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
                              // rectangle786rVi (I80:519;59:261)
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
                              // buttongzY (I80:519;59:262)
                              left: 32.5*fem,
                              top: 13*fem,
                              child: Center(
                                child: Align(
                                  child: SizedBox(
                                    width: 146*fem,
                                    height: 29*fem,
                                    child: Text(
                                      'Add chords',
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
          ],
        ),
      ),
    ),
          );
  }
}