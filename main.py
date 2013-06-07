#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
import jinja2
import webapp2
import wsgiref.handlers
from google.appengine.ext import ndb

# app related imports
from ytm_core import conf
from ytm_core.youtube_api import get_video_info

# jinja env variable setup
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class HomePageHandler(webapp2.RequestHandler):

    page = 'templates/index.html'

    def get(self):
        # easy: loads with default video
        template = JINJA_ENVIRONMENT.get_template(self.page)
        self.response.write(template.render(get_video_info()))


def main():
    application = webapp2.WSGIApplication([
        ('/', HomePageHandler),
    ], debug=conf.DEBUG)

    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
