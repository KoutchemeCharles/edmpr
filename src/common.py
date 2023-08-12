from src.distance import (
    str_dist, seq_dist, ted_dist,
    str_norm_dist as nstr_dist, seq_norm_dist as nseq_dist, ted_norm_dist as nted_dist,
    str_rps_dist, seq_rps_dist, ted_rps_dist,
    bleu_dist, rouge1_dist, rougelcsum_dist, codebleu_dist
)


new_assignments_id = {
    "count_102.py_ca117_count_letters": "count_letters",
    "func_reverse.py_ca116_reverse": "reverse_by_swap",
    "iterative07.py_ca278_index": "index_iter",
    "iterative07.py_ca278_search": "search_iter",
    "iterative08.py_ca278_index": "index_iter",
    "iterative08.py_ca278_search": "search_iter",
    "maximum_102.py_ca117_maximum": "maximum",
    "minimum_102.py_ca117_minimum": "minimum",
    "recursive07.py_ca278_search": "search_recur",
    "recursive08.py_ca278_search": "search_recur",
    "reverse.py_ca277_reverse": "reverse_iter",
    "reverse_102.py_ca117_reverse_list": "reverse_recur",
    "sumup_102.py_ca117_sumup": "sumup",
    "swap_42.py_ca117_swap_keys_values": "swap_keys_values",
    "swap_v1_042.py_ca117_swap_keys_values": "swap_keys_values"
}



dist_funcs = [str_dist, seq_dist, ted_dist,
                nstr_dist, nseq_dist, nted_dist,
                bleu_dist, rouge1_dist, rougelcsum_dist, codebleu_dist]
