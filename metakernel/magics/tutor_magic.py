"""
==========
tutormagic
==========

Magics to display pythontutor.com in the notebook.
"""

# Based on Kiko Correoso's IPython magic:
# https://github.com/kikocorreoso/tutormagic
# and Doug Blank's
# http://jupyter.cs.brynmawr.edu/hub/dblank/public/Examples/Online%20Python%20Tutor.ipynb
#-----------------------------------------------------------------------------
# Copyright (C) 2015 Kiko Correoso and the pythontutor.com developers
#
# Distributed under the terms of the MIT License. The full license is in
# the file LICENSE, distributed as part of this software.
#
# Contributors:
#   kikocorreoso
#-----------------------------------------------------------------------------

from metakernel import Magic, option
from IPython.display import display, IFrame
import sys
if sys.version_info.major == 2 and sys.version_info.minor == 7:
    from urllib import quote
elif sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from urllib.parse import quote
    
class TutorMagic(Magic):

    @option(
        '-l', '--language', action='store', nargs = 1,
        help=("Possible languages to be displayed within the iframe. " +
              "Possible values are: python2, python3, java, javascript")
    )
    def cell_tutor(self, language="python3"):
        """
        %%tutor [--language=LANGUAGE] - show cell with 
        Online Python Tutor.

        Examples:
           %%tutor -l python3
           a = 1
           b = 1
           a + b

           [You will see an iframe with the pythontutor.com page 
           including the code above.]

           %%tutor --language=java
           
           public class Test {
               public Test() {
               }
               public static void main(String[] args) {
                   int x = 1;
                   System.out.println("Hi");
               }
           }
        """
        if language not in ['python2', 'python3', 'java', 'javascript']:
            raise ValueError("{} not supported. Only the following options are allowed: "
                             "'python2', 'python3', 'java', 'javascript'".format(language))
        
        url = "http://pythontutor.com/iframe-embed.html#code="
        url += quote(self.code)
        url += "&origin=opt-frontend.js&cumulative=false&heapPrimitives=false"
        url += "&textReferences=false&"
        if language == "python3":
            url += "py=3&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        if language == "python2":
            url += "py=2&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        if language == "java":
            url += "py=java&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        if language == "javascript":
            url += "py=js&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        
        # Display the results in the output area
        self.kernel.Display(IFrame(url, height=350, width="100%"))
        self.evaluate = False

def register_magics(kernel):
    kernel.register_magics(TutorMagic)
