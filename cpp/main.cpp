/* Copyright 2022 iwatake2222

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
/*** Include ***/
/* for general */
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <memory>
#include <vector>
#include <string>

#include "my_class.h"

/*** Macro ***/

/*** Setting ***/

/*** Global variable ***/

/*** Function ***/
int main(int argc, char* argv[])
{
    int32_t a = 0;
    int32_t b = 0;
    std::cout << ">";
    std::cin >> a >> b;
    MyClass my_class;
    int32_t ans = my_class.Add(a, b);
    std::cout << std::to_string(a) + " + " + std::to_string(b) + " = " + std::to_string(ans) << std::endl;

    return 0;
}
