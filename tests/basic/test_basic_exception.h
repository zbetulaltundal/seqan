// ==========================================================================
//                 SeqAn - The Library for Sequence Analysis
// ==========================================================================
// Copyright (c) 2006-2018, Knut Reinert, FU Berlin
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//     * Neither the name of Knut Reinert or the FU Berlin nor the names of
//       its contributors may be used to endorse or promote products derived
//       from this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL KNUT REINERT OR THE FU BERLIN BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
// LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
// OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
// DAMAGE.
//
// ==========================================================================
// Author: Enrico Siragusa <enrico.siragusa@fu-berlin.de>
// ==========================================================================

#ifndef SEQAN_TESTS_BASIC_TEST_BASIC_EXCEPTION_H_
#define SEQAN_TESTS_BASIC_TEST_BASIC_EXCEPTION_H_

using namespace seqan;

SEQAN_DEFINE_TEST(test_basic_exception_try_catch)
{
    SEQAN_TRY
    {
        SEQAN_THROW(Exception());
    }
    SEQAN_CATCH(Exception &)
    {
        return;
    }

    SEQAN_ASSERT_MSG(false, "Exception has not been caught!");
}

SEQAN_DEFINE_TEST(test_basic_exception_bad_alloc)
{
    SEQAN_TRY
    {
        SEQAN_THROW(BadAlloc());
    }
    SEQAN_CATCH(BadAlloc &)
    {
        return;
    }

    SEQAN_ASSERT_MSG(false, "BadAlloc Exception has not been caught!");
}

SEQAN_DEFINE_TEST(test_basic_exception_runtime_error)
{
    SEQAN_TRY
    {
        SEQAN_THROW(RuntimeError("Throwing a RuntimeError."));
    }
    SEQAN_CATCH(RuntimeError &)
    {
        return;
    }

    SEQAN_ASSERT_MSG(false, "RuntimeError Exception has not been caught!");
}

#endif  // #ifndef SEQAN_TESTS_BASIC_TEST_BASIC_EXCEPTION_H_
