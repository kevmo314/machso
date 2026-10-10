#!/usr/bin/env python3
"""Export a native dylib interface for portable ELF dependency discovery."""
import argparse
import json
from aot.macho import native_interface


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('library')
    parser.add_argument('output')
    parser.add_argument('--soname', required=True)
    args = parser.parse_args()
    with open(args.output, 'w') as output:
        json.dump(native_interface(args.library, args.soname), output, indent=2)
        output.write('\n')


if __name__ == '__main__':
    main()
