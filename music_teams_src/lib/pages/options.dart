import 'package:flutter/material.dart';
import 'package:myapp/components/option-rectangle.dart';


class OptionsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double baseWidth = 450; //500; //450; //500; //430; //322.1;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return SingleChildScrollView(
    child: Container(
      width: double.infinity,
      child: Container(
        // optionspagesXz (5:16)
        width: double.infinity,
        height: 932*fem,
        decoration: BoxDecoration (
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
                    decoration: BoxDecoration (
                      color: Color(0xff451475),
                    ),
                  ),
                ),
              ),
            ),
            
            OptionRectangle(top: 0, buttonText: 'Options', navigateToRoute: '/options'),
          
            OptionRectangle(top: 83, buttonText: 'Disclaimer', navigateToRoute: '/disclaimer'),
            OptionRectangle(top: 166, buttonText: 'Add Song', navigateToRoute: '/add-song'),
            OptionRectangle(top: 249, buttonText: 'Song Demand', navigateToRoute: '/song-demand'),
            OptionRectangle(top: 333, buttonText: 'Live', navigateToRoute: '/live'),
            OptionRectangle(top: 416, buttonText: 'Team Home', navigateToRoute: '/team-home'),

            
          ],
        )
      )
    )
    );
  }
}
