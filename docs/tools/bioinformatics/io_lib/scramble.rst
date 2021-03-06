:orphan:

scramble
========

*1 contributor · 1 version*

scramble: streaming bam to cram compression


Quickstart
-----------

    .. code-block:: python

       from janis_bioinformatics.tools.io_lib.scramble.versions import Scramble_1_14_1_2

       wf = WorkflowBuilder("myworkflow")

       wf.step(
           "scramble_step",
           Scramble_1_14_1_2(
               inputFilename=None,
               reference=None,
           )
       )
       wf.output("out", source=scramble_step.out)
    

*OR*

1. `Install Janis </tutorials/tutorial0.html>`_

2. Ensure Janis is configured to work with Docker or Singularity.

3. Ensure all reference files are available:

.. note:: 

   More information about these inputs are available `below <#additional-configuration-inputs>`_.



4. Generate user input files for scramble:

.. code-block:: bash

   # user inputs
   janis inputs scramble > inputs.yaml



**inputs.yaml**

.. code-block:: yaml

       inputFilename: inputFilename.bam
       reference: reference.fasta




5. Run scramble with:

.. code-block:: bash

   janis run [...run options] \
       --inputs inputs.yaml \
       scramble





Information
------------


:ID: ``scramble``
:URL: `https://github.com/jkbonfield/io_lib/ <https://github.com/jkbonfield/io_lib/>`_
:Versions: 1.14.12
:Container: quay.io/biocontainers/staden_io_lib:1.14.12--h244ad75_0
:Authors: Matthias De Smet (@mattdsm)
:Citations: None
:Created: 2020-02-27
:Updated: 2020-02-27



Outputs
-----------

======  ============  ===============
name    type          documentation
======  ============  ===============
out     stdout<CRAM>
======  ============  ===============



Additional configuration (inputs)
---------------------------------

==========================  ==================  ========  ==========  =================================================
name                        type                prefix      position  documentation
==========================  ==================  ========  ==========  =================================================
inputFilename               BAM                                  200
reference                   FastaFai            -r                    Reference sequence file.
outputFilename              Optional<Filename>
range                       Optional<String>    -R                    Specifies the refseq:start-end range
maxBases                    Optional<Integer>   -b                    Max. bases per slice, default 5000000.
maxSequences                Optional<Integer>   -s                    Sequences per slice, default 10000.
maxSlicesPerContainer       Optional<Integer>   -S                    Slices per container, default 1.
embedReferenceSeuence       Optional<Boolean>   -e                    Embed reference sequence.
nonReferenceBaseEncoding    Optional<Boolean>   -x                    Non-reference based encoding.
multipleReferencesPerSlice  Optional<Boolean>   -M                    Use multiple references per slice.
generateTags                Optional<Boolean>   -m                    Generate MD and NM tags.
lzmaCompression             Optional<Boolean>   -Z                    Also compress using lzma
discardReadNames            Optional<Boolean>   -n                    Discard read names where possible.
preserveAuxTags             Optional<Boolean>   -P                    Preserve all aux tags (incl RG,NM,MD).
preserveAuxTagSizes         Optional<Boolean>   -p                    Preserve aux tag sizes ('i', 's', 'c').
noAddPG                     Optional<Boolean>   -q                    Don't add scramble @PG header line.
decodeStop                  Optional<Integer>   -N                    Stop decoding after 'integer' sequences.
threads                     Optional<Integer>   -t                    Number of threads. (default = 1)
enableQualityBinning        Optional<Integer>   -B                    Enable Illumina 8 quality-binning system (lossy).
==========================  ==================  ========  ==========  =================================================
