import os

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
_ITERATIONS = "20"
experiment_name = "test_tinap"

browsertime_path = "node browsertime.js "
firefox_args = " --browser firefox"
# firefox_args += '--firefox.geckoProfiler true --firefox.geckoProfilerParams.interval 10   --firefox.geckoProfilerParams.features "js,stackwalk,leaf" --firefox.geckoProfilerParams.threads "GeckoMain,Compositor,ssl,socket,url,bhm,dns" '

# WebPageReplay
# firefox_args += '--firefox.preference network.dns.forceResolve:' + host_ip + ' --firefox.acceptInsecureCerts true '

_CMD = "node browsertime.js"
_ARGS = [
    "--pageCompleteWaitTime",
    "8000",
    "--browsertime.url",
    '"%(url)s"',
    "preload.js",
    "-n",
    "%(iterations)d",
    "--resultDir",
    '"%(result_dir)s"',
    "--browser",
    "firefox",
]

for line in open("sites.txt"):
    url = line.strip()
    print("Loading url: " + url + " with browsertime")

    options = {
        "url": url,
        "iterations": _ITERATIONS,
        "result_dir": result_dir(url, "test_tinap"),
    }
    cmd = _CMD + " ".join(_ARGS) % options
    print("\ncommand " + cmd)
    os.system(cmd)
