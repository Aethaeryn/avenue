URLS
----

* Forum URL Structure:

  * URL structure: example.com/f/forum_name/

    * The default forum_name is main.

* Basic URL possibilities:

  * example.com/f/forum_name/tag/tag_name

    * Shows all content in a forum called forum_name with the tag
      called tag_name (e.g. economics, news).

    * Multiple tags can be shown if in between each tag is a +

  * example.com/f/forum_name/submission_id

    * The full path to the submission of the ID submission_id
      (e.g. ac134ff1). Shows the submission at the top, followed by
      the comments.

  * example.com/submission_id

    * Redirects to the full path to the submission id.

  * example.com/tag/tag_name

    * Shows all content on all forums with the tag called tag_name.

    * Note that this is a meta-category since each tag is run
      independently in each forum, so no one can actually moderate
      this. People who moderate particular tags do so under a
      particular forum, so content here can be under the supervision
      of multiple different moderator sets. Thus, it needs to be
      clear which forum it is under.

  * example.com/f/forum_name/wiki/Article_Name

    * Wikis use their human-friendly article name instead of a
      submission id and their article name (i.e. title) must be unique
      to the forum. Note that the submission ID redirect (i.e. the
      path example.com/submission_id) does not work since the article
      name could be confused with a section of the website.

  * example.com/wiki/Article_Name

    * This either redirects to the Article Name in the appropriate
      forum, or if there are multiple articles with the same name in
      different forums it is a disambiguation page that lists them
      all. This allows for multiple articles on the same thing from
      different perspectives based on the nature of the forum.

  * example.com/game_name/f/forum_name

    * A second hierarchy of forums can exist under the path of a
      particular game_name, of content specific to that game. /f/main
      is the official forum for the game and other forums can exist
      that are run by specific subgroups of the game.

    * This second hierarchy repeats the above hierarchy except it does
      *not* include duplicates of the paths not specific to a forum
      (see below), i.e. mail and user profiles. If the game has its
      own user profile system that is linked to the website profile
      system, it is handled independently of the forum profile system
      (i.e. coded via the game logic).

* Global URL paths not specific to a forum:

  * example.com/mail

    * Shows the user's private messages, and eventually email.

  * example.com/mail/mail_id

    * A particular link to a particular piece of mail.

  * example.com/mail/tag/tag_name

    * All mail of a particular tag, which is assigned by the user for
      his or her own personal organizational purposes.

  * example.com/user/user_id

    * Redirects to example.com/user/username

  * example.com/user/username

    * Is the profile for a particular user (see above, under the
      section Special Content Types).
