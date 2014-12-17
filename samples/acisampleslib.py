# Copyright (c) 2014 Cisco Systems
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
"""
Function used by samples to get the APIC login credentials from the command
line (--help gives usage).  If login credentials are not provided on the
command line, the bash environment variables are taken from the file ~/.profile.
"""
import argparse
import os

DEFAULT_URL = os.environ['APIC_URL'] if 'APIC_URL' in os.environ.keys() else ''
DEFAULT_LOGIN = os.environ['APIC_LOGIN'] if 'APIC_LOGIN' in os.environ.keys() else ''
DEFAULT_PASSWORD = os.environ['APIC_PASSWORD'] if 'APIC_PASSWORD' in os.environ.keys() else ''


def get_login_info(description='No description'):

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-u', '--url', default=DEFAULT_URL, help='APIC IP address.')
    parser.add_argument('-l', '--login', default=DEFAULT_LOGIN, help='APIC login ID.')
    parser.add_argument('-p', '--password', default=DEFAULT_PASSWORD, help='APIC login password.')

    return parser

