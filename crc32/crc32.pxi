# cython: language_level=3
# Cython CRC32. Coded by Wojciech Lawren.
from crc32 cimport *

cdef class CRC32:
  # CRC32
  cpdef uint32_t crc32c(bytes s, uint32_t _crc = 0) except? 0:
    return _crc32c(_crc, s, len(s))
