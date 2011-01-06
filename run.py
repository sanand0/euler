import os, os.path, stat, time, glob, operator, logging
from django.utils import simplejson as json

logging.basicConfig(level=logging.INFO)

PATH        = os.path.dirname(__file__)
STATS_FILE  = os.path.join(PATH, 'stats.txt')
TEMPLATE    = os.path.join(PATH, 'template.html')
HTML_FILE   = 'D:/html/a/euler.html'
stats       = json.loads(open(STATS_FILE).read())
stats_mtime = os.stat(STATS_FILE)[stat.ST_MTIME]

for file in glob.glob(os.path.join(PATH, '0*.py')):
    key = os.path.basename(file)
    if not stats.has_key(key) or os.stat(file)[stat.ST_MTIME] > stats_mtime:
        logging.info(file)
        t0 = time.time()
        ans = os.popen(file).read().strip()
        interval = int(1000*(time.time() - t0))
        if ans:
            logging.info('Answer: %s (%d ms)' % (ans, interval))
            stats[key] = { 'ans': ans, 'time': interval, 'num': str(int(key.replace('.py',''))) }

open(STATS_FILE, 'w').write(json.dumps(stats))

table = ''.join('<tr><td class="numbers"><a target="_blank" href="http://projecteuler.net/index.php?section=problems&id=' + stats[x]['num'] + '">' + stats[x]['num'] + '</a>' +
                '</td><td class="numbers">' + str(stats[x]['ans']) +
                '</td><td class="numbers">' + (stats[x]['time'] > 10000 and '<span class="slow">' or '') + str(stats[x]['time']) + (stats[x]['time'] > 10000 and '</span>' or '') +
                '</td><td><a href="#" class="show">Show solution</a><pre>' + open(os.path.join(PATH, x)).read() + '</pre>' +
                '</td></tr>' for x in sorted(stats.keys()))

module = ''.join('<br><a href="#" class="show">' + x + '</a><pre>' + os.popen(os.path.join(PATH, x)).read() + '</pre>' for x in ('prime.py', 'combinatorics.py'))

print open(TEMPLATE).read() % locals()
