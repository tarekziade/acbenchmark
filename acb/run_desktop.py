import os
import argparse


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


host_ip = "127.0.0.1"
# firefox_args += '--firefox.geckoProfiler true --firefox.geckoProfilerParams.interval 10   --firefox.geckoProfilerParams.features "js,stackwalk,leaf" --firefox.geckoProfilerParams.threads "GeckoMain,Compositor,ssl,socket,url,bhm,dns" '
# WebPageReplay
# firefox_args += '--firefox.preference network.dns.forceResolve:' + host_ip + ' --firefox.acceptInsecureCerts true '

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
    parser.add_argument("--iterations", default=20, help="Number of iterations")
    parser.add_argument("--name", default="tinap", help="Name of the test")
    args = parser.parse_args()

    for line in open(SITES_TXT):
        url = line.strip()
        print("Loading url: " + url + " with browsertime")

        options = {
            "url": url,
            "iterations": args.iterations,
            "result_dir": result_dir(url, args.name),
        }
        cmd = " ".join(_CMD) % options
        print("\ncommand " + cmd)
        os.system(cmd)


if __name__ == "__main__":
    main()
