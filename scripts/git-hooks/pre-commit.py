#!/usr/bin/env python3
import os
import re
import sys
import subprocess


def bump_version():
    with open('hackedit_python/__init__.py') as f:
        lines = f.read().splitlines()
        new_lines = f.newlines
    for i, l in enumerate(lines):
        if '__version__' in l:
            string = l.split('=')[1].strip().replace('"', '').replace("'", '')
            for prefix in ['dev']:
                try:
                    suffix = re.findall(r'%s\d*' % prefix, string)[0]
                except IndexError:
                    suffix = None
                    version = None
                else:
                    version = int(suffix.replace(prefix, ''))
                    break
            if None in [suffix, version]:
                return  # stable version, nothing to do
            version += 1
            new_suffix = '%s%d' % (prefix, version)
            new_string = string.replace(suffix, new_suffix)
            lines[i] = "__version__ = '%s'" % new_string
            print(lines[i])
            break

    with open('hackedit_python/__init__.py', 'w') as f:
        f.write('\n'.join(lines))
        f.write('\n')

    with open('.commit', 'w') as f:
        pass

bump_version()
