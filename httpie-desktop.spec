# RPM spec file for HTTPie Desktop (based on Arch PKGBUILD approach)
# Maintainer: Your Name <you@example.com>

Name:           httpie-desktop
Version:        2025.2.0
Release:        1%{?dist}
Summary:        Modern, user-friendly HTTP client for the desktop
License:        MIT
URL:            https://httpie.io
Source0:        https://github.com/httpie/desktop/releases/download/v%{version}/HTTPie-%{version}.AppImage

BuildArch:      x86_64
ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
Requires:       gtk3 alsa-lib nss fuse-libs

%description
HTTPie Desktop is a modern, user-friendly HTTP client with a beautiful interface
for testing and debugging APIs, powered by the same team behind the popular
HTTPie CLI tool. This package repackages the official AppImage release into
an RPM for convenient installation on Fedora and RHEL-based systems.

%prep
cp %{SOURCE0} HTTPie.AppImage
chmod +x HTTPie.AppImage

# Extract AppImage contents
./HTTPie.AppImage --appimage-extract > /dev/null
mv squashfs-root %{name}-%{version}

# Fix desktop file Exec path
sed -i -E "s|Exec=AppRun|Exec=/usr/bin/httpie-desktop|" %{name}-%{version}/httpie.desktop

%build
# Fix permissions like Arch PKGBUILD does
# Remove execute bit from all files, then add read+execute for directories only
cd %{name}-%{version}
chmod -R a-x+rX usr/ locales/ resources/

# Now explicitly make necessary binaries executable
chmod 755 AppRun
chmod 755 httpie
chmod 755 chrome-crashpad_handler 2>/dev/null || true
find . -name "*.so*" -exec chmod 755 {} \;

%install
# Install to /usr/lib/httpie-desktop (like Arch does)
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -R %{name}-%{version}/* %{buildroot}%{_libdir}/%{name}/

# Remove unnecessary files
rm -rf %{buildroot}%{_libdir}/%{name}/usr
rm -f %{buildroot}%{_libdir}/%{name}/httpie.png

# Install icons from extracted AppImage
for size in 16x16 32x32 64x64 128x128 256x256 512x512 1024x1024; do
    if [ -f %{name}-%{version}/usr/share/icons/hicolor/${size}/apps/httpie.png ]; then
        mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
        cp %{name}-%{version}/usr/share/icons/hicolor/${size}/apps/httpie.png \
           %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
    fi
done

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
cp %{name}-%{version}/httpie.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install licenses
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
cp %{name}-%{version}/LICENSE.electron.txt %{buildroot}%{_datadir}/licenses/%{name}/ 2>/dev/null || true
cp %{name}-%{version}/LICENSES.chromium.html %{buildroot}%{_datadir}/licenses/%{name}/ 2>/dev/null || true

# Create launcher script
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<'EOF'
#!/usr/bin/bash
# HTTPie Desktop launcher

INSTALL_DIR="/usr/lib64/httpie-desktop"

# Change to install directory
cd "$INSTALL_DIR" || cd "/usr/lib/httpie-desktop" || exit 1

# Set environment
export APPDIR="$INSTALL_DIR"
export LD_LIBRARY_PATH="$INSTALL_DIR/lib:${LD_LIBRARY_PATH}"

# Execute the main binary
exec "$INSTALL_DIR/httpie" --no-sandbox "$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

%files
%license %{_datadir}/licenses/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/httpie.png
%{_libdir}/%{name}/

%post
update-desktop-database %{_datadir}/applications &> /dev/null || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor &> /dev/null || :

%postun
update-desktop-database %{_datadir}/applications &> /dev/null || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor &> /dev/null || :

%changelog
* Sat Oct 25 2025 Your Name <you@example.com> - 2025.2.0-1
- Adopted Arch PKGBUILD approach for permission handling
- Install to /usr/lib/httpie-desktop
- Direct binary execution without AppRun
- First stable RPM release
