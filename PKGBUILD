# Maintainer: SQL-ENWiki <sqlatenwiki@gmail.com>
# Maintainer: G_cat101 <gcatmail2@gmail.com>

pkgname=wfetch-git
pkgver=1.0
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
  install -Dd wfetch/icons/day "$pkgdir/opt/wfetch/day"
  cp wfetch/icons/day/*.txt "$pkgdir/opt/wfetch/day"
  install -Dd wfetch/icons/neutral "$pkgdir/opt/wfetch/neutral"
  cp wfetch/icons/neutral/* "$pkgdir/opt/wfetch/neutral"
  install -Dd wfetch/icons/night "$pkgdir/opt/wfetch/night"
  cp wfetch/icons/night/* "$pkgdir/opt/wfetch/night"
  install -DT wfetch/icons/unknown.txt "$pkgdir/opt/wfetch/unknown.txt"
}
