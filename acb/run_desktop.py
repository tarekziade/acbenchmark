import os
import argparse
import json

_REP = (
    ("http://", ""),
    ("https://", ""),
    ("/", "_"),
    ("?", "_"),
    ("&", "_"),
    (":", ";"),
    ("\n", " "),
    ("\r", ""),
)


def result_dir(url, test_name):
    for orig, repl in _REP:
        url = url.replace(orig, repl)
    return os.path.join("browsertime-results", url, test_name)

# find out the local host ip automatically
# run "co servers" prior to running the script.
# I guess we can provide them using a list of commands, one per coserver/


HERE = os.path.dirname(__file__)

_CMD = [
    "browsertime",
    "--pageCompleteWaitTime",
    "8000",
    "--browsertime.url",
    '"%(url)s"',
    os.path.join(HERE, "preload.js"),
    "-n",
    "%(iterations)d",
    "--resultDir",
    '"%(result_dir)s"',
    "--browser",
    "firefox",
]

SITES_TXT = os.path.join(HERE, "sites.txt")


def main():
    parser = argparse.ArgumentParser(description="acbenchmark")
    parser.add_argument("--iterations", type=int, default=20, help="Number of iterations")
    parser.add_argument("--name", default="tinap", help="Name of the test")
    parser.add_argument("--prefs", default=None, help="prefs file")
    args = parser.parse_args()

    if os.path.exists(args.prefs):
        with open(args.prefs) as f:
            prefs = json.loads(f.read())
        for key, value in prefs.items():
            _CMD.append("--%s" % key)
            _CMD.append(str(value))

    for line in open(SITES_TXT):
        url = line.strip()
        print("Loading url: " + url + " with browsertime")

        options = {
            "url": url,
            "iterations": args.iterations,
            "result_dir": result_dir(url, args.name),
            "host_ip": "127.0.0.1"
        }
        cmd = " ".join(_CMD) % options
        print("\ncommand " + cmd)
        os.system(cmd)


if __name__ == "__main__":
    main()
