# Google's Audioset: Reformatted

During my work with Google's Audioset I encountered some problems due to the
fact that [Weak](https://research.google.com/audioset/download.html) and
[Strong](https://research.google.com/audioset/download_strong.html) versions
of the dataset using different csv formatting for the data, and that also
labels used in the two dataset [are different](https://github.com/audioset/ontology/issues/9)
and also presented in files with different formatting.

This repository aims to unify the formats of the datasets so that it is possible
to analyse them in the same pipelines, and also make the dataset files compatible
with [psds_eval](https://github.com/audioanalytic/psds_eval), [dcase_util](https://github.com/DCASE-REPO/dcase_util)
and [sed_eval](https://github.com/TUT-ARG/sed_eval).

The [source folder](src) contains also the original dataset files and the script
`convert.py` to regenerate the reformatted files. It can be run from this folder
as ```python src/convert.py```, it does not require any external libraries.

NOTE: `audioset_weak_train_unbalanced.tsv` has been manually split into two
files to comply with GitHub's size limit. 
