<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>models.py : /home/nbadb/nba/models.py : Editor : nbadb : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="models.py : /home/nbadb/nba/models.py : Editor : nbadb : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />

        <!-- Le styles -->
        <link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">
        <link href="/static/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
        <link href="/static/anywhere/styles/bootstrap_base.css" rel="stylesheet">
        
    <link rel="stylesheet" href="/static/anywhere/styles/editor.css" type="text/css" media="screen" charset="utf-8" />
    

        <link rel="stylesheet" href="/static/jquery/jquery-ui-1.8.11.custom.css" type="text/css" media="screen" charset="utf-8" />
        
        <style type="text/css">
            body {
                height: auto;
            }
        </style>
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
        <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->

        <!-- Le fav and touch icons -->
        <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
        <link rel="apple-touch-icon" sizes="72x72" href="images/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="114x114" href="images/apple-touch-icon-114x114.png">

        <script type="text/javascript" src="/static/jquery/jquery-1.7.1.min.js"></script>

    </head>

     <body>
        
    <div class="navbar navbar-fixed-top">
        <div class="navbar-inner">
            <div id="id_internal_nav_bar_container" class="container">
                <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                </a>
                <a class="brand" href="/"><img id="id_logo" src="/static/anywhere/images/logo-234x35.png" height="35" title="PythonAnywhere logo" alt="PythonAnywhere logo" /></a>
                <div class="nav-collapse">
                    <ul id="id_header_links" class="nav">
                        <li><a id="id_feedback_link" class='feedback_link' href="">Send feedback</a></li>
                        <li><a id="id_forums_link" href="/forums/">Forums</a></li>
                        <li><a href="/wiki/" id="id_help_link">Help</a></li>
                        <li><a href="http://blog.pythonanywhere.com/" id="id_blog_link">Blog</a></li>
                        
                        
                            <li><a href="/user/nbadb/" id="id_dashboard_link">Dashboard</a></li>
                            <li><a href="/user/nbadb/account/" id="id_account_link">Account</a></li>
                            <li><a href="/logout" id="id_logout_link">Log out</a></li>
                        
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <div class="top-container" id="id_dummy"></div>

    



        
    


        

<div>

    <div id="id_editor_toolbar">

      <span id="id_breadcrumbs_div">
            
                <a class="breadcrumbs_link" href="/user/nbadb/files/">/</a> &gt;
            
                <a class="breadcrumbs_link" href="/user/nbadb/files/home">home</a> &gt;
            
                <a class="breadcrumbs_link" href="/user/nbadb/files/home/nbadb">nbadb</a> &gt;
            
                <a class="breadcrumbs_link" href="/user/nbadb/files/home/nbadb/nba">nba</a> &gt;
            
        <span id="id_file_name">models.py</span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden">*</span>
        </span>
      </span>
      <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
      <div id="id_editor_buttons_right" class="form-inline">

          
            <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts</a></span>
            <select id="id_keybinding_mode_select" class="input-small">
                <option value="normal">Normal</option>
                <option value="vim">Vim</option>
            </select>
          
          <button class="btn" id="id_save">Save</button>
          <span id="id_save_error" class="error_message pa_hidden">There was an error saving</span>
          
              <button class="btn" id="id_run_button">Save &amp; Run</button>
          

          
          
            <form class="reload_web_app" style="display: inline" method="POST" action="/user/nbadb/webapps/nbadb.pythonanywhere.com/reload">
                <button class="btn" type="submit">
                    <img style="height: 16px; position: relative; bottom: -3px;" src="/static/glyphicons/glyphicons_081_refresh.png">
                    <b>Reload nbadb.pythonanywhere.com</b>
                </button>
                <img style="display: none;" class="spinner" src="/static/anywhere/images/spinner-small.gif" />
                <span style="display: none;" class="error_message">
                    Sorry, there was a problem.  Please try again in a minute, and
                    <a href="" class="feedback_link">send us feedback</a> if it keeps happening.
                </span>
            </form>
          
          

        </div>
        <div class="clear"></div>
    </div>

    
          <div id="id_editor">from django.db import models


# Models for the NBA app

class Team(models.Model) :
    &quot;&quot;&quot;
    Contains information for a Team that is current and will not change
    Each Team has multiple TeamYear&#39;s (One-To-Many)
    &quot;&quot;&quot;
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=30, unique=True)
    coach = models.CharField(max_length=30, unique=True)
    gm = models.CharField(max_length=30, unique=True)
    owner = models.CharField(max_length=30)
    twitter = models.URLField(unique=True)
    logo = models.URLField(unique=True)

    def __unicode__(self) :
        return self.name

    def __str__(self) :
        return &quot;name: &quot; + self.name + &quot;\n&quot; \
               &quot;location: &quot; + self.location + &quot;\n&quot; \
               &quot;coach: &quot; + self.coach + &quot;\n&quot; \
               &quot;gm: &quot; + self.gm + &quot;\n&quot; \
               &quot;owner: &quot; + self.owner + &quot;\n&quot; \
               &quot;twitter: &quot; + str(self.twitter) + &quot;\n&quot; \
               &quot;logo: &quot; + str(self.logo) + &quot;\n&quot;

    class Meta:
        app_label = &#39;nba&#39;

class Player(models.Model) :
    &quot;&quot;&quot;
    Contains information about a Player that is current and will not change
    Each Player has multiple PlayerYear&#39;s (One-To-Many)
    &quot;&quot;&quot;
    name = models.CharField(max_length=30, unique=True)
    position = models.CharField(max_length=2)
    education = models.CharField(max_length=20)
    years_exp = models.IntegerField(default=0)
    twitter = models.URLField(unique=True)
    photo = models.URLField(unique=True)

    def __unicode__(self) :
        return self.name

    def __str__(self) :
        return &quot;name: &quot; + self.name + &quot;\n&quot; \
               &quot;position: &quot; + self.position + &quot;\n&quot; \
               &quot;education: &quot; + self.education + &quot;\n&quot; \
               &quot;years of experience: &quot; + self.years_exp + &quot;\n&quot; \
               &quot;twitter: &quot; + str(self.twitter) + &quot;\n&quot; \
               &quot;photo: &quot; + str(self.photo) + &quot;\n&quot;

    class Meta:
        app_label = &#39;nba&#39;

class Year(models.Model) :
    &quot;&quot;&quot;
    Contains information about a certain Year
    Each Year has multiple PlayerYear&#39;s and TeamYear&#39;s (One-To-Many)
    &quot;&quot;&quot;
    year = models.CharField(max_length=4, unique=True)
    all_nba = models.ManyToManyField(Player)
    all_def = models.ManyToManyField(Player)
    finals_mvp = models.ForeignKey(Player)
    champion = models.ForeignKey(Team)
    finals_logo = models.URLField(unique=True)
    finals_recap = models.TextField()

    def __unicode__(self):
        return self.year

    class Meta:
        app_label = &#39;nba&#39;

class PlayerYear(models.Model) :
    &quot;&quot;&quot;
    Contains information/statistics about a Player during a certain Year
    &quot;&quot;&quot;
    year = models.ForeignKey(Year)
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    gp = models.IntegerField(default=0)
    gs = models.IntegerField(default=0)
    minpg = models.FloatField()
    fgperc = models.FloatField()
    ftperc = models.FloatField()
    reb = models.FloatField()
    ast = models.FloatField()
    blk = models.FloatField()
    stl = models.FloatField()
    pts = models.FloatField()
    mvp = models.BooleanField()
    finals_mvp = models.BooleanField()
    all_nba = models.BooleanField()
    all_def = models.BooleanField()

    def __unicode__(self):
        return (self.player.name, self.year.year)

    class Meta:
        app_label = &#39;nba&#39;


class TeamYear(models.Model) :
    &quot;&quot;&quot;
    Contains information/statistics about a Team during a certain Year
    &quot;&quot;&quot;
    team = models.ForeignKey(Team)
    year = models.ForeignKey(Year)
    wins = models.IntegerField()
    losses = models.IntegerField()
    playoffrecap = models.TextField()

    def __unicode__(self) :
        return (self.year.year, self.team.name)

    class Meta:
        app_label = &#39;nba&#39;



</div>
    

    <div id="id_go_to_line_dialog" class="pa_hidden">
        <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
        <div class="dialog_buttons">
            <button class="btn" id="id_go_to_line_dialog_ok_button">Go</button>
            <button class="btn" id="id_go_to_line_dialog_close_button">Close</button>
        </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
        <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
        <div class="dialog_buttons">
            <button id="id_cancel_save" class="btn">Cancel</button>
            <button id="id_force_save" class="btn btn-danger">Force Save</button>
        </div>
    </div>



        
    <div id="id_footer" class="container">

        <footer id="id_copyright_div">
            <p>
                Copyright &copy; 2014 <a href="/about/company_details/">PythonAnywhere LLP</a>
                &mdash;
                <a href="/terms/">Terms</a>
                &mdash;
                <a href="/privacy/">Privacy</a><br/>
                "Python" is a registered trademark of the Python Software Foundation.
            </p>
        </footer>

    </div>


        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" class="pa_hidden">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
</div>


        <!-- Le javascript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script type="text/javascript" src="/static/jquery/jquery-ui-1.8.11.custom.min.js"></script>
        <script src="/static/bootstrap/js/bootstrap-transition.js"></script>
        <script src="/static/bootstrap/js/bootstrap-alert.js"></script>
        <script src="/static/bootstrap/js/bootstrap-modal.js"></script>
        <script src="/static/bootstrap/js/bootstrap-dropdown.js"></script>
        <script src="/static/bootstrap/js/bootstrap-scrollspy.js"></script>
        <script src="/static/bootstrap/js/bootstrap-tab.js"></script>
        <script src="/static/bootstrap/js/bootstrap-tooltip.js"></script>
        <script src="/static/bootstrap/js/bootstrap-popover.js"></script>
        <script src="/static/bootstrap/js/bootstrap-button.js"></script>
        <script src="/static/bootstrap/js/bootstrap-collapse.js"></script>
        <script src="/static/bootstrap/js/bootstrap-carousel.js"></script>
        <script src="/static/bootstrap/js/bootstrap-typeahead.js"></script>

        <script type="text/javascript">
            var urls = {};
            var Anywhere = {};
            Anywhere.urls = {};
        </script>
        <script type="text/javascript" src="/static/anywhere/scripts/ajax_utils.js"></script>

        <script type="text/javascript" src="/static/anywhere/scripts/feedback_dialog.js"></script>
        
        <script type="text/javascript">
            $(function() {
                $.extend(
                    urls,
                    {
                        feedback: '/feedback/submit/'
                    }
                );
                
                    Anywhere.FeedbackDialog.Initialise(urls, false);
                
            });
        </script>

        <script type="text/javascript">

            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-18014859-6']);
            _gaq.push(['_trackPageview']);

            (function() {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();

        </script>

        
    <script src="/static/ace/ace.js" type="text/javascript"></script>

    <script src="/static/ace/keybinding-vim.js" type="text/javascript"></script>
    <script src="/static/ace/ext-language_tools.js" type="text/javascript"></script>
    <script src="/static/ace/ext-searchbox.js" type="text/javascript"></script>
    <script src="/static/ace/ext-keybinding_menu.js" type="text/javascript"></script>

    <script src="/static/ace/mode-asciidoc.js" type="text/javascript"></script>
    <script src="/static/ace/mode-css.js" type="text/javascript"></script>
    <script src="/static/ace/mode-html.js" type="text/javascript"></script>
    <script src="/static/ace/mode-javascript.js" type="text/javascript"></script>
    <script src="/static/ace/mode-json.js" type="text/javascript"></script>
    <script src="/static/ace/mode-python.js" type="text/javascript"></script>
    <script src="/static/ace/mode-xml.js" type="text/javascript"></script>
    <script src="/static/ace/mode-c_cpp.js" type="text/javascript"></script>
    <script src="/static/ace/mode-clojure.js" type="text/javascript"></script>
    <script src="/static/ace/mode-coffee.js" type="text/javascript"></script>
    <script src="/static/ace/mode-c_cpp.js" type="text/javascript"></script>
    <script src="/static/ace/mode-css.js" type="text/javascript"></script>
    <script src="/static/ace/mode-diff.js" type="text/javascript"></script>
    <script src="/static/ace/mode-golang.js" type="text/javascript"></script>
    <script src="/static/ace/mode-html.js" type="text/javascript"></script>
    <script src="/static/ace/mode-java.js" type="text/javascript"></script>
    <script src="/static/ace/mode-javascript.js" type="text/javascript"></script>
    <script src="/static/ace/mode-json.js" type="text/javascript"></script>
    <script src="/static/ace/mode-less.js" type="text/javascript"></script>
    <script src="/static/ace/mode-latex.js" type="text/javascript"></script>
    <script src="/static/ace/mode-lua.js" type="text/javascript"></script>
    <script src="/static/ace/mode-markdown.js" type="text/javascript"></script>
    <script src="/static/ace/mode-perl.js" type="text/javascript"></script>
    <script src="/static/ace/mode-php.js" type="text/javascript"></script>
    <script src="/static/ace/mode-python.js" type="text/javascript"></script>
    <script src="/static/ace/mode-ruby.js" type="text/javascript"></script>
    <script src="/static/ace/mode-sass.js" type="text/javascript"></script>
    <script src="/static/ace/mode-scss.js" type="text/javascript"></script>
    <script src="/static/ace/mode-sql.js" type="text/javascript"></script>
    <script src="/static/ace/mode-svg.js" type="text/javascript"></script>
    <script src="/static/ace/mode-tcl.js" type="text/javascript"></script>
    <script src="/static/ace/mode-latex.js" type="text/javascript"></script>
    <script src="/static/ace/mode-textile.js" type="text/javascript"></script>
    <script src="/static/ace/mode-xml.js" type="text/javascript"></script>
    <script src="/static/ace/mode-yaml.js" type="text/javascript"></script>

    <script src="/static/anywhere/scripts/ajax_utils.js" type="text/javascript"></script>
    <script src="/static/anywhere/scripts/editor.js" type="text/javascript"></script>
    <script src="/static/anywhere/scripts/web_app_control.js" type="text/javascript"></script>

    <script type="text/javascript">
        $(function() {
            $.extend(urls, {
                save: '/user/nbadb/files/home/nbadb/nba/models.py',
                check_hash: '/user/nbadb/files/home/nbadb/nba/models.py',
                run: '/user/nbadb/files/home/nbadb/nba/models.py' + '?run',
                update_editor_mode_preference: '/user/nbadb/account/update_editor_mode_preference',

            });
            $.extend(Anywhere.urls, urls);
            var filename = "/home/nbadb/nba/models.py";
            var hash = "c97e5b6e2686acc644deffc8a82f49c3";

            
              Anywhere.Editor.InitialiseAce(ace, urls, filename, hash);
              Anywhere.Editor.resetEditorState({pyflakes_warnings: [] });
              $("#id_keybinding_mode_select").val("normal");
              $("#id_keybinding_mode_select").trigger("change");
            

            Anywhere.WebAppControl.initialize();
        });
    </script>




    </body>
</html>
