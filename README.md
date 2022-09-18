# Google's AudioSet: Reformatted

During my work with [Google's AudioSet](https://research.google.com/audioset/index.html)
I encountered some problems due to the
fact that [Weak](https://research.google.com/audioset/download.html) [1] and
[Strong](https://research.google.com/audioset/download_strong.html) [2] versions
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

## Changes in dataset

All files are converted to **tab-separated `*.tsv` files** (i.e. `csv` files with `\t`
as a separator). All files have a header as the first line.

### New fields and filenames

Fields are renamed according to the following table, to be compatible with [psds_eval](https://github.com/audioanalytic/psds_eval):

|**Old field**|**New field**|
|-------------|-------------|
|`YTID`|`filename`|
|`segment_id`|`filename`|
|`start_seconds`|`onset`|
|`start_time_seconds`|`onset`|
|`end_seconds`|`offset`|
|`end_time_seconds`|`offset`|
|`positive_labels`|`event_label`|
|`label`|`event_label`|
|`present`|`present`|

For class label files, `id` is now the name for the for `mid` label (e.g. `/m/09xor`)
and `label` for the human-readable label (e.g. `Speech`). Index of label indicated
for Weak dataset labels (`index` field in `class_labels_indices.csv`) is not used.

Files are renamed according to the following table to ensure consisted naming
of the form `audioset_[weak|strong]_[train|eval]_[balanced|unbalanced|posneg]*.tsv`:

|**Old name**|**New name**|
|------------|------------|
|`balanced_train_segments.csv`|`audioset_weak_train_balanced.tsv`|
|`unbalanced_train_segments.csv`|`audioset_weak_train_unbalanced.tsv` (split into two files)|
|`eval_segments.csv`|`audioset_weak_eval.tsv`|
|`audioset_train_strong.tsv`|`audioset_strong_train.tsv`|
|`audioset_eval_strong.tsv`|`audioset_strong_eval.tsv`|
|`ausioset_eval_strong_framed_posneg.tsv`|`audioset_strong_eval_posneg.tsv`|
|`class_labels_indices.csv`|`class_labels.tsv` (merged with `mid_to_display_name.tsv`)|
|`mid_to_display_name.tsv`|`class_labels.tsv` (merged with `class_labels_indices.csv`)|

### Strong dataset changes

Only changes to the Strong dataset are renaming of fields and reordering of columns,
so that both Weak and Strong version have `filename` and `event_label` as first 
two columns.

### Weak dataset changes

- Labels are given one per line, instead of comma-separated and quoted list

- To make sure that `filename` format is the same as in Strong verson, the following
format change is made:

**The value of the `start_seconds` field is converted to milliseconds and appended
to the `filename` with an underscore.** Since all files in the dataset are assumed to be
10 seconds long, this unifies the format of `filename` with the Strong version and
makes `end_seconds` also redundant.

### Class labels changes

Class labels from both datasets are merged into one file and given in alphabetical
order of `id`s. Since same `id`s are present in both datasets, but sometimes with
different human-readable labels, labels from Strong dataset overwrite those from Weak.
It is possible to regenerate `class_labels.tsv` while giving priority to the Weak
version of labels by calling `convert_labels(False)` from [`src/convert.py`](src/convert.py).

## License

Both the original dataset and this reworked version are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

**NOTE** Labels come from the [AudioSet ontology](https://research.google.com/audioset/ontology/index.html), which 
is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/),
but is not replicated in this repository.

## References

[1] Gemmeke, J. F., Ellis, D. P., Freedman, D., Jansen, A., Lawrence, W., Moore, R. C., ... & Ritter, M. (2017, March). Audio set: An ontology and human-labeled dataset for audio events. In 2017 IEEE international conference on acoustics, speech and signal processing (ICASSP) (pp. 776-780). IEEE.

[2] Hershey, S., Ellis, D. P., Fonseca, E., Jansen, A., Liu, C., Moore, R. C., & Plakal, M. (2021, June). The benefit of temporally-strong labels in audio event classification. In ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 366-370). IEEE.
