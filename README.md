# TRUE-nanotribology

### TRUE Simulation
A TRUE simulation is defined as a **T**ransparent, **R**eproducible, **U**sable by others, and **E**xtensible. The concept was born to encourage researchers to set up project in a more standardized fashion, with the goal to improve the reprodicibility and scalability, as well as lower the barrier for new researcher entering any given project. Currently, there is no strict standard to build a TRUE simulation project, but there are a few principles that could be demonstrated through different examples workflow. Below is an example of a TRUE nanotribology screening project, which shows how researcher at Vanderbilt University have successfully inherited and significantly scaled up a TRUE project. 

### Original Project
The original project was developed by Dr. Andrew Z. Summers to study the tribological properties when two self-assembled monolayer (SAM) coated surface are sheared against each other. The project focus to study the effects induced by monolayer density, backbone chain length, and some terminal groups on the tribological properties of these surfaces, and have spanned approximately 820 state points.

The original project workflow could be found in several github repository hosted by the author Andrew Z. Summers:
- https://github.com/summeraz/monolayer_screening
- https://github.com/summeraz/terminal_group_screening
- https://github.com/summeraz/terminal_groups_mixed

### Current Project
Currently, new members of the project are extending from the original screening proejct to explore even more variables, scaling from the original 820 statepoints to an additional of almost 40,000 statepoints. In this repository, we hope demonstrate how a TRUE simulation can be set up, and how these projects can be readily transfered to and picked up by new member joining the research. The latter point would be extremely beneficial in academia setting where students constantly leaving (graduating) and joining the group.

### Repository Structure
This repository is set up to provide some background about the incentive of these types of shearing, follow by a demonstration of single complete workflow, and complete by how it can be scaled up using several open-source software packages such as MoSDeF (mBuild and Foyer), signac and signac-flow. The mentioned materials will be located insde the `workflow` folders. Please also be noted that several packages have to be installed and built for demonstration to work properly.
#### Single Run 
This Single Run folder is meant to provide a brief overview about both the incentive of the nanotriboly screening project as well as one complete workflow, starting with system initialization and end with coefficient of friction (COF) and force of adhesion (F_0) for a system. Most of the code will be executable inside a jupyter notebook, however, be informed that these type of simulation would usually require a considerable amount of computational resouce. 

(If this is only for showing purpose, we might only need to show up to LAMMPS energy minimization and cite Andrew paper for the rest of the workflow)
#### Batch Run
The Batch Run folder to show how our module is readily expansible - need to turn the single run script to method (OOP), show how the data is generate correctly (call and visualize some data), and how the specific data can be retrieved efficiently (showing how signac can find specific job statepoint)
