import argparse
from data_io import read_pkl
from eval_erl import compute_node_segment_lut_low_mem, compute_erl


def test_AxonEM(gt_stats_path, pred_seg_path, num_chunk=1):
    # get stats
    gt_graph, gt_node_voxel = read_pkl(gt_stats_path)

    node_segment_lut = compute_node_segment_lut_low_mem(
        gt_node_voxel, [pred_seg_path], num_chunk
    )
    scores = compute_erl(gt_graph, node_segment_lut)
    print(f"ERL for seg {pred_seg_path}: {scores[0]}")


def get_arguments():
    """
    The function `get_arguments()` is used to parse command line arguments for the evaluation on AxonEM.
    :return: The function `get_arguments` returns the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="ERL evaluation with precomputed gt statistics"
    )
    parser.add_argument(
        "-s",
        "--seg-path",
        type=str,
        help="path to the segmentation prediction",
        required=True,
    )
    parser.add_argument(
        "-g",
        "--gt-stats-path",
        type=str,
        help="path to ground truth skeleton statistics",
        default="",
    )
    parser.add_argument(
        "-c",
        "--num-chunk",
        type=int,
        help="number of chunks to process the volume",
        default=1,
    )
    return parser.parse_args()


if __name__ == "__main__":
    # python test_axonEM.py -s db/30um_human/axon_release/gt_16nm.h5 -g db/30um_human/axon_release/gt_16nm_skel_stats.p -c 1
    args = get_arguments()
    # compute erl
    test_AxonEM(args.gt_stats_path, args.seg_path, args.num_chunk)
