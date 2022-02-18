#!/usr/bin/env python
import _crc32

MSG = b"The quick brown fox jumps over the lazy dog."
MSG_S = MSG.decode('ascii')


def test_crc32c_z():
    _c = _crc32.crc32c(b"")
    assert not _c
    _cc = 17
    assert _crc32.crc32c(b"", _cc) == _cc


def test_crc32c_fail_type():
    err = 0
    assert not err
    try:
        _c = _crc32.crc32c(MSG_S)
    except TypeError:
        err += 1
    assert err


def test_crc32c_fail_overflow():
    err = 0
    assert not err
    try:
        _c = _crc32.crc32c(MSG, 2**32)
    except OverflowError:
        err += 1
    assert err
