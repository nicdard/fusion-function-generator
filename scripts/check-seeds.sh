#!/bin/bash

for dir in semantic_fusion_seeds/*/ ; do
    theory=$(basename "$dir")
    # skip unsupported theories
    if [[ $theory == "AUFBVDTLIA" || $theory == "AUFDTLIA" || $theory == "QF_ABVFP" ]] ; then
        echo "skipping $theory..."
        continue
    fi

    echo "checking $theory..."
    for subdir in "$dir"*/ ; do
        oracle=$(basename "$subdir")
        for filename in "$subdir"*.smt2 ; do
            z3_out=$(timeout 10 z3 "$filename")
            if [[ $z3_out != "$oracle" && $z3_out != "" ]] ; then
                echo "-------------------------------------------------------"
                echo "$filename"
                echo "oracle: $oracle"
                echo "z3:     $z3_out"
                echo "-------------------------------------------------------"
            fi
        done
    done
done

echo "done"
