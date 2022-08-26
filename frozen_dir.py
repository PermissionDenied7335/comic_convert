#!/usr/bin/env python3
import os
import sys

if hasattr(sys, "frozen"):
    WORKSPACE = os.path.dirname(sys.executable)
else:
    WORKSPACE = os.path.dirname(__file__)
