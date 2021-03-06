:orphan:

Merge and Mark Duplicates
============================================

*0 contributors · 2 versions*

No documentation was provided: `contribute one <https://github.com/PMCC-BioinformaticsCore/janis-bioinformatics>`_


Quickstart
-----------

    .. code-block:: python

       from janis_bioinformatics.tools.common.mergeandmark.mergeandmark_4_0 import MergeAndMarkBams_4_0

       wf = WorkflowBuilder("myworkflow")

       wf.step(
           "mergeandmarkbams_step",
           MergeAndMarkBams_4_0(
               bams=None,
           )
       )
       wf.output("out", source=mergeandmarkbams_step.out)
    

*OR*

1. `Install Janis </tutorials/tutorial0.html>`_

2. Ensure Janis is configured to work with Docker or Singularity.

3. Ensure all reference files are available:

.. note:: 

   More information about these inputs are available `below <#additional-configuration-inputs>`_.



4. Generate user input files for mergeAndMarkBams:

.. code-block:: bash

   # user inputs
   janis inputs mergeAndMarkBams > inputs.yaml



**inputs.yaml**

.. code-block:: yaml

       bams:
       - bams_0.bam
       - bams_1.bam




5. Run mergeAndMarkBams with:

.. code-block:: bash

   janis run [...run options] \
       --inputs inputs.yaml \
       mergeAndMarkBams





Information
------------

URL: *No URL to the documentation was provided*

:ID: ``mergeAndMarkBams``
:URL: *No URL to the documentation was provided*
:Versions: 4.0.12, 4.1.3
:Authors: 
:Citations: 
:Created: None
:Updated: None



Outputs
-----------

======  ==========  ===============
name    type        documentation
======  ==========  ===============
out     IndexedBam
======  ==========  ===============


Embedded Tools
***************

======================  ================================
GATK4: Merge SAM Files  ``Gatk4MergeSamFiles/4.0.12.0``
GATK4: Mark Duplicates  ``Gatk4MarkDuplicates/4.0.12.0``
======================  ================================



Additional configuration (inputs)
---------------------------------

==================================  =================  ================================================================================================================================================================================================================================================================================================================================================================================================
name                                type               documentation
==================================  =================  ================================================================================================================================================================================================================================================================================================================================================================================================
bams                                Array<IndexedBam>
createIndex                         Optional<Boolean>
maxRecordsInRam                     Optional<Integer>
mergeSamFiles_useThreading          Optional<Boolean>  Option to create a background thread to encode, compress and write to disk the output file. The threaded version uses about 20% more CPU and decreases runtime by ~20% when writing out a compressed BAM file.
mergeSamFiles_validationStringency  Optional<String>   Validation stringency for all SAM files read by this program. Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.The --VALIDATION_STRINGENCY argument is an enumerated type (ValidationStringency), which can have one of the following values: [STRICT, LENIENT, SILENT]
==================================  =================  ================================================================================================================================================================================================================================================================================================================================================================================================


