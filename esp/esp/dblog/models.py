
__author__    = "MIT ESP"
__date__      = "$DATE$"
__rev__       = "$REV$"
__license__   = "GPL v.2"
__copyright__ = """
This file is part of the ESP Web Site
Copyright (c) 2007 MIT ESP

The ESP Web Site is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Contact Us:
ESP Web Group
MIT Educational Studies Program,
84 Massachusetts Ave W20-467, Cambridge, MA 02139
Phone: 617-253-4882
Email: nu-websupport@lists.learningu.org
"""
from django.db import models
from traceback import format_stack
from esp.settings import LOG_FILE
from django.shortcuts import render_to_response # aseering 2-14-2007: This can't be Axiak's fancy esp.web.data version because otherwise we get an import loop.  Possibly we should fix that someday.

# Create your models here.


class Log(models.Model):

    # Store/log errors
    text = models.TextField(blank=True)
    extra = models.TextField(blank=True)
    stack_trace = models.TextField(blank=True)
    current_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):

        return str(self.current_date) + '\n\nTEXT: ' + \
               self.text              + '\n\nEXTRA:' + \
               self.extra             + '\n\nSTACKTRACE: ' + \
               self.stack_trace

    def save(self, *args, **kwargs):
        if LOG_FILE != None:
            errfile = open(LOG_FILE, 'a')
            errfile.write( str(self) )
            errfile.close()

        super(Log, self).save(*args, **kwargs)

    class Admin:
        pass
        
        

def error(err_txt, extra = '', stack_trace = None, log = True):
    """  Log an error, with the specified text
    stack_trace = None causes the stack trace to be autogenerated """
    
    if log:
        # Log an error to the database
        # Let programmers be lame.  Auto stack trace.
        if stack_trace == None:
            stack_trace = "\n".join(format_stack())

        # Save the error as a database record
        err = Log()
        err.text = err_txt
        err.stack_trace = stack_trace


        try:
            err.extra = str(extra)
        except:
            err.extra = ''
            
        err.save()

    return render_to_response('error.html', { 'error': err_txt } )

