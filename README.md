# HTTPie Desktop for Fedora/RHEL

RPM packaging for HTTPie Desktop, repackaged from official AppImage.

## Installation
```bash
# Enable Copr repository
sudo dnf copr enable anifyuliansyah/httpie-desktop

# Install
sudo dnf install httpie-desktop
```

## Building Locally
```bash
# Install dependencies
sudo dnf install rpmdevtools rpmlint spectool

# Download sources
spectool -g -R httpie-desktop.spec

# Build SRPM
rpmbuild -bs httpie-desktop.spec

# Build RPM
rpmbuild -bb httpie-desktop.spec
```
