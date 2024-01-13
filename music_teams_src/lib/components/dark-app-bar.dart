import 'package:flutter/material.dart';
import 'package:myapp/pages/options.dart';
import 'package:myapp/utils.dart';

class PurpleAppBar extends StatelessWidget implements PreferredSizeWidget {
  final String header;

  PurpleAppBar({required this.header});

  @override
  Widget build(BuildContext context) {
    double fem = MediaQuery.of(context).size.width / 450; // Adjust as needed
    double ffem = fem * 0.97;
    return AppBar(
      title: Text(header),
      titleTextStyle: TextStyle (
        fontFamily: 'Zilla Slab',
        fontSize: 22*ffem,
        fontWeight: FontWeight.w700,
        height: 1.2*ffem/fem,
        letterSpacing: 2.4*fem,
        color: Color(0xffffffff),
      ),
      backgroundColor: Color(0xff451475),
      automaticallyImplyLeading: true,
      foregroundColor: Color(0xFFFFFFFF),
      actions: [
        Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            IconButton(
              icon: Image.asset(
                'assets/assets-components/images/3-line-menu-icon-13.jpeg',
                width: 50 * fem,
                height: 50 * fem,
              ),
              onPressed: () {
                // Add your button's functionality here
                Navigator.push(context, MaterialPageRoute(builder: (context) => OptionsPage()));
              },
            ),
          ],
        ),
      ],
    );
  }

  @override
  Size get preferredSize => AppBar().preferredSize;
}
