Conditionals
#############

As of Janis v0.9.5, Janis supports conditionality within a pipeline. This allows Janis to run a step _when_ specific
conditions are met.

This has the following minimum specifications:

- CWL v1.2 or later (currently in beta)
- WDL v1.0 or later (Janis uses the WDL Development Biscayne specification)

See the `engine support <#engine-support>`_ support section for information about which engines this is supported by.


How to do conditionals
------------------------

It will be helpful to have a basic understanding of conditionals from CWL, WDL or Nextflow.


Examples
-----------


Engine support
--------------

WDL
......

WDL has supported conditionality since draft-2. Janis only exports the WDL development Biscayne specification
(to become WDL v1.2) and hence requires:

- Cromwell >= 43
- MiniWDL (any version)


CWL
......

The conditionals spec is still in development, but likely to make it to the v1.2 specification.

Notes:

- CWL Spec PR: https://github.com/common-workflow-language/cwl-v1.2/pull/4
- CWLTool conditionals PR: https://github.com/common-workflow-language/cwltool/pull/1222


