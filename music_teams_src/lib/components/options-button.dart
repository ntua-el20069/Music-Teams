import 'package:flutter/material.dart';
import 'package:myapp/prototype/options-page.dart';

class OptionsButton extends StatelessWidget {
  final double fem;

  const OptionsButton({
    required this.fem,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Positioned(
      left: 307 * fem,
      top: 0 * fem,
      child: TextButton(
        onPressed: () {
          Navigator.of(context).pushReplacementNamed('/options');
        },
        style: TextButton.styleFrom(padding: EdgeInsets.zero),
        child: Container(
          padding: EdgeInsets.fromLTRB(9.62 * fem, 18.75 * fem, 9.62 * fem, 18.75 * fem),
          width: 76.93 * fem,
          height: 75 * fem,
          decoration: BoxDecoration(
            image: DecorationImage(
              fit: BoxFit.cover,
              image: AssetImage(
                'assets/prototype/images/vector.png',
              ),
            ),
          ),
          child: Center(
            child: SizedBox(
              width: 57.7 * fem,
              height: 37.5 * fem,
              child: Image.asset(
                'assets/prototype/images/vector-gfv.png',
                width: 57.7 * fem,
                height: 37.5 * fem,
              ),
            ),
          ),
        ),
      ),
    );
  }
}

