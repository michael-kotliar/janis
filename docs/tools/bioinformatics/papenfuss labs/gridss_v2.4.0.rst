:orphan:


Gridss
===============

Description
-------------

Tool identifier: ``gridss``

Tool path: ``janis_bioinformatics.tools.pappenfuss.gridss.gridss import Gridss_2_4_0``

Version: v2.4.0

Docker: ``gridss/gridss:2.4.0``

Versions
*********

- v2.4.0 (current)
- `v2.2.3 <gridss_v2.2.3.html>`_

Documentation
-------------

URL
******
*No URL to the documentation was provided*

Tool documentation
******************
*No documentation was provided: `contribute one <https://github.com/illusional>`_*

Outputs
-------
======  ======  ===============
name    type    documentation
======  ======  ===============
out     VCF
======  ======  ===============

Inputs
------
Find the inputs below

Required inputs
***************

=========  =============  ===========  ==========  ===============
name       type           prefix         position  documentation
=========  =============  ===========  ==========  ===============
bams       Array<BAM>                           1
reference  FastaWithDict  --reference
assembly   BAM            --assembly
=========  =============  ===========  ==========  ===============

Optional inputs
***************

==============  ==================  ===========  ==========  ===============
name            type                prefix       position    documentation
==============  ==================  ===========  ==========  ===============
outputFilename  Optional<Filename>  --output
threads         Optional<Integer>   --threads
blacklist       Optional<bed>       --blacklist
==============  ==================  ===========  ==========  ===============


Metadata
********

Author: **Unknown**


*Gridss was last updated on **Unknown***.
*This page was automatically generated on 2019-07-24*.