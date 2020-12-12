"""
    Copyright 2020 Ext-Creators

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import sys


_ALL = {
    # This will be populated by loaded alternative converters at runtime
}

def py_allow(major: int, minor: int, micro: int) -> None:
    if sys.version_info < (major, minor, micro):
        raise RuntimeError("This extension requires Python>={0}.{1}.{2}".format(major, minor, micro))
