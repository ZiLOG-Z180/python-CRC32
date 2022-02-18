# cython: language_level=3
from libc.stdint cimport *

cdef extern from "crc32.h" nogil:
  uint32_t _crc32c(const uint32_t _crc, const uint8_t *s, const uint64_t N)
