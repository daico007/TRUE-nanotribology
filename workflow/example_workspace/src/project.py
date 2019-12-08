import textwrap
import logging
import os
import pathlib

import flow
from flow import FlowProject, environments

from util.helper.functions import system_builder
from util.helper.recipes import Alkylsilane
class Project(FlowProject):
    pass
    
@Project.operation
@flow.directives()
@Project.post.isfile("init.top")
@Project.post.isfile("init.gro")
@Project.post.isfile("init.lammps")
@Project.post.isfile("init.ndx")
def initialize_system(job):

    backbone_dict = {'Alkylsilane':Alkylsilane}

    """
    ---------------------------
    Read statepoint information
    ---------------------------
    """
    chainlength = job.statepoint()["chainlength"]
    backbone = backbone_dict[job.statepoint()["backbone"]]
    seed = job.statepoint()["seed"]
    pattern_type = job.statepoint()["pattern_type"]
    terminal_group = job.statepoint()["terminal_group"]
    num_chains = job.statepoint()["n"]

    # change into job directoryA
    _switch_dir(job)
    logging.info("at dir: {}".format(job.ws))
    return  system_builder(seed=seed, chainlength=chainlength, backbone=backbone,
                           terminal_group=terminal_group, num_chains=num_chains)

def _switch_dir(job):
    p = pathlib.Path(job.workspace())
    os.chdir(str(p.absolute()))


if __name__ == "__main__":
    Project().main()
