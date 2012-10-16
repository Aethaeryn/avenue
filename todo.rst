* Posts

  * author(s)

  * content

  * karma

  * parent and children

  * revisions

  * tags

* Content

  * pic

    * Links to externally hosted pictures (and eventually uploaded
      pictures).

  * video

    * Links to externally hosted videos.

  * post

    * Threads where the first post is a post rather than a link or
      special content type.

  * micro

    * Threads where there is no first post, only a title.

  * link

    * Links to an external site that is not a picture or video link.

  * wiki

    * Collaborative editing of the first post, with public history
      available on that post.

    * Ability to include content from other sections in some sort of
      quote-like system.

    * URL contains the title, which must be unique, rather than a
      hexadecimal number.

    * Comments 'hidden' at first and must be clicked to be shown???

* Special Content Types

  * data

    * Machine-generated, human-readable content.

  * mail

    * Can handle private messaging and (eventually) email.

    * Private to the receiver instead of public to all.

  * profile

    * User profile, with information for the user, both info publicly
      visible and private to only user (and/or admins?).

    * Allow for customization of the material presented, e.g. to allow
      for "blogging" with content shown under profile/foo/blog that
      doubles as a post-type content visible elsewhere?

    * Show post/submission history?

* Forums

  * Independently run sections of the site with global moderators and
    moderators for various content or tag types.

  * URL structure: example.com/f/forum_name/

    * The default forum_name is main.

* Additional URL possibilities:

  * example.com/f/forum_name/tag/tag_name

    * Shows all content in a forum called forum_name with the tag
      called tag_name (e.g. economics, news).

  * example.com/f/forum_name/content_type

    * Shows all content in a forum called forum_name of the content of
      the type content_type (e.g. pic, link).

  * example.com/f/forum_name/content_type/tag/tag_name

    * Shows all content in a forum called forum_name of the content of
      the type content_type with the tag called tag_name.

  * example.com/f/forum_name/content_type/submission_id

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

  * example.com/content_type

    * Shows all content on all forums of a particular content type.

    * This is also a meta-category (see above).

  * example.com/content_type/tag/tag_name

    * Shows all content on all forums of a particular content type and
      tag.

    * This is also a meta-category (see above).

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

* Permissions and Accounts

* Tagging

  * public (global, multi-tag)

  * private (visible only you, such as tagging users or posts with a
    certain label)

  * Tags allow 'inheritance' from parent tags, so if tagged as a child
    tag it is automatically tagged as its parent tag(s) as well.

* Forum Types

  * public

  * open only to members

* Repost Interface

  * After three months, the ability is given to repost something
    already posted (if not wiki). The first/top reply in this case is
    a special meta post that links to previous discussions.
