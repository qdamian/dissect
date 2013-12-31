set -e
hg clone http://bitbucket.org/birkenfeld/sphinx-contrib/
cd sphinx-contrib/autorun
python setup.py install
cd -
echo "extensions.append('sphinxcontrib.autorun')" >> ./doc/source/conf.py
