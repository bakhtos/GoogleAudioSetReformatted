import os

def convert_labels(priority_strong=True):
    mid_to_dis = open(os.path.join('src', 'mid_to_display_name.tsv'), 'r') 
    mid_dict = dict()
    class_labels_indices = open(os.path.join('src', 'class_labels_indices.csv'), 'r')
    class_labels_dict = dict()
    for line in mid_to_dis:
        id_, label = line.split('\t')
        mid_dict[id_] = label[:-1]
    mid_to_dis.close()

    for line in class_labels_indices:
        parts = line.split(',')
        ix = parts[0]
        if ix == 'index': continue
        id_ = parts[1] 
        label = ','.join(parts[2:])
        label = label[1:-2]
        class_labels_dict[id_] = label
    class_labels_indices.close()
    if priority_strong:
        class_labels_dict.update(mid_dict)
        output_dict = class_labels_dict
    else:
        mid_dict.update(class_labels_dict)
        output_dict = mid_dict
    output = open('class_labels.tsv', 'w')
    output.write("id\tlabel\n")
    for k in sorted(output_dict):
        output.write(f"{k}\t{output_dict[k]}\n")
    output.close()

def convert_strong(filename, output):
    file = open(filename, 'r')
    output = open(output, 'w')
    output.write("filename\tevent_label\tonset\toffset\n")
    for line in file:
        filename, onset, offset, label = line.split('\t')
        if filename == 'segment_id': continue
        label = label[:-1]
        output.write(f"{filename}\t{label}\t{onset}\t{offset}\n")
    file.close()
    output.close()

def convert_strong_posneg(filename, output):
    file = open(filename, 'r')
    output = open(output, 'w')
    output.write("filename\tevent_label\tonset\toffset\tpresent\n")
    for line in file:
        filename, onset, offset, label, posneg = line.split('\t')
        if filename == 'segment_id': continue
        posneg = posneg[:-1]
        output.write(f"{filename}\t{label}\t{onset}\t{offset}\t{posneg}\n")
    file.close()
    output.close()

def convert_weak(filename, output):
    file = open(filename, 'r')
    output = open(output, 'w')
    output.write("filename\tevent_label\n")
    for line in file:
        if line[0] == '#': continue
        elements = line.split(',')
        filename = elements[0]
        onset = elements[1][1:]
        time, dot, zeros = onset.partition('.')
        if time == "0":
            onset = time
        else:
            onset = time+zeros
        #offset = elements[2][1:]
        #time, dot, zeros = offset.partition('.')
        #offset = time+zeros
        labels = elements[3:]
        labels[0] = labels[0][2:]
        labels[-1] = labels[-1][:-2]
        for label in labels:
            output.write(f"{filename}_{onset}\t{label}\n")
    file.close()
    output.close()

if __name__ == '__main__':
    convert_labels()
    convert_strong(os.path.join('src', 'audioset_eval_strong.tsv'), 'audioset_strong_eval.tsv')
    convert_strong(os.path.join('src', 'audioset_train_strong.tsv'), 'audioset_strong_train.tsv')
    convert_strong_posneg(os.path.join('src', 'audioset_eval_strong_framed_posneg.tsv'), 'audioset_strong_eval_posneg.tsv')
    convert_weak(os.path.join('src','eval_segments.csv'), 'audioset_weak_eval.tsv')
    convert_weak(os.path.join('src','balanced_train_segments.csv'), 'audioset_weak_train_balanced.tsv')
    convert_weak(os.path.join('src','unbalanced_train_segments.csv'), 'audioset_weak_train_unbalanced.tsv')
