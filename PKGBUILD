# Maintainer: G_cat101 <gcatmail2@gmail.com>
pkgname=wfetch
pkgver=1.0
pkgrel=1
pkgdesc="Neofetch/pfetch, but for weather"
arch=('x86_64')
url="https://github.com/Gcat101/Wfetch.git"
license=('GPL-3.0')
groups=()
depends=(git python python-pip)
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
  echo "1.0.$(git ls-remote git://github.com/gcat101/wfetch.git | grep refs/heads/master | cut -f 1)"
}

package() {
  cd wfetch
  ./install.sh
}
