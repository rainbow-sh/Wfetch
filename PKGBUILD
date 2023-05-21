# Maintainer: SQL-ENWiki <sqlatenwiki@gmail.com>
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
source=("git+$url")
noextract=()
md5sums=('SKIP')

pkgver() {
  echo "1.0.$(git ls-remote https://github.com/rainbow-sh/Wfetch.git | grep refs/heads/master | cut -f 1)"
}

package() {
  cd ./Wfetch
  install -DT wfetch/wfetch.py "$pkgdir/usr/local/bin/wfetch"
  install -Dd wfetch/icons "$pkgdir/opt/wfetch"
}
