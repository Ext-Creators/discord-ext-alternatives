import collections


_VersionInfo = collections.namedtuple("_VersionInfo", "year month day release serial")

version_info = _VersionInfo(2021, 4, 13, "final", 0)
version = "2021.04.13"
