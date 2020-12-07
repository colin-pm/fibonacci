//
// Created by cpmcalli on 12/4/2020.
//

#include "gtest/gtest.h"
#include "fibonacci.h"

TEST(FibonacciTests, BaseCaseZero)
{
    EXPECT_EQ(fibonacci(0), 0);
}

TEST(FibonacciTests, BaseCaseOne)
{
    EXPECT_EQ(fibonacci(1), 1);
}

TEST(FibonacciTests, LoopTest)
{
    int valOne = 0;
    int valTwo = 1;
    int newVal;
    for(int i = 2; i < 10; i++)
    {
        newVal = valOne + valTwo;
        valOne = valTwo;
        valTwo = newVal;
        EXPECT_EQ(fibonacci(i), newVal);
    }
}
