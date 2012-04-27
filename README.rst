======
Avenue
======

Avenue is a 'good enough' generalist program to handle all of my
website needs in one application. It does what I need it to and
nothing more, and I know what all of the lines of code do. Since I
designed it for my website, it's not perfect. If you want perfect, you
can always fork and improve it.

It will eventually handle support for all sorts of 'social' uses that
are traditionally handled by different web applications. For instance,
the forum/subforum metaphor is abandoned altogether. Tagging is simply
turned into restricted (only one tag per post), and tags are displayed
in a hierarchical manner. Then the forum rendering mode makes it look
like a forum when it is really just Avenue.

Similarly, the wiki problem is nearly identical to the forum problem
when approached through Avenue. Permissions are set to allow multiple
people to edit a wiki page, and the theme is set so that the comments
are on a separate page from the wiki content itself. Tags are then
handled in a way that imitates MediaWiki categories instead of a way
that imitates traditional web forums. All edit revisions will be saved
and almost every content type will allow revisions, so wikis will only
be special only in that they're designed so more than the creator and
moderators can edit them.

The only thing that's handled somewhat specially is the webmail, since
it needs to interface with the established email standards. For
instance, the only tagging possible will be tagging on the client
side, so categorization will be based on what the recipient chooses
rather than what the sender chooses. Still, the problem can be reduced
to storing, processing, and rendering plaintext so a lot of the
resources should still be shared with the rest of Avenue.

You can discuss things in a wiki or a blog, you can blog in a web
forum, and so on, but each of those are monolithic silos of content
optimized for one particular task. I could use one of those and get a
sub par experience, or I could use many large applications that have
many features I simply do not need. None of this is preferable.

Plus, each of these features will be able to fully integrate with my
games in a clean manner. I don't need to patch someone else's code,
and I know exactly what to expect. I don't run all sorts of web apps,
I just run Avenue and configure it to import my games and use the
appropriate modules of Avenue.

How is this possible? Well, object oriented programming makes it
possible. Simply separate the content itself from the rendering of the
content, and share as much resources as possible between similar
tasks. Ultimately, it's all just text.
