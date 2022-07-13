#!/usr/bin/python3

import os
import sys
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def get_bug_list(directory):
    files = {}

    for file in os.listdir(directory):
        root, ext = os.path.splitext(file)
        root = '-'.join(root.split('-')[:-1]) # remove random hash

        if ext not in ['.smt2', '.output']:
            continue

        if root not in files:
            files[root] = [None, None]

        idx = 0 if ext == '.smt2' else 1
        files[root][idx] = os.path.join(directory, file)

    return [tuple(files[root]) for root in files.keys()]


def parse_output_file(out_file):
    with open(out_file, 'r') as file:
        lines = file.readlines()
        line_nr = 0

        cmd = lines[line_nr][len('command: '):]
        line_nr += 1

        while not lines[line_nr].startswith('stderr:'):
            cmd += lines[line_nr]
            line_nr += 1

        stderr = lines[line_nr][len('stderr: '):]
        line_nr += 1

        if stderr == '\n':
            stderr = ''

        while not lines[line_nr].startswith('stdout:'):
            stderr += lines[line_nr]
            line_nr += 1

        stdout = lines[line_nr][len('stdout: '):] 
        stdout += ''.join(lines[(line_nr+1):])
        
        return cmd.strip(), stdout.strip(), stderr.strip()


def notify(client, in_file, out_file):
    if not in_file or not out_file:
        return False
    
    cmd, stdout, stderr = parse_output_file(out_file)
    message = 'cmd:' + '```' + cmd + ' ' +  os.path.basename(in_file) + '```' + '\n'
    if stdout:
        message += 'stdout:' + '\n' + '```' + stdout + '```'
    if stderr:
        message += 'stderr:' + '\n' + '```' + stderr + '```' + '\n'

    try:
        result = client.files_upload(
            channels=os.getenv('SLACK_CHANNEL_ID'),
            initial_comment=message,
            file=in_file,
        )
        logging.info(result)
        return True

    except SlackApiError as e:
        logging.error("Error uploading file: {}".format(e))
        return False


def main():
    client = WebClient(token=os.getenv('SLACK_TOKEN'))
    bugs = get_bug_list(sys.argv[1])

    for in_file, out_file in bugs:
        if notify(client, in_file, out_file):
            os.remove(in_file)
            os.remove(out_file)


if __name__ == '__main__':
    main()
