# HTTPie Desktop for Fedora/RHEL

[![⚡️ Powered By: Copr](https://img.shields.io/badge/⚡️_Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
![📦 Architectures](https://img.shields.io/badge/📦_Architectures-x86__64_|_aarch64-blue?style=flat-square)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/anifyuliansyah/httpie-desktop/package/httpie-desktop/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/anifyuliansyah/httpie-desktop/package/httpie-desktop/)

Unofficial RPM packaging for [HTTPie Desktop](https://httpie.io/desktop) - a modern, user-friendly HTTP client with a beautiful interface for testing and debugging APIs.

> **⚠️ Important Notice**  
> HTTPie Desktop is **proprietary freeware** software, not open source. This repository only provides RPM packaging for convenient installation on Fedora and RHEL-based systems. The application itself is developed and owned by HTTPie, Inc.

## Installation

### Via Copr (Recommended)

```bash
# Enable the Copr repository
sudo dnf copr enable anifyuliansyah/httpie-desktop

# Install HTTPie Desktop
sudo dnf install httpie-desktop
```

### Supported Distributions

- Fedora 40, 41, 42
- EPEL 9 (for RHEL 9, CentOS Stream 9, Rocky Linux 9, AlmaLinux 9)
- EPEL 10 (for RHEL 10, CentOS Stream 10, Rocky Linux 10, AlmaLinux 10)

### Supported Architectures

- x86_64 (Intel/AMD 64-bit)
- aarch64 (ARM 64-bit)

## Usage

Launch from application menu or run from terminal:

```bash
httpie-desktop
```

## Updates

Updates are delivered through your package manager:

```bash
sudo dnf update httpie-desktop
```

HTTPie Desktop may show update notifications. Since updates are managed through DNF, you can safely ignore these notifications. Your package will be updated through the Copr repository when new versions are released.

## Building Locally

If you want to build the RPM yourself:

### Prerequisites

```bash
sudo dnf install rpmdevtools rpmlint spectool
```

### Build Process

```bash
# Clone this repository
git clone https://github.com/Anifyuli/httpie-desktop-rpm.git
cd httpie-desktop-rpm

# Download sources
spectool -g -R httpie-desktop.spec

# Build SRPM
rpmbuild -bs httpie-desktop.spec \
    --define "_sourcedir $(pwd)" \
    --define "_specdir $(pwd)" \
    --define "_builddir $(pwd)" \
    --define "_srcrpmdir $(pwd)" \
    --define "_rpmdir $(pwd)"

# Build RPM
rpmbuild -bb httpie-desktop.spec \
    --define "_sourcedir $(pwd)" \
    --define "_specdir $(pwd)" \
    --define "_builddir $(pwd)" \
    --define "_srcrpmdir $(pwd)" \
    --define "_rpmdir $(pwd)"
```

### Using Mock (Clean Build)

```bash
# Build with Mock for Fedora 40
mock -r fedora-40-x86_64 --rebuild httpie-desktop-*.src.rpm
```

## Uninstallation

```bash
sudo dnf remove httpie-desktop
```

Configuration files in `~/.config/HTTPie/` will be preserved. To remove them:

```bash
rm -rf ~/.config/HTTPie/
```

## Package Details

### What This Package Does

This package:
- ✅ Extracts the official HTTPie Desktop AppImage
- ✅ Installs files to `/usr/lib64/httpie-desktop/`
- ✅ Creates desktop entry and installs icons
- ✅ Provides a launcher script at `/usr/bin/httpie-desktop`
- ✅ Integrates with system package management

### Source

The package is built from official AppImage releases:
- x86_64: `HTTPie-{version}.AppImage`
- aarch64: `HTTPie-{version}-arm64.AppImage`

Source: https://github.com/httpie/desktop/releases

## License

**Application License:** Proprietary (Freeware)  
HTTPie Desktop is free to use for personal and commercial purposes but is not open source software. See https://httpie.io/terms for details.

**Packaging License:** MIT  
The RPM spec file and packaging scripts in this repository are licensed under the MIT License.

## Acknowledgments

- **HTTPie, Inc.** - for creating HTTPie Desktop
- **Arch Linux httpie-desktop-bin package** - for the packaging approach inspiration

## Disclaimer

This is an **unofficial, community-maintained** RPM package. It is not affiliated with, endorsed by, or supported by HTTPie, Inc.

For official support and bug reports about the application itself, please visit:
- Official Website: https://httpie.io
- GitHub: https://github.com/httpie/desktop

For issues related to this RPM packaging, please open an issue on this repository.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

### Reporting Issues

When reporting issues, please specify:
- Your distribution and version (e.g., Fedora 40)
- Architecture (x86_64 or aarch64)
- HTTPie Desktop version
- Steps to reproduce the issue

## Related Projects

- [HTTPie CLI](https://github.com/httpie/cli) - Command-line HTTP client (open source)
- [HTTPie Desktop Official](https://httpie.io/desktop) - Official desktop application
- [Flatpak version](https://flathub.org/apps/io.httpie.Httpie) - Official Flatpak package

## Contact

- Repository Maintainer: [@Anifyuli](https://github.com/Anifyuli)
- Copr Repository: https://copr.fedorainfracloud.org/coprs/anifyuliansyah/httpie-desktop/

---

**Note:** HTTPie Desktop requires network access for API testing. The application may collect usage data. Please review HTTPie's privacy policy at https://httpie.io/privacy
