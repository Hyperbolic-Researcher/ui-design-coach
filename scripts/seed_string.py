"""Generate random alphanumeric seed strings for UI design divergence.

The seed string is injected into a design prompt as a hidden source of
creative direction. LLMs cannot generate true randomness themselves, so
the randomness must come from outside the model.
"""

import argparse
import secrets
import string
import sys

ALPHABET = string.ascii_letters + string.digits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="生成随机字母数字种子串，用作设计提示词的隐藏创意种子"
    )
    parser.add_argument("--count", type=int, default=1, help="生成数量，1-32，默认 1")
    parser.add_argument("--length", type=int, default=64, help="每条长度，8-512，默认 64")
    args = parser.parse_args()

    if not 1 <= args.count <= 32:
        print("error: --count 必须在 1-32 之间", file=sys.stderr)
        return 2
    if not 8 <= args.length <= 512:
        print("error: --length 必须在 8-512 之间", file=sys.stderr)
        return 2

    for _ in range(args.count):
        print("".join(secrets.choice(ALPHABET) for _ in range(args.length)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
