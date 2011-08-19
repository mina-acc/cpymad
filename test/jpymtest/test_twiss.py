#-------------------------------------------------------------------------------
# This file is part of PyMad.
# 
# Copyright (c) 2011, CERN. All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# 	http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------
'''
Created on Nov 17, 2010

@author: kaifox
'''
import unittest

from utils import PyMadTestCase

class Test(unittest.TestCase):

    def testTwiss(self):
        madxvarnames = ["s", "name", "betx", "bety"]
        result, params = PyMadTestCase.pms.am.twiss(madxvarnames)
        
        print result

        self.assertTrue(not result["s"] == None, "s-values must be returned")
        try:
            self.assertTrue(result["x"] == None, "x-values were not requested")
        except KeyError:
            pass
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTwiss']
    unittest.main()