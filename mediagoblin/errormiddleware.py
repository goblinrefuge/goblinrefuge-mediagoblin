# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

MGOBLIN_ERROR_MESSAGE = """\
<div style="text-align:center;font-family: monospace">
  <h1>YEOWCH... that's an error!</h1>
  <pre>
.-------------------------.
|     __            _     |
|    -, \_,------,_//     |
|     <\  ,--   --.\      |
|      / (x  ) ( X )      |
|      '  '--, ,--'\      |
|     / \ -v-v-u-v /      |
|     .  '.__.--__'.\     |
|    / ',___/ / \__/'     |
|    | |   ,'\_'/, ||     |
|    \_|   | | | | ||     |
|     W',_ ||| |||_''     |
|      |  '------'|       |
|      |__|     |_|_      |
|     ,,,-'     '-,,,     |
'-------------------------'
  </pre>
  <p>Sorry, our goblins had a little too much to drink.</p>
  <p>You may want to <a href="mailto:goblinpolice@goblinrefuge.com?Subject=Goblin%20Error" target="_top">alert the Goblin Police</a> and let them know what happened.</p>
</div>"""


def mgoblin_error_middleware(app, global_conf, **kw):
    """
    MediaGoblin wrapped error middleware.

    This is really just wrapping the error middleware from Paste.
    It should take all of Paste's default options, so see:
      http://pythonpaste.org/modules/exceptions.html
    """
    # No paste?  Fail in a friendly way!
    try:
        from paste.exceptions.errormiddleware import make_error_middleware
    except ImportError:
        return app

    kw['error_message'] = MGOBLIN_ERROR_MESSAGE
    return make_error_middleware(app, global_conf, **kw)
