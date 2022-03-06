#!/usr/bin/env python
import os
import psutil

class MemoryChecker():
    """
    Callable class to get current memory use of program.

    Instances of this class may be called, at which time
    they will return current memory use.
    """

    def __init__(self):
        self.process = psutil.Process(os.getpid())  # <1>

    def __call__(self):
        return self.process.memory_info().rss  # <2>
