import 'package:flutter/material.dart';
import 'package:myapp/utils.dart';
import 'package:myapp/prototype/opening-page.dart';

// import 'package:myapp/prototype/sign-in-page.dart';
// import 'package:myapp/prototype/home-page.dart';
// import 'package:myapp/prototype/team-home-page.dart';
// import 'package:myapp/prototype/add-chords-page.dart';
// import 'package:myapp/prototype/add-song-page.dart';
// import 'package:myapp/prototype/ranking-page.dart';
// import 'package:myapp/prototype/new-team-page-pop-up.dart';
// import 'package:myapp/prototype/options-page.dart';
// import 'package:myapp/prototype/sign-up-page.dart';
// import 'package:myapp/prototype/create-a-new-team-pop-up.dart';
// import 'package:myapp/prototype/song-page.dart';
// import 'package:myapp/prototype/rename-page.dart';
// import 'package:myapp/prototype/live-team-1.dart';
// import 'package:myapp/prototype/song-demand.dart';
// import 'package:myapp/prototype/team-code-pop-up.dart';
// import 'package:myapp/prototype/add-rec-page.dart';
// import 'package:myapp/assets-components/frame-1.dart';
// import 'package:myapp/assets-components/group-22.dart';
// import 'package:myapp/assets-components/frame-2.dart';
// import 'package:myapp/assets-components/iphone-14-15-pro-max-1.dart';
// import 'package:myapp/assets-components/fra.dart';
// import 'package:myapp/assets-components/icon-mic.dart';
// import 'package:myapp/assets-components/buttons.dart';
// import 'package:myapp/assets-components/styles.dart';
// import 'package:myapp/assets-components/input-fields.dart';
// import 'package:myapp/wireframes/opening-page.dart';
// import 'package:myapp/wireframes/sign-in-page.dart';
// import 'package:myapp/wireframes/home-page.dart';
// import 'package:myapp/wireframes/team-home-page.dart';
// import 'package:myapp/wireframes/add-chords-page.dart';
// import 'package:myapp/wireframes/add-song-page.dart';
// import 'package:myapp/wireframes/ranking-page.dart';
// import 'package:myapp/wireframes/new-team-page-pop-up.dart';
// import 'package:myapp/wireframes/options-page.dart';
// import 'package:myapp/wireframes/sign-up-page.dart';
// import 'package:myapp/wireframes/create-a-new-team-pop-up.dart';
// import 'package:myapp/wireframes/song-page.dart';
// import 'package:myapp/wireframes/rename-page.dart';
// import 'package:myapp/wireframes/live-team-1.dart';
// import 'package:myapp/wireframes/song-demand.dart';
// import 'package:myapp/wireframes/team-code-pop-up.dart';
// import 'package:myapp/wireframes/add-rec-page.dart';
// import 'package:myapp/wireframes/group-26.dart';
// import 'package:myapp/wireframes/transport.dart';
// import 'package:myapp/final-ui/opening-page.dart';
// import 'package:myapp/final-ui/sign-in-page.dart';
// import 'package:myapp/final-ui/home-page.dart';
// import 'package:myapp/final-ui/team-home-page.dart';
// import 'package:myapp/final-ui/add-chords-page.dart';
// import 'package:myapp/final-ui/add-song-page.dart';
// import 'package:myapp/final-ui/ranking-page.dart';
// import 'package:myapp/final-ui/new-team-page-pop-up.dart';
// import 'package:myapp/final-ui/options-page.dart';
// import 'package:myapp/final-ui/sign-up-page.dart';
// import 'package:myapp/final-ui/create-a-new-team-pop-up.dart';
// import 'package:myapp/final-ui/song-page.dart';
// import 'package:myapp/final-ui/rename-page.dart';
// import 'package:myapp/final-ui/live-team-1.dart';
// import 'package:myapp/final-ui/song-demand.dart';
// import 'package:myapp/final-ui/team-code-pop-up.dart';
// import 'package:myapp/final-ui/add-rec-page.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
	@override
	Widget build(BuildContext context) {
	return MaterialApp(
		title: 'Flutter',
		debugShowCheckedModeBanner: false,
		scrollBehavior: MyCustomScrollBehavior(),
		theme: ThemeData(
		primarySwatch: Colors.blue,
		),
		home: Scaffold(
		body: SingleChildScrollView(
			child: Opening(),
		),
		),
	);
	}
}
