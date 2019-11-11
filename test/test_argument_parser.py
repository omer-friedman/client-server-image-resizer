import argparse


class ArgumentParser:
    parser = argparse.ArgumentParser(description='Image properties')
    parser.add_argument('N', metavar='N', type=int, help='Number of instances')
    parser.add_argument('M', metavar='M', type=int, help='Delay to start next proccess')
    parser.add_argument('video_path', metavar='video_path', type=str, help='Local path to video')
    parser.add_argument('--max_gpu', metavar='percent(1-100)', type=str, help='Maximum gpu usage while processing video.')

    args = parser.parse_args()
