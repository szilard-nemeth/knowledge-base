#!/usr/bin/env python3
"""Unpause all the paused jobs on the virtual clusters
which jobs api is in the virtual cluster endpoint json file."""

import json
import os
import subprocess
from copy import copy
from datetime import datetime
from cde_cli.cde_cli_processor import CdeCliJsonParser

list_cmd = ["cde", "job", "list"]
# cde job list --vcluster-endpoint https://d94tftqj.cde-64m2285t.dex-priv.xcu2-8y8x.dev.cldr.work/dex/api/v1

run_cmd = ["cde", "job", "run"]
# cde job run --vcluster-endpoint https://d94tftqj.cde-64m2285t.dex-priv.xcu2-8y8x.dev.cldr.work/dex/api/v1

# parse json, run only airflow jobs

def list_jobs(vc_ep: str):
    """Run the cde list CLI command for a given vc endpoint."""
    env = os.environ

    # cde cli should use the configuration from the ~/.cde/credentials
    # with the cdp access key if the CDE_USER is set in the env
    # it prompts to authenticate with it.
    try:
        env.pop("CDE_USER")
    except KeyError:
        pass

    cmd = copy(list_cmd)
    cmd.append("--vcluster-endpoint")
    cmd.append(vc_ep)
    print(" ".join(cmd))
    cde_cli_parser = CdeCliJsonParser(cmd)
    job_names = cde_cli_parser.parse_job_names()
    return job_names


def run_job(vc_ep: str, job_name: str):
    """Run the cde run CLI command for a given vc endpoint."""
    env = os.environ

    # cde cli should use the configuration from the ~/.cde/credentials
    # with the cdp access key if the CDE_USER is set in the env
    # it prompts to authenticate with it.
    try:
        env.pop("CDE_USER")
    except KeyError:
        pass

    cmd = copy(run_cmd)
    cmd.append("--name")
    cmd.append(job_name)
    cmd.append("--vcluster-endpoint")
    cmd.append(vc_ep)
    print(" ".join(cmd))

    cde_cli_parser = CdeCliJsonParser(cmd)
    cde_cli_parser.run()


def load_vc_ep_list(cluster_id: str):
    """Load the virtual cluster endpoint list from the local config file."""
    vc_ep_filename = os.path.join(cluster_id, "vc_ep.json")
    with open(vc_ep_filename, encoding="utf-8") as ep_file:
        return json.load(ep_file)


def main():
    """Main entrypoint."""
    cluster_id = os.environ["CLUSTER_ID"]  # fail early if missing

    for vc_ep in load_vc_ep_list(cluster_id):
        job_names = list_jobs(vc_ep)
        print("Running jobs: {}".format(job_names))
        for job in job_names:
            run_job(vc_ep, job)

    print(datetime.now())


if __name__ == "__main__":
    print(os.environ["PATH"])
    main()
