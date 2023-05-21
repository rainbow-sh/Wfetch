# Maintainer: SQL-ENWiki <sqlatenwiki@gmail.com>
# Maintainer: G_cat101 <gcatmail2@gmail.com>

pkgname=wfetch-git
pkgver=1.0.3feafcd1142441a7dcbe80b0d41e0a547a4672f9
pkgrel=1
pkgdesc="Neofetch/pfetch, but for weather"
arch=('x86_64')
url="https://github.com/rainbow-sh/Wfetch.git"
license=('GPL-3.0')
groups=()
depends=(git python python-pip python-fire python-requests )
makedepends=()
optdepends=()
provides=(wfetch)
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("git+$url" "https://files.pythonhosted.org/packages/source/p/pyowm/pyowm-3.3.0.tar.gz")
noextract=()
sha256sums=('SKIP'
            '8196f77c91eac680676ed5ee484aae8a165408055e3e2b28025cbf60b8681e03')

pkgver() {
  echo "1.0.$(git ls-remote https://github.com/rainbow-sh/Wfetch.git | grep refs/heads/master | cut -f 1)"
}

package() {
  cd ./Wfetch
  install -DT wfetch/wfetch.py "$pkgdir/usr/local/bin/wfetch"
  install -Dd wfetch/icons "$pkgdir/opt/wfetch"
}
