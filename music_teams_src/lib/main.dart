import 'package:flutter/material.dart';
import 'package:myapp/components/error.dart';
import 'package:myapp/pages/opening.dart';
import 'package:myapp/route-generator.dart';
import 'package:myapp/utils.dart';
import 'package:myapp/prototype/opening-page.dart';

// Run each of the following:
// MyApp()      for the app
// MyAppDemo()  for the demo app (figma with navigation)
// Get()        for the GET example
// Post()       for the POST example
void main() => runApp(MyApp());


class MyAppDemo extends StatelessWidget {  // MyAppDemo is running all pages from prototype folder (as a figma with navigations)
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


class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Music Teams',
      theme: ThemeData(),
      initialRoute: '/',
      onGenerateRoute: RouteGenerator.onGenerateRoute,
      //navigatorKey: GlobalKey<NavigatorState>(),
    );
  }
}


