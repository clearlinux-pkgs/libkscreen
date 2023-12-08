#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : libkscreen
Version  : 5.27.10
Release  : 91
URL      : https://download.kde.org/stable/plasma/5.27.10/libkscreen-5.27.10.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.10/libkscreen-5.27.10.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.10/libkscreen-5.27.10.tar.xz.sig
Summary  : Qt Based library to manage screens with backends (xrandr, whatevercomesnext)
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1
Requires: libkscreen-bin = %{version}-%{release}
Requires: libkscreen-data = %{version}-%{release}
Requires: libkscreen-lib = %{version}-%{release}
Requires: libkscreen-license = %{version}-%{release}
Requires: libkscreen-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules wayland
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kwayland-dev
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# libkscreen
libkscreen is the screen management library for KDE Plasma Workspaces. Its primary consumer is the KDE screen management application KScreen.

%package bin
Summary: bin components for the libkscreen package.
Group: Binaries
Requires: libkscreen-data = %{version}-%{release}
Requires: libkscreen-license = %{version}-%{release}
Requires: libkscreen-services = %{version}-%{release}

%description bin
bin components for the libkscreen package.


%package data
Summary: data components for the libkscreen package.
Group: Data

%description data
data components for the libkscreen package.


%package dev
Summary: dev components for the libkscreen package.
Group: Development
Requires: libkscreen-lib = %{version}-%{release}
Requires: libkscreen-bin = %{version}-%{release}
Requires: libkscreen-data = %{version}-%{release}
Provides: libkscreen-devel = %{version}-%{release}
Requires: libkscreen = %{version}-%{release}

%description dev
dev components for the libkscreen package.


%package lib
Summary: lib components for the libkscreen package.
Group: Libraries
Requires: libkscreen-data = %{version}-%{release}
Requires: libkscreen-license = %{version}-%{release}

%description lib
lib components for the libkscreen package.


%package license
Summary: license components for the libkscreen package.
Group: Default

%description license
license components for the libkscreen package.


%package services
Summary: services components for the libkscreen package.
Group: Systemd services
Requires: systemd

%description services
services components for the libkscreen package.


%prep
%setup -q -n libkscreen-5.27.10
cd %{_builddir}/libkscreen-5.27.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702018563
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702018563
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkscreen
cp %{_builddir}/libkscreen-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkscreen/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libkscreen-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libkscreen/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/libkscreen-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkscreen/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/libkscreen-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libkscreen/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/libkscreen-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/libkscreen/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/libkscreen-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libkscreen/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/libkscreen-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/libkscreen/7d9831e05094ce723947d729c2a46a09d6e90275 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf5/kscreen_backend_launcher
/usr/lib64/libexec/kf5/kscreen_backend_launcher

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kscreen-doctor
/usr/bin/kscreen-doctor

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.kde.kscreen.service
/usr/share/locale/ca/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/de/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/es/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/id/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/it/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libkscreen5_qt.qm
/usr/share/qlogging-categories5/libkscreen.categories
/usr/share/zsh/site-functions/_kscreen-doctor

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KScreen/KScreen/Config
/usr/include/KF5/KScreen/KScreen/ConfigMonitor
/usr/include/KF5/KScreen/KScreen/ConfigOperation
/usr/include/KF5/KScreen/KScreen/EDID
/usr/include/KF5/KScreen/KScreen/GetConfigOperation
/usr/include/KF5/KScreen/KScreen/Log
/usr/include/KF5/KScreen/KScreen/Mode
/usr/include/KF5/KScreen/KScreen/Output
/usr/include/KF5/KScreen/KScreen/Screen
/usr/include/KF5/KScreen/KScreen/SetConfigOperation
/usr/include/KF5/KScreen/KScreen/Types
/usr/include/KF5/KScreen/KScreenDpms/Dpms
/usr/include/KF5/KScreen/kscreen/backendmanager_p.h
/usr/include/KF5/KScreen/kscreen/config.h
/usr/include/KF5/KScreen/kscreen/configmonitor.h
/usr/include/KF5/KScreen/kscreen/configoperation.h
/usr/include/KF5/KScreen/kscreen/edid.h
/usr/include/KF5/KScreen/kscreen/getconfigoperation.h
/usr/include/KF5/KScreen/kscreen/kscreen_export.h
/usr/include/KF5/KScreen/kscreen/log.h
/usr/include/KF5/KScreen/kscreen/mode.h
/usr/include/KF5/KScreen/kscreen/output.h
/usr/include/KF5/KScreen/kscreen/screen.h
/usr/include/KF5/KScreen/kscreen/setconfigoperation.h
/usr/include/KF5/KScreen/kscreen/types.h
/usr/include/KF5/KScreen/kscreendpms/dpms.h
/usr/include/KF5/KScreen/kscreendpms/kscreendpms_export.h
/usr/include/KF5/kscreen_version.h
/usr/lib64/cmake/KF5Screen/KF5ScreenConfig.cmake
/usr/lib64/cmake/KF5Screen/KF5ScreenConfigVersion.cmake
/usr/lib64/cmake/KF5Screen/KF5ScreenTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Screen/KF5ScreenTargets.cmake
/usr/lib64/libKF5Screen.so
/usr/lib64/libKF5ScreenDpms.so
/usr/lib64/pkgconfig/kscreen2.pc
/usr/lib64/qt5/mkspecs/modules/qt_KScreen.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Screen.so.5.27.10
/V3/usr/lib64/libKF5ScreenDpms.so.5.27.10
/V3/usr/lib64/qt5/plugins/kf5/kscreen/KSC_Fake.so
/V3/usr/lib64/qt5/plugins/kf5/kscreen/KSC_KWayland.so
/V3/usr/lib64/qt5/plugins/kf5/kscreen/KSC_QScreen.so
/V3/usr/lib64/qt5/plugins/kf5/kscreen/KSC_XRandR.so
/V3/usr/lib64/qt5/plugins/kf5/kscreen/KSC_XRandR11.so
/usr/lib64/libKF5Screen.so.5.27.10
/usr/lib64/libKF5Screen.so.8
/usr/lib64/libKF5ScreenDpms.so.5.27.10
/usr/lib64/libKF5ScreenDpms.so.8
/usr/lib64/qt5/plugins/kf5/kscreen/KSC_Fake.so
/usr/lib64/qt5/plugins/kf5/kscreen/KSC_KWayland.so
/usr/lib64/qt5/plugins/kf5/kscreen/KSC_QScreen.so
/usr/lib64/qt5/plugins/kf5/kscreen/KSC_XRandR.so
/usr/lib64/qt5/plugins/kf5/kscreen/KSC_XRandR11.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkscreen/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/libkscreen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkscreen/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/libkscreen/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/libkscreen/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kscreen.service
