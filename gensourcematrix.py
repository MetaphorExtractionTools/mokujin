#!/usr/bin/env python
# coding: utf-8

# Copyright (C) USC Information Sciences Institute
# Author: Vladimir M. Zaytsev <zaytsev@usc.edu>
# URL: <http://nlg.isi.edu/>
# For more information, see README.md
# For license information, see LICENSE


#!/usr/bin/env python
# coding: utf-8

# Copyright (C) USC Information Sciences Institute
# Author: Vladimir M. Zaytsev <zaytsev@usc.edu>
# URL: <http://nlg.isi.edu/>
# For more information, see README.md
# For license information, see LICENSE


import logging
import argparse

from cPickle import load
from mokujin.index import TripleIndex
from mokujin.index import TripleSearchEngine
from mokujin.sourcematrix import extract_source_matrix


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", default="data/index", help="Triple store index directory", type=str)
    parser.add_argument("-i", "--input", default=None, help="Pickle file with imported sources",  type=str)
    parser.add_argument("-t", "--threshold", default=100, help="Threshold to select first k best sources",  type=int)
    args = parser.parse_args()

    if args.input is None:
        exit(0)

    logging.info("INDEX DIR: %s" % args.data)
    logging.info("INPUT: %s" % args.input)

    input_fl = open(args.input, "rb")
    matrix_fl = "%s.matrix.txt" % args.input
    terms_fl = "%s.terms.txt" % args.input
    patterns_fl = "%s.patterns.txt" % args.input

    logging.info("TERMS OUT: %s" % terms_fl)
    logging.info("PATTERN OUT: %s" % patterns_fl)
    logging.info("MATRIX OUT: %s" % matrix_fl)

    matrix_fl = open(matrix_fl, "w")
    terms_fl = open(terms_fl, "w")
    patterns_fl = open(patterns_fl, "w")

    logging.info("LOADING INDEX")
    indexer = TripleIndex(args.data)
    engine = TripleSearchEngine(indexer)

    sources = load(input_fl)
    extract_source_matrix(sources, engine, terms_fl, patterns_fl, matrix_fl, threshold=args.threshold)

    input_fl.close()
    matrix_fl.close()
    terms_fl.close()
    patterns_fl.close()

    logging.info("DONE")