#!/usr/bin/env python
"""Initialize the project's data space.

Iterates over all defined state points and initializes
the associated job workspace directories."""
import argparse
import logging
import datetime
from copy import deepcopy
from hashlib import sha1

import signac

logging.basicConfig(filename='init.log', filemode='w', level=logging.INFO)

'''
----------------------------------------
5 Backbone chainlengths to be considered
----------------------------------------
'''

chainlengths = [5, 7, 9, 13, 17]

# Initialize the project
def main(args, random_seed):
    project = signac.init_project("Chainlengths")
    logging.info("Init begin: {}".format(datetime.datetime.today()))
    logging.info("Initialized project name")
    statepoints = list()
    # generate the new top and bottom monolayers
    for replication_index in range(args.num_replicas):
        for chainlength in chainlengths:
            the_statepoint = dict(
                              # Carbon backbone length
                                chainlength = chainlength,
                              # Backbone chemistry
                                backbone = 'Alkylsilane',
                              # Terminal group
                                terminal_group = 'methyl',
                              # Number of monolayer chains
                                n = 50,
                              # monolayer pattern type
                                pattern_type = 'random',
                              # Random seed
                                seed = random_seed*(replication_index + 1))
            project.open_job(statepoint=the_statepoint).init()
            statepoints.append(the_statepoint)
            logging.info(msg="At the statepoint: {}".format(the_statepoint))
    # write statepoints to signac statepoint file
    project.write_statepoints(statepoints=statepoints)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Initialize the data space.")
    parser.add_argument(
        '-s','--seed',
        type=str,
        help="A string to generate a random seed.")
    parser.add_argument(
        '-n', '--num-replicas',
        type=int,
        default=1,
        help="Initialize multiple replications.")
    args = parser.parse_args()

    # Generate an integer from the random str.
    try:
        random_seed = int(args.seed)
    except ValueError:
        random_seed = int(sha1(args.random.encode()).hexdigest(), 16) % (10 ** 8)

    logging.info("Params:\
                random: {}\
                num-replicas: {}".format(
                                    random_seed,
                                    args.num_replicas,
                                    ))

    main(args, random_seed)
