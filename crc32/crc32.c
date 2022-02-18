#include "crc32.h"

uint32_t _crc32c(const uint32_t _crc, const uint8_t *s, const uint64_t N)
{
    register uint64_t crc = (uint64_t)~_crc;
    register uint64_t nq = N / 8;
    register uint8_t nr = N % 8;

    if (nq)
        asm volatile("movq %2, %%rcx\n\t"
                     "xorl %%r11d, %%r11d\n\t"
                     "1:\n\t"
                     "crc32q (%1, %%r11, 8), %0\n\t"
                     "incq %%r11\n\t"
                     "loop 1b"
                     : "+r"(crc)
                     : "r"(s), "r"(nq)
                     : "rcx", "r11");

    if (nr)
        asm volatile("movzbq %2, %%rcx\n\t"
                     "xorl %%r11d, %%r11d\n\t"
                     "1:\n\t"
                     "crc32b (%1, %%r11), %0\n\t"
                     "incb %%r11b\n\t"
                     "loop 1b"
                     : "+r"(crc)
                     : "r"(s + nq * 8), "r"(nr)
                     : "rcx", "r11");

    return ~(uint32_t)crc;
}
