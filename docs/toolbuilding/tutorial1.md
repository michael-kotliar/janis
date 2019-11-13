
# Tool Tutorial 1 - Wrapping a new tool

## Introduction

A CommandTool is the interface between Janis and a program to be executed. Simply put, a CommandTool has a name, a command, inputs, outputs and a container to run in. Inputs and arguments can have a prefix and / or position, and this is used to construct the command line.

The Janis documentation for the [CommandTool](https://janis.readthedocs.io/en/latest/references/commandtool.html) gives an introduction to the tool structure and a template for constructing your own tool. A tool wrapper must provide all of the information to configure and run the specified tool, this includes the `base_command`, [`janis.ToolInput`](https://janis.readthedocs.io/en/latest/references/commandtool.html#tool-input), [`janis.ToolOutput`](https://janis.readthedocs.io/en/latest/references/commandtool.html#tool-output),  a `container` and its version.

## Requirements

You must have Python 3.6 and Janis installed:

```bash
pip3 install janis-pipelines
```

You can check you have the correct version of Janis installed by running:

```bash
$ janis -v
--------------------  ------
janis-core            v0.7.1
janis-assistant       v0.7.8
janis-unix            v0.7.0
janis-bioinformatics  v0.7.1
--------------------  ------
```


### Container

> _Further information_: [Containerising your tools](https://janis.readthedocs.io/en/latest/tutorials/containers.html)

> Guide on using containers

For portability, we require that you specify an OCI compliant  `container` (eg: Docker) for your tool. Often they're will already be a container with some searching, however here's a guide on [preparing your tools in containers](https://janis.readthedocs.io/en/latest/tutorials/containers.html) to ensure it works across all environments. 


## Samtools flagstat

In this workshop we're going to wrap `samtools flagstat`. 

### Samtools project links

- Latest version: `1.9`
- Project page: [http://www.htslib.org/doc/samtools.html](http://www.htslib.org/doc/samtools.html)
- Github: [samtools/samtools](https://github.com/samtools/samtools)
- Docker containers: [quay.io/biocontainers/samtools](https://quay.io/repository/biocontainers/samtools?tag=latest&tab=tags) (automatically / community generated)
	- Latest tag: `1.9--h8571acd_11`


### Command tool template

The following template is the minimum amount of information required to wrap a tool. For more information, it's worth having a look at 

```python
from typing import List, Optional, Union
import janis as j

class ToolName(j.CommandTool):
    @staticmethod
    def tool() -> str:
        return "toolname"
        
    @staticmethod
    def base_command() -> Optional[Union[str, List[str]]]:
        pass
        
    @staticmethod
    def container() -> str:
        return ""

    @staticmethod
    def version() -> str:
        pass

    def inputs(self) -> List[j.ToolInput]:
        return []

    def outputs(self) -> List[j.ToolOutput]:
        return []
```

### Basic information

Let's start by creating a file with this template:

```bash
vim samtoolsflagstat.py
```

We can start by filling in the basic information:

- Rename the class to be `SamtoolsFlagstat`,
- Add the tool identifier in the `tool()` method,
- Add the container `"quay.io/biocontainers/samtools:1.9--h8571acd_11"`,
- Add the version: `"1.9.0"`.

You'll have a class definition like the following
```python
class SamtoolsFlagstat(j.CommandTool):
    @staticmethod
    def tool() -> str:
        return "samtoolsflagstat"

    @staticmethod
    def base_command() -> Optional[Union[str, List[str]]]:
        return ["samtools", "flagstat"]
    
    @staticmethod
    def container() -> str:
        return "quay.io/biocontainers/samtools:1.9--h8571acd_11"

    @staticmethod
    def version() -> str:
        return "1.9.0"
	
	# inputs and outputs
```

### Inputs

#### Inspecting inputs

Although we can check `samtools`' [documentation](http://www.htslib.org/doc/samtools.html), it's often easier to check the help text to find the appropriate tool inputs.  To view the help guide, we can run:

```bash
samtools flagstat # no -h / --help required
```
Output:
```
Usage: samtools flagstat [options] <in.bam>
    --input-fmt-option OPT[=VAL]
            Specify a single input file format option in the form of OPTION or OPTION=VALUE

    -@, --threads INT
            Number of additional threads to use [0]
```

We're going to add:

- The positional `<in.bam>` input
- The configuration `--threads` input

#### Positional Bam input

Our positional input is a Bam, so we'll import the Bam type from `janis` with the following line:

```python
from janis.data_types import Bam
```

Then we can declare our two inputs:

1. Positional bam input
2. Threads configuration input with the prefix `--threads`

```python
	# in the class
	def inputs(self):
	return [
		# 1. Positional bam input
		j.ToolInput(
			 tag="bam", 
			 input_type=Bam, 
			 position=1, 
			 doc="Input bam to generate statistics for"
		),
		# 2. `threads` inputs
		j.ToolInput(
		    "threads", 
		    j.Int(optional=True), 
		    prefix="--threads", 
		    doc="(-@)  Number of additional threads to use [0] "
		)
	]
```


### Outputs

The only output of `samtools flagstat` is the statistics that are written to `stdout`. We can collect this with the `Stdout` data type. We'll give this the output tag `stats` which will give the following `ToolOutput`:

```python
	# in the class
	def outputs(self):
		return [
			ToolOutput("stats", Stdout)
		]
```


### Tool definition

Putting this all together, you should have the following tool definition:

```python
from typing import List, Optional, Union
import janis as j
from janis.bioinformatics.data_types import Bam

class SamtoolsFlagstat(j.CommandTool):
    @staticmethod
    def tool() -> str:
        return "samtoolsflagstat"

    @staticmethod
    def base_command() -> Optional[Union[str, List[str]]]:
        return ["samtools", "flagstat"]

    @staticmethod
    def container() -> str:
        return "quay.io/biocontainers/samtools:1.9--h8571acd_11"

    @staticmethod
    def version() -> str:
        return "1.9.0"

    def inputs(self) -> List[j.ToolInput]:
        return [
		j.ToolInput(
			 tag="bam", 
			 input_type=Bam, 
			 position=1, 
			 doc="Input bam to generate statistics for"
		),
		# 2. `threads` inputs
		j.ToolInput(
		    "threads", 
		    j.Int(optional=True), 
		    prefix="--threads", 
		    doc="(-@)  Number of additional threads to use [0] "
		)

        ]

    def outputs(self) -> List[j.ToolOutput]:
        return [j.ToolOutput("out", Stdout)]
```

## Testing the tool

We can test the translation to janis from the CLI:

> If you have multiple command tools or workflows declared in the same file, you will need to provide the `--name` parameter with the name of your workflow.

```bash
janis translate samtoolsflagstat.py cwl
```


### Running the workflow

We can call the `janis run` functionality (default CWLTool) with our bam input:

```bash
janis run samtoolsflagstat.py --bam /data/brca1.bam
```

OUTPUT:
```
TID:        dc7844
WID:        dc7844
Name:       samtoolsflagstatWf

Engine:     cwltool
Engine url: N/A

Path:       /Users/franklinmichael/janis/execution/samtoolsflagstatWf/20190806_095944_dc7844/

Status:     Completed
Duration:   3
Start:      2019-08-05T23:59:44.596567+00:00
Finish:     N/A

Jobs: 
       

Outputs:    out
2019-08-05T23:59:47+00:00 [INFO]: Hard linking /Users/franklinmichael/janis/execution/samtoolsflagstatWf/20190806_095944_dc7844/workflow/generated-18f2defe-b7dd-11e9-8af4-f218985ebfa7.txt to /Users/franklinmichael/janis/execution/samtoolsflagstatWf/20190806_095944_dc7844/outputs/out.txt
Finished managing task 'dc7844'. View the task outputs: file:///Users/franklinmichael/janis/execution/samtoolsflagstatWf/20190806_095944_dc7844/
```

We can test this by looking at our output file: 

```bash
cat /Users/franklinmichael/janis/execution/samtoolsflagstatWf/20190806_095944_dc7844/outputs/out.txt
```

```
20061 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
337 + 0 supplementary
0 + 0 duplicates
19971 + 0 mapped (99.55% : N/A)
19724 + 0 paired in sequencing
9862 + 0 read1
9862 + 0 read2
18606 + 0 properly paired (94.33% : N/A)
19544 + 0 with itself and mate mapped
90 + 0 singletons (0.46% : N/A)
860 + 0 with mate mapped to a different chr
691 + 0 with mate mapped to a different chr (mapQ>=5)
```

## Outcomes

- Learn about the structure of a CommandTool
- Use an existing docker container
- Look at the inputs and outputs of an existing tool
- Use InputSelectors to get the value of an input
