# Copyright 2022 iwatake2222
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Main function
"""

import argparse
import my_package.my_func


def main():
    """main function"""
    parser = argparse.ArgumentParser(description='Calculator')
    parser.add_argument('--lval', type=str, default='1', help='Left value')
    parser.add_argument('--rval', type=str, default='1', help='Right value')
    args = parser.parse_args()

    lval = int(args.lval)
    rval = int(args.rval)
    ret = my_package.my_func.add(lval, rval)
    print(ret)


if __name__ == '__main__':
    main()
