#!/usr/bin/env python

import sys
import os

import requests

url = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'  # <1>
saved_pdf_file = 'nasa_iss.pdf'  # <2>

response = requests.get(url)  # <3>
if response.status_code == requests.codes.OK:  # <4>
    if response.headers.get('content-type') == 'application/pdf':
        with open(saved_pdf_file, 'wb') as pdf_in:  # <5>
            pdf_in.write(response.content)  # <6>

        if sys.platform == 'win32':  # <7>
            cmd = saved_pdf_file
        elif sys.platform == 'darwin':
            cmd = 'open ' + saved_pdf_file
        else:
            cmd = 'acroread ' + saved_pdf_file

        os.system(cmd)  # <8>
