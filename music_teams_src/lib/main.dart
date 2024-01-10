import 'package:flutter/material.dart';
import 'package:myapp/pages/team-home.dart';
import 'package:myapp/utils.dart';
import 'package:myapp/prototype/opening-page.dart';


// Run each of the following:
// MyApp()      for the app
// MyAppDemo()  for the demo app (figma with navigation)
// Get()        for the GET example
// Post()       for the POST example
void main() => runApp(const MyApp());


class MyAppDemo extends StatelessWidget {
  const MyAppDemo({super.key});
  // MyAppDemo is running all pages from prototype folder (as a figma with navigations)
	@override
	Widget build(BuildContext context) {
	return MaterialApp(
		title: 'Flutter',
		debugShowCheckedModeBanner: false,
		scrollBehavior: MyCustomScrollBehavior(),
		theme: ThemeData(
		primarySwatch: Colors.blue,
		),
		home: const Scaffold(
		body: SingleChildScrollView(
			child: Opening(),
		),
		),
	);
	}
}


class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: TeamHomePage(),                 // here change the page you want to see first
    );
  }
}