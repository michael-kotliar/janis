:orphan:

BCFTools: Concat
=================================

*0 contributors · 1 version*


Concatenate or combine VCF/BCF files. All source files must have the same sample
columns appearing in the same order. The program can be used, for example, to
concatenate chromosome VCFs into one VCF, or combine a SNP VCF and an indel
VCF into one. The input files must be sorted by chr and position. The files
must be given in the correct order to produce sorted VCF on output unless
the -a, --allow-overlaps option is specified. With the --naive option, the files
are concatenated without being recompressed, which is very fast but dangerous
if the BCF headers differ.



Quickstart
-----------

    .. code-block:: python

       from janis_bioinformatics.tools.bcftools.concat.versions import BcfToolsConcat_1_9

       wf = WorkflowBuilder("myworkflow")

       wf.step(
           "bcftoolsconcat_step",
           BcfToolsConcat_1_9(
               vcf=None,
           )
       )
       wf.output("out", source=bcftoolsconcat_step.out)
    

*OR*

1. `Install Janis </tutorials/tutorial0.html>`_

2. Ensure Janis is configured to work with Docker or Singularity.

3. Ensure all reference files are available:

.. note:: 

   More information about these inputs are available `below <#additional-configuration-inputs>`_.



4. Generate user input files for bcftoolsConcat:

.. code-block:: bash

   # user inputs
   janis inputs bcftoolsConcat > inputs.yaml



**inputs.yaml**

.. code-block:: yaml

       vcf:
       - vcf_0.vcf.gz
       - vcf_1.vcf.gz




5. Run bcftoolsConcat with:

.. code-block:: bash

   janis run [...run options] \
       --inputs inputs.yaml \
       bcftoolsConcat





Information
------------


:ID: ``bcftoolsConcat``
:URL: `https://samtools.github.io/bcftools/bcftools.html#concat <https://samtools.github.io/bcftools/bcftools.html#concat>`_
:Versions: v1.9
:Container: michaelfranklin/bcftools:1.9
:Authors: 
:Citations: Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R, and 1000 Genome Project Data Processing Subgroup, The Sequence alignment/map (SAM) format and SAMtools, Bioinformatics (2009) 25(16) 2078-9
:DOI: http://www.ncbi.nlm.nih.gov/pubmed/19505943
:Created: None
:Updated: 2019-09-09



Outputs
-----------

======  =============  ===============
name    type           documentation
======  =============  ===============
out     CompressedVCF
======  =============  ===============



Additional configuration (inputs)
---------------------------------

==============  ====================  ============  ==========  ============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
name            type                  prefix          position  documentation
==============  ====================  ============  ==========  ============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
vcf             Array<CompressedVCF>                        15
outputFilename  Optional<Filename>    -o                        --output: When output consists of a single stream, write it to FILE rather than to standard output, where it is written by default.
allowOverLaps   Optional<Boolean>     -a                        First coordinate of the next file can precede last record of the current file.
compactPS       Optional<Boolean>     -c                        Do not output PS tag at each site, only at the start of a new phase set block.
rmDups          Optional<String>      -d                        Output duplicate records present in multiple files only once: <snps|indels|both|all|none>
rmDupsNone      Optional<Boolean>     -d                        Alias for -d none
fileList        Optional<File>        -f                        Read the list of files from a file.
ligate          Optional<Boolean>     -l                        Ligate phased VCFs by matching phase at overlapping haplotypes
noVersion       Optional<Boolean>     --no-version              Do not append version and command line information to the output VCF header.
naive           Optional<Boolean>     -n                        Concatenate files without recompression (dangerous, use with caution)
outputType      Optional<String>      -O                        --output-type b|u|z|v: Output compressed BCF (b), uncompressed BCF (u), compressed VCF (z), uncompressed VCF (v). Use the -Ou option when piping between bcftools subcommands to speed up performance by removing unnecessary compression/decompression and VCF←→BCF conversion.
minPG           Optional<Integer>     -q                        Break phase set if phasing quality is lower than <int> [30]
regions         Optional<String>      -r                        --regions chr|chr:pos|chr:from-to|chr:from-[,…]: Comma-separated list of regions, see also -R, --regions-file. Note that -r cannot be used in combination with -R.
regionsFile     Optional<File>        -R                        --regions-file: Regions can be specified either on command line or in a VCF, BED, or tab-delimited file (the default). The columns of the tab-delimited file are: CHROM, POS, and, optionally, POS_TO, where positions are 1-based and inclusive. The columns of the tab-delimited BED file are also CHROM, POS and POS_TO (trailing columns are ignored), but coordinates are 0-based, half-open. To indicate that a file be treated as BED rather than the 1-based tab-delimited file, the file must have the '.bed' or '.bed.gz' suffix (case-insensitive). Uncompressed files are stored in memory, while bgzip-compressed and tabix-indexed region files are streamed. Note that sequence names must match exactly, 'chr20' is not the same as '20'. Also note that chromosome ordering in FILE will be respected, the VCF will be processed in the order in which chromosomes first appear in FILE. However, within chromosomes, the VCF will always be processed in ascending genomic coordinate order no matter what order they appear in FILE. Note that overlapping regions in FILE can result in duplicated out of order positions in the output. This option requires indexed VCF/BCF files. Note that -R cannot be used in combination with -r.
threads         Optional<Integer>     --threads                 Number of output compression threads to use in addition to main thread. Only used when --output-type is b or z. Default: 0.
==============  ====================  ============  ==========  ============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
