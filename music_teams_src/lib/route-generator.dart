import 'package:flutter/material.dart';
import 'package:myapp/components/disclaimer.dart';
import 'package:myapp/components/error.dart';
import 'package:myapp/pages/add-recording.dart';
import 'package:myapp/pages/add-song.dart';
import 'package:myapp/pages/live.dart';
import 'package:myapp/pages/opening.dart';
import 'package:myapp/pages/options.dart';
import 'package:myapp/pages/song.dart';
import 'package:myapp/pages/team-home.dart';

class RouteGenerator {
  static Route<dynamic> onGenerateRoute(RouteSettings settings) {
    if (settings.name == null) {
      return MaterialPageRoute(
        builder: (_) => CustomError(
          errorText: 'The route provided by the Navigator does not exist. Check all the available routes.',
          errorTitle: 'Undefined Route',
          navigateToRoute: '/',
        ),
      );
    }

    final List<String> pathSegments = settings.name!.split('/');
    //final String id = pathSegments[0];
    final String routeName = pathSegments[1]; // Get the first segment after the leading '/'

    switch (routeName) {
      case '':
        return MaterialPageRoute(builder: (_) => OpeningPage());

      case 'team-home':
        return MaterialPageRoute(builder: (_) => TeamHomePage());

      case 'options':
        return MaterialPageRoute(builder: (_) => OptionsPage());

      case 'live':
        return MaterialPageRoute(builder: (_) => LivePage());

      case 'song-demand':
        return MaterialPageRoute(builder: (_) => TeamHomePage(mode: 'SongDemand'));

      case 'add-song':
        return MaterialPageRoute(builder: (_) => AddSongPage());

      case 'add-recording':
        final String id = pathSegments[2];
        final String title = pathSegments[3];
        return MaterialPageRoute(
          builder: (_) => AddRecordingPage(songId: int.tryParse(id) ?? -1, title: title),
        );

      case 'song':
        final String id = pathSegments[2];
        return MaterialPageRoute(
          builder: (_) => SongPage(songId: int.tryParse(id) ?? -1),
        );

      case 'disclaimer':
        return MaterialPageRoute(builder: (_) => Disclaimer());
    }

    return MaterialPageRoute(
      builder: (_) => CustomError(
        errorText: 'The route provided by the Navigator does not exist. Check all the available routes.',
        errorTitle: 'Undefined Route',
        navigateToRoute: '/',
      ),
    );
  }
}
