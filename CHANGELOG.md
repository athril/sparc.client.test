v0.2.0
======
New functionalities:
* Added O2SparcService service:
   * Introduced a `O2SparcSolver` class which is the main class for running computational jobs on o²S²PARC. This class holds the following methods:
   * `submit_job`
   * `get_job_progress`
   * `job_done`
   * `get_results`
   * `get_job_log`
* Introduced `get_solver` method to `O2SparcService` which returns a `O2SparcSolver` object
* Scaffold Retrieval:
   * Introducing the ability to use `sparc.client` to retrieve scaffolds or scaffold descriptions.
   * The retrieved scaffold or scaffold description files can now be converted to a commonly used mesh format, such as VTK.
   * Reuse of packages from the mapping tools codebase ensures efficient and standardized mesh conversion.
* MBF Segmentation Export:
   * Added support for exporting MBF Segmentation data to a commonly used mesh format, like VTK.
* Segmentation Data Analysis:
   * New functionality to analyze a given segmentation data file for suitability in the mapping tools fitting workflow, and provide a clear and informative report.
* Updated Documentation:
   * Added the [SPARC Python Zinc Client tutorial](https://github.com/nih-sparc/sparc.client/blob/main/docs/tutorial-zinc.ipynb) to reflect the features related to Zinc.


v0.1.0
======
Fixes:
* download multiple files from Pennsieve #12
* pennsieve Download file API #14
* Github action updates: Reviewdog should run whenever a PR is modified after opening #15
* new tutorial in Jupyter Notebook
* README.md update


v0.0.2
======
Alpha2 release of Python Sparc Client.
Major updates:
* Code coverage at 100%
* Sphinx documentation with Github Pages


v0.0.1
======
Alpha release of Python Sparc Client.
Basic functionalities:
* automatic/manual module loading
* ServiceBase class for adding new modules
* Pennsieve module with basic functionalities: 
   * listing datasets, files, records
   * downloading files
   * Basic API support (GET/POST) 
## [v0.0.42] - 2023-12-12
### :sparkles: New Features
- [`3124672`](https://github.com/athril/sparc.client/commit/31246720c92a0acbeaaf648878d5c46e5747c99d) - improving release mechanism *(commit by [@athril](https://github.com/athril))*


[v0.0.42]: https://github.com/athril/sparc.client/compare/v0.0.41...v0.0.42