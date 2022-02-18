#!/usr/bin/env python
import _rdrand as rd  # https://github.com/ZiLOG-Z180/python-TRNG

import _crc32

RDS = 1
ITR = 100

MSG = b"The quick brown fox jumps over the lazy dog."
MSG_1k = rd.rand_bytes(1_000)
MSG_10k = rd.rand_bytes(10_000)


def test_crc32c_c():
    _crc = 419469235
    for _ in range(ITR):
        assert _crc32.crc32c(MSG) == _crc


def test_crc32c_r():
    for _ in range(ITR):
        msg = rd.rand_bytes(rd.rand16())
        _crc = _crc32.crc32c(msg)
        assert _crc32.crc32c(msg) == _crc


def test_crc32c_d():
    for _ in range(ITR):
        msg1 = rd.rand_bytes(rd.rand16())
        msg2 = rd.rand_bytes(rd.rand16())
        _crc1 = _crc32.crc32c(msg1)
        assert _crc32.crc32c(msg2, _crc1) == _crc32.crc32c(msg1 + msg2)


def test_crc32c_dex():
    for _ in range(ITR):
        msg1 = rd.rand_bytes(rd.rand16())
        msg2 = rd.rand_bytes(rd.rand16())
        msg3 = rd.rand_bytes(rd.rand16())
        _crc1 = _crc32.crc32c(msg1)
        _crc2 = _crc32.crc32c(msg2, _crc1)
        assert _crc2 == _crc32.crc32c(msg1 + msg2)
        assert _crc32.crc32c(msg3, _crc2) == _crc32.crc32c(msg1 + msg2 + msg3)


def test_crc32_crc32c(benchmark):
    benchmark.pedantic(_crc32.crc32c, args=(MSG,), rounds=RDS, iterations=ITR)


def test_crc32_crc32c_1k(benchmark):
    benchmark.pedantic(_crc32.crc32c, args=(MSG_1k,), rounds=RDS, iterations=ITR)


def test_crc32_crc32c_10k(benchmark):
    benchmark.pedantic(_crc32.crc32c, args=(MSG_10k,), rounds=RDS, iterations=ITR)
