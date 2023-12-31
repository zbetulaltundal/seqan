#!/usr/bin/env python
"""Execute the tests for the pair_align program.

The golden test outputs are generated by the script generate_outputs.sh.

You have to give the root paths to the source and the binaries as arguments to
the program.  These are the paths to the directory that contains the 'projects'
directory.

Usage:  run_tests.py SOURCE_ROOT_PATH BINARY_ROOT_PATH
"""
import logging
import os.path
import sys

# Automagically add util/py_lib to PYTHONPATH environment variable.
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                    '..', '..', 'util', 'py_lib'))
sys.path.insert(0, path)

import seqan.app_tests as app_tests

def main(source_base, binary_base):
    """Main entry point of the script."""

    print('Executing test for pair_align')
    print('=============================')
    print()

    ph = app_tests.TestPathHelper(
        source_base, binary_base,
        'apps/pair_align/tests')  # tests dir

    # ============================================================
    # Auto-detect the binary path.
    # ============================================================

    path_to_program = app_tests.autolocateBinary(
      binary_base, 'apps/pair_align', 'pair_align')

    # ============================================================
    # Built TestConf list.
    # ============================================================

    # Build list with TestConf objects, analoguely to how the output
    # was generated in generate_outputs.sh.
    conf_list = []

    # ============================================================
    # Run on Proteins (Balibase).
    # ============================================================

    # Run with defaults for all non-mandatory options.
    for fname in ['1aab', '1ad2', '2trx']:
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.stdout' % fname),
            args=['-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.fa' % fname)],
            to_diff=[(ph.inFile('%s_out.fa' % fname),
                      ph.outFile('%s.fa' % fname)),
                     (ph.inFile('%s.stdout' % fname),
                      ph.outFile('%s.stdout' % fname))])
        conf_list.append(conf)

    # Run with explicit alphabet.
    for fname in ['1aab', '1ad2', '2trx']:
        conf = app_tests.TestConf(
            program=path_to_program,
            args=['-a', 'protein',
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.protein.fa' % fname)],
            redir_stdout=ph.outFile('%s.protein.stdout' % fname),
            to_diff=[(ph.inFile('%s.protein_out.fa' % fname),
                      ph.outFile('%s.protein.fa' % fname)),
                     (ph.inFile('%s.protein.stdout' % fname),
                      ph.outFile('%s.protein.stdout' % fname))])
        conf_list.append(conf)

    # Run with different alignment methods.
    for fname in ['1aab', '1ad2', '2trx']:
        for m in ['nw', 'gotoh', 'sw', 'lcs']:
            conf = app_tests.TestConf(
                program=path_to_program,
                redir_stdout=ph.outFile('%s.m%s.stdout' % (fname, m)),
                args=['-m', m,
                      '-s', ph.inFile('%s.fa' % fname),
                      '-o', ph.outFile('%s.m%s.fa' % (fname, m))],
                to_diff=[(ph.inFile('%s.m%s_out.fa' % (fname, m)),
                          ph.outFile('%s.m%s.fa' % (fname, m))),
                         (ph.inFile('%s.m%s.stdout' % (fname, m)),
                          ph.outFile('%s.m%s.stdout' % (fname, m)))])
            conf_list.append(conf)

    # Run with different scoring options.
    for fname in ['1aab', '1ad2', '2trx']:
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.g-20.stdout' % fname),
            args=['-g', '-20',
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.g-20.fa' % fname)],
            to_diff=[(ph.inFile('%s.g-20_out.fa' % fname),
                      ph.outFile('%s.g-20.fa' % fname)),
                     (ph.inFile('%s.g-20.stdout' % fname),
                      ph.outFile('%s.g-20.stdout' % fname))])
        conf_list.append(conf)
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.e-5.stdout' % fname),
            args=['-e', '-5',
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.e-5.fa' % fname)],
            to_diff=[(ph.inFile('%s.e-5_out.fa' % fname),
                      ph.outFile('%s.e-5.fa' % fname)),
                     (ph.inFile('%s.e-5.stdout' % fname),
                      ph.outFile('%s.e-5.stdout' % fname))])
        conf_list.append(conf)
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.ms10.stdout' % fname),
            args=['-ms', '10',
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.ms10.fa' % fname)],
            to_diff=[(ph.inFile('%s.ms10_out.fa' % fname),
                      ph.outFile('%s.ms10.fa' % fname)),
                     (ph.inFile('%s.ms10.stdout' % fname),
                      ph.outFile('%s.ms10.stdout' % fname))])
        conf_list.append(conf)
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.mm-8.stdout' % fname),
            args=['-mm', '-8',
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.mm-8.fa' % fname)],
            to_diff=[(ph.inFile('%s.mm-8_out.fa' % fname),
                      ph.outFile('%s.mm-8.fa' % fname)),
                     (ph.inFile('%s.mm-8.stdout' % fname),
                      ph.outFile('%s.mm-8.stdout' % fname))])
        conf_list.append(conf)

    # Run with matrix file.
    for fname in ['1aab', '1ad2', '2trx']:
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.maVTML200.stdout' % fname),
            args=['-ma', ph.inFile('VTML200I'),
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.maVTML200.fa' % fname)],
            to_diff=[(ph.inFile('%s.maVTML200_out.fa' % fname),
                      ph.outFile('%s.maVTML200.fa' % fname)),
                     (ph.inFile('%s.maVTML200.stdout' % fname),
                      ph.outFile('%s.maVTML200.stdout' % fname))])
        conf_list.append(conf)

    # Run with different banded alignment options.
    for fname in ['1aab', '1ad2', '2trx']:
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.lo5.stdout' % fname),
            args=['-lo', '5',
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.lo5.fa' % fname)],
            to_diff=[(ph.inFile('%s.lo5_out.fa' % fname),
                      ph.outFile('%s.lo5.fa' % fname)),
                     (ph.inFile('%s.lo5.stdout' % fname),
                      ph.outFile('%s.lo5.stdout' % fname))])
        conf_list.append(conf)
        conf = app_tests.TestConf(
            program=path_to_program,
            redir_stdout=ph.outFile('%s.hi5.stdout' % fname),
            args=['-hi', '5',
                  '-s', ph.inFile('%s.fa' % fname),
                  '-o', ph.outFile('%s.hi5.fa' % fname)],
            to_diff=[(ph.inFile('%s.hi5_out.fa' % fname),
                      ph.outFile('%s.hi5.fa' % fname)),
                     (ph.inFile('%s.hi5.stdout' % fname),
                      ph.outFile('%s.hi5.stdout' % fname))])
        conf_list.append(conf)

    # Run with different matrix configuraiton options.
    for fname in ['1aab', '1ad2', '2trx']:
        for c in ['ffff', 'tttt', 'ffft', 'fftf', 'ftff', 'tfff', 'fftt',
                  'fttf', 'ttff', 'tfft']:
            conf = app_tests.TestConf(
                program=path_to_program,
                redir_stdout=ph.outFile('%s.c%s.stdout' % (fname, c)),
                args=['-c', c,
                      '-s', ph.inFile('%s.fa' % fname),
                      '-o', ph.outFile('%s.c%s.fa' % (fname, c))],
                to_diff=[(ph.inFile('%s.c%s_out.fa' % (fname, c)),
                          ph.outFile('%s.c%s.fa' % (fname, c))),
                         (ph.inFile('%s.c%s.stdout' % (fname, c)),
                          ph.outFile('%s.c%s.stdout' % (fname, c)))])
            conf_list.append(conf)

    # ============================================================
    # Run on DNA (Adenoviruses).
    # ============================================================

    # Run with defaults for all non-mandatory options.
    for i in [1, 2, 3]:
        conf = app_tests.TestConf(
            program=path_to_program,
            args=['-a', 'dna',
                  '-s', ph.inFile('adeno%d.fa' % i),
                  '-o', ph.outFile('adeno%d.fa' % i)],
            to_diff=[(ph.inFile('adeno%d_out.fa' % i),
                      ph.outFile('adeno%d.fa' % i))])
        conf_list.append(conf)

    # ============================================================
    # Run on RNA.
    # ============================================================

    # Run with defaults for all non-mandatory options.
    for i in [1, 2, 3]:
        conf = app_tests.TestConf(
            program=path_to_program,
            args=['-a', 'rna',
                  '-s', ph.inFile('adeno%d-rna.fa' % i),
                  '-o', ph.outFile('adeno%d-rna.fa' % i)],
            to_diff=[(ph.inFile('adeno%d-rna_out.fa' % i),
                      ph.outFile('adeno%d-rna.fa' % i))])
        conf_list.append(conf)

    # Execute the tests.
    failures = 0
    for conf in conf_list:
        res = app_tests.runTest(conf)
        # Output to the user.
        print(' '.join(['pair_align'] + conf.args), end=' ')
        if res:
             print('OK')
        else:
            failures += 1
            print('FAILED')

    # Cleanup.
    ph.deleteTempDir()

    print('==============================')
    print('     total tests: %d' % len(conf_list))
    print('    failed tests: %d' % failures)
    print('successful tests: %d' % (len(conf_list) - failures))
    print('==============================')
    # Compute and return return code.
    return failures != 0


if __name__ == '__main__':
    sys.exit(app_tests.main(main))
