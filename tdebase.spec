%bcond clang 1
%bcond esound 0
%bcond gamin 1
%bcond tsak 1
%bcond tdehwlib 1
%bcond xrandr 1
%bcond xtest 1
%bcond openexr 1
%bcond xscreensaver 1
%bcond libart 1
%bcond libconfig 1
%bcond kbdledsync 1
%bcond tderandrtray 1
%bcond elficon 0
%bcond ssh 1
%bcond xtst 1
%bcond systemd 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tdebase

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		%{tde_version}
Release:		%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Trinity Base Programs
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

License:		GPLv2+

#Vendor:			Trinity Desktop
#Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:			/opt/trinity

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

Source2:		pamd.kdm-trinity.omv
Source3:		pamd.kdm-trinity-np.omv
Source4:		pamd.kcheckpass-trinity.omv
Source5:		pamd.kscreensaver-trinity.omv

Obsoletes:	trinity-kdebase < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebase = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebase-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdebase-extras = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase = %{?epoch:%{epoch}:}%{version}-%{release}

BuildSystem:  cmake

BuildOption:  -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:  -DCMAKE_SKIP_RPATH=OFF
BuildOption:  -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:  -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:  -DCMAKE_INSTALL_RPATH="%{prefix}/%{_lib}"
BuildOption:  -DBIN_INSTALL_DIR="%{prefix}/bin"
BuildOption:  -DCONFIG_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:  -DINCLUDE_INSTALL_DIR="%{prefix}/include/tde"
BuildOption:  -DLIB_INSTALL_DIR="%{prefix}/%{_lib}"
BuildOption:  -DSHARE_INSTALL_PREFIX="%{prefix}/share"
BuildOption:  -DCONFIG_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:  -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:  -DXDG_MENU_INSTALL_DIR="%{_sysconfdir}/xdg/menus"
BuildOption:  -DWITH_ALL_OPTIONS=ON -DWITH_SASL=ON -DWITH_LDAP=ON
BuildOption:  -DWITH_SAMBA=ON -DWITH_XCOMPOSITE=ON -DWITH_XCURSOR=ON
BuildOption:  -DWITH_XFIXES=ON -DWITH_XRENDER=ON -DWITH_PCRE=ON
BuildOption:  -DWITH_OPENGL=ON -DWITH_LIBUSB=ON -DWITH_LIBRAW1394=ON
BuildOption:  -DWITH_SUDO_TDESU_BACKEND=ON
BuildOption:  -DWITH_SUDO_KONSOLE_SUPER_USER_COMMAND=ON
BuildOption:  -DWITH_PAM=ON -DWITH_SHADOW=OFF -DWITH_XDMCP=ON
BuildOption:  -DWITH_XINERAMA=ON -DWITH_ARTS=ON -DWITH_I8K=ON
BuildOption:  -DWITH_SENSORS=ON -DWITH_UPOWER=ON
BuildOption:  -DBUILD_ALL=ON 
BuildOption:  -DKCHECKPASS_PAM_SERVICE="kcheckpass-trinity"
BuildOption:  -DTDM_PAM_SERVICE="tdm-trinity"
BuildOption:  -DTDESCREENSAVER_PAM_SERVICE="tdescreensaver-trinity"
BuildOption:  -DHTDIG_SEARCH_BINARY="%{_bindir}/hldig"
BuildOption:  -DBUILD_TDM_SYSTEMD_UNIT_FILE="ON"
BuildOption:  -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:  -DWITH_OPENEXR=%{?!with_openexr:OFF}%{?with_openexr:ON}
BuildOption:  -DWITH_XRANDR=%{?!with_xrandr:OFF}%{?with_xrandr:ON}
BuildOption:  -DWITH_LIBCONFIG=%{?!with_libconfig:OFF}%{?with_libconfig:ON}
BuildOption:  -DWITH_XTEST=%{?!with_xtest:OFF}%{?with_xtest:ON}
BuildOption:  -DWITH_XSCREENSAVER=%{?!with_xscreensaver:OFF}%{?with_xscreensaver:ON}
BuildOption:  -DWITH_LIBART=%{?!with_libart:OFF}%{?with_libart:ON}
BuildOption:  -DWITH_ELFICON=%{!?with_elficon:OFF}%{?with_elficon:ON}
BuildOption:  -DWITH_TDEHWLIB=%{?!with_tdehwlib:OFF}%{?with_tdehwlib:ON}
BuildOption:  -DBUILD_TDEKBDLEDSYNC=%{!?with_kbdledsync:OFF}%{?with_kbdledsync:ON}
BuildOption:  -DBUILD_TSAK=%{!?with_tsak:OFF}%{?with_tsak:ON}

# OpenMandriva
Requires:	distro-release-theme
%define tde_bg /usr/share/wallpapers/default.png

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	fdupes

# HTDIG support
BuildRequires:	htdig

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# AUDIOFILE support
BuildRequires:	audiofile-devel

# ALSA supportl
BuildRequires:  pkgconfig(alsa)

# RAW1394 support
BuildRequires:  pkgconfig(libraw1394)

# VORBIS support
BuildRequires:  pkgconfig(vorbis)

# GLIB2 support
BuildRequires:	pkgconfig(glib-2.0)

# PCRE support
BuildRequires:	pkgconfig(libpcreposix)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# SASL support
BuildRequires:  pkgconfig(libsasl2)

# PAM support
BuildRequires:	pkgconfig(pam)

# LIBUSB support
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libusb)

# ESOUND support
%{?with_esound:BuildRequires:	pkgconfig(esound)}

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENLDAP support
BuildRequires:  pkgconfig(ldap)

# SENSORS support
BuildRequires:	lm_sensors-devel

# TSAK support (requires libudev-devel)
#  On RHEL5, udev is built statically, so TSAK cannot build.
BuildRequires:	pkgconfig(udev)

# ACL support
BuildRequires:  pkgconfig(libacl)

# XINERAMA support
BuildRequires:  pkgconfig(xinerama)

# XCOMPOSITE support
BuildRequires:  pkgconfig(xcomposite)

# XCURSOR support
BuildRequires:  pkgconfig(xcursor)

# XRANDR support
%{?with_xrandr:BuildRequires:  pkgconfig(xrandr)}

# XRENDER support
BuildRequires:  pkgconfig(xrender)

BuildRequires:	pkgconfig(xft)

# OPENEXR support
%{?with_openexr:BuildRequires:  pkgconfig(OpenEXR)}

%if %{with xscreensaver}
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  xscreensaver
BuildRequires:  xscreensaver-base
%endif

# AVAHI support
BuildRequires:	libavahi-tqt-devel

# MESA support
BuildRequires:  pkgconfig(glu)

# DBUS support
BuildRequires:	libdbus-tqt-1-devel >= %{tde_epoch}:0.63
BuildRequires:	libdbus-1-tqt-devel >= %{tde_epoch}:0.9
Requires:		libdbus-tqt-1-0 >= %{tde_epoch}:0.63

# LIBART_LGPL support
%{?with_libart:BuildRequires:	pkgconfig(libart-2.0)}

# SAMBA support
BuildRequires:  pkgconfig(smbclient)

# IMAKE
BuildRequires:	imake

# XKB support
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbfile)

# XDMCP support
BuildRequires:  pkgconfig(xdmcp)

# XTST support
%{?with_xtst:BuildRequires:  pkgconfig(xtst)}

# XDAMAGE support
BuildRequires:  pkgconfig(xdamage)

# Requires 'usb.ids'
BuildRequires:	usbutils

# LIBFONTENC support
BuildRequires:  pkgconfig(fontenc)

# Other X11 stuff ...
BuildRequires:	x11-font-util
BuildRequires:	x11-proto-devel

# LIBCONFIG support
# Needed for "compton" stuff
%{?with_libconfig:BuildRequires:  pkgconfig(libconfig)}

# ELFICON support
%{?with_elficon:BuildRequires:		libr-devel >= 0.6.0}

# RPC support
BuildRequires:		pkgconfig(libtirpc)
BuildRequires:    pkgconfig(libnsl)

# ATTR support
BuildRequires: pkgconfig(libattr)

# LIBSSH support
%{?with_ssh:BuildRequires:	libssh-devel}

# tdebase is a metapackage that installs all sub-packages
Requires: %{name}-runtime-data-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdeio-pim-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kappfinder = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kate = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kwrite = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kcontrol = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdepasswd = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdeprint = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdm = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kfind = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-khelpcenter = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kicker = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klipper = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmenuedit = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konqueror = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konqueror-nsplugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konsole = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpager = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpersonalizer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksmserver = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksplash = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksysguard = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksysguardd = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktip = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-twin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-libtqt3-integration = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdeio-smb-plugin = %{?epoch:%{epoch}:}%{version}-%{release}
 
Requires:	trinity-arts >= %{tde_epoch}:1.5.10
Requires:	trinity-tdelibs >= %{tde_version}

%description
TDE (the Trinity Desktop Environment) is a powerful Open Source graphical
desktop environment for Unix workstations. It combines ease of use,
contemporary functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This metapackage includes the nucleus of TDE, namely the minimal package
set necessary to run TDE as a desktop environment. This includes the
window manager, taskbar, control center, a text editor, file manager,
web browser, X terminal emulator, and many other programs and components.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS README README.pam
%{prefix}/bin/tde_release_notes
%{prefix}/share/autostart/tde_release_notes.desktop
%{prefix}/share/applications/tde/tdehtml_userinterface.desktop

##########

%package devel
Summary:	%{summary} - Development files
Group:		Development/Libraries/Other
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
Requires:	trinity-tdelibs-devel >= %{tde_version}

Requires:	%{name}-bin-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kate-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kcontrol-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kdesktop-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kicker-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-konqueror-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ksplash-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ksysguard-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkonq-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdm-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-twin-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Provides:	trinity-kdebase-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This is a meta-package that installs all tdebase development packages.

Header files for developing applications using %{name}.
Install tdebase-devel if you want to develop or compile Konqueror,
Kate plugins or TWin styles.

%files devel
%defattr(-,root,root,-)
%{prefix}/share/cmake/*.cmake

##########

%package tdeio-pim-plugins
Summary:	PIM TDEIOslaves from %{name}
Group:		System/GUI/Other

Provides:	trinity-kdebase-pim-ioslaves = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdebase-pim-ioslaves < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-kio-pim-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-kio-pim-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdebase-kio-pim-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdebase-kio-pim-plugins < %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-pim-plugins
Protocol handlers (TDEIOslaves) for personal information management, including:
 * tdeio_ldap
 * tdeio_nntp
 * tdeio_pop3
 * tdeio_smtp

%files tdeio-pim-plugins
%defattr(-,root,root,-)
%{prefix}/%{_lib}/trinity/tdeio_ldap.la
%{prefix}/%{_lib}/trinity/tdeio_ldap.so
%{prefix}/%{_lib}/trinity/tdeio_nntp.la
%{prefix}/%{_lib}/trinity/tdeio_nntp.so
%{prefix}/%{_lib}/trinity/tdeio_pop3.la
%{prefix}/%{_lib}/trinity/tdeio_pop3.so
%{prefix}/%{_lib}/trinity/tdeio_smtp.la
%{prefix}/%{_lib}/trinity/tdeio_smtp.so
%{prefix}/share/services/ldap.protocol
%{prefix}/share/services/ldaps.protocol
%{prefix}/share/services/nntp.protocol
%{prefix}/share/services/nntps.protocol
%{prefix}/share/services/pop3.protocol
%{prefix}/share/services/pop3s.protocol
%{prefix}/share/services/smtp.protocol
%{prefix}/share/services/smtps.protocol

##########

%package runtime-data-common
Summary:	Shared common files for Trinity and KDE4
Group:		System/GUI/Other

Provides:	tdebase-runtime-data-common = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-runtime-data-common < %{?epoch:%{epoch}:}%{version}-%{release}

%description runtime-data-common
Shared common files for both Trinity and KDE4
Such as the desktop right-click-"Create New" list

%files runtime-data-common
%defattr(-,root,root,-)
%{prefix}/share/apps/kxkb/
%{prefix}/share/desktop-directories/
%{prefix}/share/icons/hicolor/*/apps/kxkb.png
%{prefix}/share/icons/hicolor/*/apps/knetattach.*
%{prefix}/share/icons/hicolor/*/apps/khotkeys.png
%{prefix}/share/icons/hicolor/*/apps/kmenuedit.png
%{prefix}/share/icons/hicolor/*/apps/ksplash.png
%{prefix}/share/locale/en_US/entry.desktop
%{prefix}/share/locale/l10n/*.desktop
%{prefix}/share/locale/l10n/*/entry.desktop
%{prefix}/share/locale/l10n/*/flag.png
%{prefix}/share/sounds/pop.wav
%{prefix}/share/templates/

##########

%package -n trinity-kappfinder
Summary:	Non-TDE application finder for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kappfinder
kappfinder searches your workstation for many common applications and
creates menu entries for them.

%files -n trinity-kappfinder
%defattr(-,root,root,-)
%{prefix}/bin/kappfinder
%{prefix}/share/applications/tde/kappfinder.desktop
%{prefix}/share/applnk/System/kappfinder.desktop
%{prefix}/share/apps/kappfinder
%{prefix}/share/icons/hicolor/*/apps/kappfinder.png
%{prefix}/share/man/man1/kappfinder.1*

##########

%package -n trinity-libkateinterfaces
Summary:	Common libraries used by kwrite and kate
Group:		System/GUI/Other

%description -n trinity-libkateinterfaces
This package contains the kateinterface library.

%files -n trinity-libkateinterfaces
%defattr(-,root,root,-)
%{prefix}/%{_lib}/libkateinterfaces.so.*

##########

%package -n trinity-kate
Summary:	Advanced text editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kwrite = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkateinterfaces = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kate
Kate is a multi document editor, based on a rewritten version of the kwrite
editing widget of TDE.

It is a multi-view editor that lets you view several instances of the same
document with all instances being synced, or view more files at the same
time for easy reference or simultaneous editing. The terminal emulation
and sidebar are docked windows that can be plugged out of the main window,
or replaced therein according to your preference.

Some random features:
* Editing of big files
* Extensible syntax highlighting
* Folding
* Dynamic word wrap
* Selectable encoding
* Filter command
* Global grep dialog

%files -n trinity-kate
%defattr(-,root,root,-)
%{prefix}/bin/kate
%{prefix}/%{_lib}/trinity/kate.la
%{prefix}/%{_lib}/trinity/kate.so
%{prefix}/%{_lib}/libkateutils.so.*
%{prefix}/%{_lib}/libtdeinit_kate.la
%{prefix}/%{_lib}/libtdeinit_kate.so
%{prefix}/share/applications/tde/kate.desktop
%{prefix}/share/apps/kate/
%{prefix}/share/apps/tdeconf_update/kate-2.4.upd
%config(noreplace) %{_sysconfdir}/trinity/katerc
%{prefix}/share/icons/hicolor/*/apps/kate.png
%{prefix}/share/icons/hicolor/*/apps/kate2.svgz
%{prefix}/share/servicetypes/kateplugin.desktop
%{prefix}/share/doc/tde/HTML/en/kate/
%{prefix}/share/man/man1/kate.1*

##########

%package -n trinity-kate-devel
Summary:	Development files for kate
Group:		Development/Libraries/Other
Requires:	trinity-kate = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kate-devel
This package contains the development files fare Kate.

%files -n trinity-kate-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/kate/
%{prefix}/%{_lib}/libkateutils.so
%{prefix}/%{_lib}/libkateutils.la
%{prefix}/%{_lib}/libkateinterfaces.so
%{prefix}/%{_lib}/libkateinterfaces.la

##########

%package -n trinity-kwrite
Summary:	Advanced text editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkateinterfaces = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kwrite
Kwrite is an advanced text editor for TDE.

%files -n trinity-kwrite
%defattr(-,root,root,-)
%{prefix}/bin/kwrite
%{prefix}/%{_lib}/trinity/kwrite.la
%{prefix}/%{_lib}/trinity/kwrite.so
%{prefix}/%{_lib}/libtdeinit_kwrite.la
%{prefix}/%{_lib}/libtdeinit_kwrite.so
%{prefix}/share/applications/tde/kwrite.desktop
%{prefix}/share/apps/kwrite/
%{prefix}/share/icons/hicolor/*/apps/kwrite.png
%{prefix}/share/icons/hicolor/*/apps/kwrite2.svgz
%{prefix}/share/doc/tde/HTML/en/kwrite/
%{prefix}/share/man/man1/kwrite.1*

##########

%package -n trinity-kcontrol
Summary:	Control center for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

# Requires 'usb.ids'
Requires:		usbutils
BuildRequires:	usbutils

%description -n trinity-kcontrol
The Trinity Control Center provides you with a centralized and convenient
way to configure all of your TDE settings.

It is made up of multiple modules. Each module is a separate application,
but the control center organizes all of these programs into a convenient
location.

In combination with udev KControl supports the advanced
configuration of Logitech mice, though the user must be a member of the
plugdev group.

%files -n trinity-kcontrol
%defattr(-,root,root,-)
%{prefix}/bin/kaccess
%{prefix}/bin/kcontrol
%{prefix}/bin/kdeinstallktheme
%{prefix}/bin/keditfiletype
%{prefix}/bin/tdefontinst
%{prefix}/bin/tdefontview
%{prefix}/bin/klocaldomainurifilterhelper
%{prefix}/bin/krdb
%{prefix}/%{_lib}/trinity/fontthumbnail.la
%{prefix}/%{_lib}/trinity/fontthumbnail.so
%{prefix}/%{_lib}/trinity/kaccess.la
%{prefix}/%{_lib}/trinity/kaccess.so
%{prefix}/%{_lib}/trinity/kcm_access.la
%{prefix}/%{_lib}/trinity/kcm_access.so
%{prefix}/%{_lib}/trinity/kcm_arts.la
%{prefix}/%{_lib}/trinity/kcm_arts.so
%{prefix}/%{_lib}/trinity/kcm_background.la
%{prefix}/%{_lib}/trinity/kcm_background.so
%{prefix}/%{_lib}/trinity/kcm_bell.la
%{prefix}/%{_lib}/trinity/kcm_bell.so
%{prefix}/%{_lib}/trinity/kcm_clock.la
%{prefix}/%{_lib}/trinity/kcm_clock.so
%{prefix}/%{_lib}/trinity/kcm_colors.la
%{prefix}/%{_lib}/trinity/kcm_colors.so
%{prefix}/%{_lib}/trinity/kcm_componentchooser.la
%{prefix}/%{_lib}/trinity/kcm_componentchooser.so
%{prefix}/%{_lib}/trinity/kcm_crypto.la
%{prefix}/%{_lib}/trinity/kcm_crypto.so
%{prefix}/%{_lib}/trinity/kcm_css.la
%{prefix}/%{_lib}/trinity/kcm_css.so
%{prefix}/%{_lib}/trinity/kcm_display.la
%{prefix}/%{_lib}/trinity/kcm_display.so
%{prefix}/%{_lib}/trinity/kcm_energy.la
%{prefix}/%{_lib}/trinity/kcm_energy.so
%{prefix}/%{_lib}/trinity/kcm_filetypes.la
%{prefix}/%{_lib}/trinity/kcm_filetypes.so
%{prefix}/%{_lib}/trinity/kcm_fontinst.la
%{prefix}/%{_lib}/trinity/kcm_fontinst.so
%{prefix}/%{_lib}/trinity/kcm_fonts.la
%{prefix}/%{_lib}/trinity/kcm_fonts.so
%if %{with tdehwlib}
%{prefix}/%{_lib}/trinity/kcm_hwmanager.la
%{prefix}/%{_lib}/trinity/kcm_hwmanager.so
%endif
%{prefix}/%{_lib}/trinity/kcm_icons.la
%{prefix}/%{_lib}/trinity/kcm_icons.so
%{prefix}/%{_lib}/trinity/kcm_info.la
%{prefix}/%{_lib}/trinity/kcm_info.so
%{prefix}/%{_lib}/trinity/kcm_input.la
%{prefix}/%{_lib}/trinity/kcm_input.so
%{prefix}/%{_lib}/trinity/kcm_joystick.la
%{prefix}/%{_lib}/trinity/kcm_joystick.so
%{prefix}/%{_lib}/trinity/kcm_kded.la
%{prefix}/%{_lib}/trinity/kcm_kded.so
%{prefix}/%{_lib}/trinity/kcm_tdm.la
%{prefix}/%{_lib}/trinity/kcm_tdm.so
%{prefix}/%{_lib}/trinity/kcm_tdednssd.so
%{prefix}/%{_lib}/trinity/kcm_tdednssd.la
%{prefix}/%{_lib}/trinity/kcm_keys.la
%{prefix}/%{_lib}/trinity/kcm_keys.so
%{prefix}/%{_lib}/trinity/kcm_kicker.la
%{prefix}/%{_lib}/trinity/kcm_kicker.so
%{prefix}/%{_lib}/trinity/kcm_tdeio.la
%{prefix}/%{_lib}/trinity/kcm_tdeio.so
%{prefix}/%{_lib}/trinity/kcm_knotify.la
%{prefix}/%{_lib}/trinity/kcm_knotify.so
%{prefix}/%{_lib}/trinity/kcm_konqhtml.la
%{prefix}/%{_lib}/trinity/kcm_konqhtml.so
%{prefix}/%{_lib}/trinity/kcm_konq.la
%{prefix}/%{_lib}/trinity/kcm_konq.so
%{prefix}/%{_lib}/trinity/kcm_kthememanager.la
%{prefix}/%{_lib}/trinity/kcm_kthememanager.so
%{prefix}/%{_lib}/trinity/kcm_kurifilt.la
%{prefix}/%{_lib}/trinity/kcm_kurifilt.so
%{prefix}/%{_lib}/trinity/kcm_launch.la
%{prefix}/%{_lib}/trinity/kcm_launch.so
%{prefix}/%{_lib}/trinity/kcm_locale.la
%{prefix}/%{_lib}/trinity/kcm_locale.so
%{prefix}/%{_lib}/trinity/kcm_nic.la
%{prefix}/%{_lib}/trinity/kcm_nic.so
%{prefix}/%{_lib}/trinity/kcm_performance.la
%{prefix}/%{_lib}/trinity/kcm_performance.so
%{prefix}/%{_lib}/trinity/kcm_privacy.la
%{prefix}/%{_lib}/trinity/kcm_privacy.so
%{prefix}/%{_lib}/trinity/kcm_screensaver.la
%{prefix}/%{_lib}/trinity/kcm_screensaver.so
%{prefix}/%{_lib}/trinity/kcm_smserver.la
%{prefix}/%{_lib}/trinity/kcm_smserver.so
%{prefix}/%{_lib}/trinity/kcm_spellchecking.la
%{prefix}/%{_lib}/trinity/kcm_spellchecking.so
%{prefix}/%{_lib}/trinity/kcm_style.la
%{prefix}/%{_lib}/trinity/kcm_style.so
%{prefix}/%{_lib}/trinity/kcm_taskbar.la
%{prefix}/%{_lib}/trinity/kcm_taskbar.so
%{prefix}/%{_lib}/trinity/kcm_usb.la
%{prefix}/%{_lib}/trinity/kcm_usb.so
%{prefix}/%{_lib}/trinity/kcm_view1394.la
%{prefix}/%{_lib}/trinity/kcm_view1394.so
%{prefix}/%{_lib}/trinity/kcm_xinerama.la
%{prefix}/%{_lib}/trinity/kcm_xinerama.so
%{prefix}/%{_lib}/trinity/kcontrol.la
%{prefix}/%{_lib}/trinity/kcontrol.so
%{prefix}/%{_lib}/trinity/tdefile_font.la
%{prefix}/%{_lib}/trinity/tdefile_font.so
%{prefix}/%{_lib}/trinity/tdeio_fonts.la
%{prefix}/%{_lib}/trinity/tdeio_fonts.so
%{prefix}/%{_lib}/trinity/tdestyle_keramik_config.la
%{prefix}/%{_lib}/trinity/tdestyle_keramik_config.so
%{prefix}/%{_lib}/trinity/libtdefontviewpart.la
%{prefix}/%{_lib}/trinity/libtdefontviewpart.so
%{prefix}/%{_lib}/trinity/libtdeshorturifilter.la
%{prefix}/%{_lib}/trinity/libtdeshorturifilter.so
%{prefix}/%{_lib}/trinity/libkuriikwsfilter.la
%{prefix}/%{_lib}/trinity/libkuriikwsfilter.so
%{prefix}/%{_lib}/trinity/libkurisearchfilter.la
%{prefix}/%{_lib}/trinity/libkurisearchfilter.so
%{prefix}/%{_lib}/trinity/liblocaldomainurifilter.la
%{prefix}/%{_lib}/trinity/liblocaldomainurifilter.so
%{prefix}/%{_lib}/libtdeinit_kaccess.la
%{prefix}/%{_lib}/libtdeinit_kaccess.so
%{prefix}/%{_lib}/libtdeinit_kcontrol.la
%{prefix}/%{_lib}/libtdeinit_kcontrol.so
%{prefix}/%{_lib}/libtdefontinst.so.*
%{prefix}/share/applications/tde/arts.desktop
%{prefix}/share/applications/tde/background.desktop
%{prefix}/share/applications/tde/bell.desktop
%{prefix}/share/applications/tde/cache.desktop
%{prefix}/share/applications/tde/cdinfo.desktop
%{prefix}/share/applications/tde/clock.desktop
%{prefix}/share/applications/tde/colors.desktop
%{prefix}/share/applications/tde/componentchooser.desktop
%{prefix}/share/applications/tde/cookies.desktop
%{prefix}/share/applications/tde/crypto.desktop
%{prefix}/share/applications/tde/desktopbehavior.desktop
%{prefix}/share/applications/tde/desktop.desktop
%{prefix}/share/applications/tde/desktoppath.desktop
%{prefix}/share/applications/tde/devices.desktop
%{prefix}/share/applications/tde/display.desktop
%{prefix}/share/applications/tde/dma.desktop
%{prefix}/share/applications/tde/ebrowsing.desktop
%{prefix}/share/applications/tde/filebrowser.desktop
%{prefix}/share/applications/tde/filetypes.desktop
%{prefix}/share/applications/tde/fonts.desktop
%{?with_tdehwlib:%{prefix}/share/applications/tde/hwmanager.desktop}
%{prefix}/share/applications/tde/icons.desktop
%{prefix}/share/applications/tde/installktheme.desktop
%{prefix}/share/applications/tde/interrupts.desktop
%{prefix}/share/applications/tde/ioports.desktop
%{prefix}/share/applications/tde/joystick.desktop
%{prefix}/share/applications/tde/kcm_tdednssd.desktop
%{prefix}/share/applications/tde/kcmaccess.desktop
%{prefix}/share/applications/tde/kcmcss.desktop
%{prefix}/share/applications/tde/kcmfontinst.desktop
%{prefix}/share/applications/tde/kcmkded.desktop
%{prefix}/share/applications/tde/kcmlaunch.desktop
%{prefix}/share/applications/tde/kcmnotify.desktop
%{prefix}/share/applications/tde/kcmperformance.desktop
%{prefix}/share/applications/tde/kcmsmserver.desktop
%{prefix}/share/applications/tde/kcmtaskbar.desktop
%{prefix}/share/applications/tde/kcmusb.desktop
%{prefix}/share/applications/tde/kcmview1394.desktop
%{prefix}/share/applications/tde/KControl.desktop
%{prefix}/share/applications/tde/tdm.desktop
%{prefix}/share/applications/tde/keys.desktop
%{prefix}/share/applications/tde/tdefontview.desktop
%{prefix}/share/applications/tde/tdehtml_behavior.desktop
%{prefix}/share/applications/tde/tdehtml_fonts.desktop
%{prefix}/share/applications/tde/tdehtml_java_js.desktop
%{prefix}/share/applications/tde/kthememanager.desktop
%{prefix}/share/applications/tde/lanbrowser.desktop
%{prefix}/share/applications/tde/language.desktop
%{prefix}/share/applications/tde/media.desktop
%{prefix}/share/applications/tde/memory.desktop
%{prefix}/share/applications/tde/mouse.desktop
%{prefix}/share/applications/tde/netpref.desktop
%{prefix}/share/applications/tde/nic.desktop
%{prefix}/share/applications/tde/opengl.desktop
%{prefix}/share/applications/tde/panel_appearance.desktop
%{prefix}/share/applications/tde/panel.desktop
%{prefix}/share/applications/tde/partitions.desktop
%{prefix}/share/applications/tde/pci.desktop
%{prefix}/share/applications/tde/privacy.desktop
%{prefix}/share/applications/tde/processor.desktop
%{prefix}/share/applications/tde/proxy.desktop
%{prefix}/share/applications/tde/screensaver.desktop
%{prefix}/share/applications/tde/scsi.desktop
%{prefix}/share/applications/tde/smbstatus.desktop
%{prefix}/share/applications/tde/sound.desktop
%{prefix}/share/applications/tde/spellchecking.desktop
%{prefix}/share/applications/tde/style.desktop
%{prefix}/share/applications/tde/tde-kcontrol.desktop
%{prefix}/share/applications/tde/useragent.desktop
%{prefix}/share/applications/tde/xserver.desktop
%{prefix}/share/applnk/.hidden/energy.desktop
%{prefix}/share/applnk/.hidden/fileappearance.desktop
%{prefix}/share/applnk/.hidden/filebehavior.desktop
%{prefix}/share/applnk/.hidden/filepreviews.desktop
%{prefix}/share/applnk/.hidden/kcmkonqyperformance.desktop
%{prefix}/share/applnk/.hidden/kicker_config_appearance.desktop
%{prefix}/share/applnk/.hidden/kicker_config.desktop
%{prefix}/share/applnk/.hidden/smb.desktop
%{prefix}/share/applnk/.hidden/xinerama.desktop
%{prefix}/share/applnk/Settings/LookNFeel/
%{prefix}/share/applnk/Settings/WebBrowsing/tdehtml_appearance.desktop
%{prefix}/share/applnk/Settings/WebBrowsing/nsplugin.desktop
%{prefix}/share/applnk/Settings/WebBrowsing/smb.desktop
%{prefix}/share/apps/kcm_componentchooser/kcm_browser.desktop
%{prefix}/share/apps/kcm_componentchooser/kcm_kemail.desktop
%{prefix}/share/apps/kcm_componentchooser/kcm_filemanager.desktop
%{prefix}/share/apps/kcm_componentchooser/kcm_terminal.desktop
%{prefix}/share/apps/kcmview1394/
%{prefix}/share/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{prefix}/share/apps/konqueror/servicemenus/installfont.desktop
%{prefix}/share/apps/usb.ids
%{prefix}/share/mimelnk/application/x-ktheme.desktop
%{prefix}/share/mimelnk/fonts/folder.desktop
%{prefix}/share/mimelnk/fonts/package.desktop
%{prefix}/share/mimelnk/fonts/system-folder.desktop
%{prefix}/share/services/fonts.protocol
%{prefix}/share/services/fontthumbnail.desktop
%{prefix}/share/services/kaccess.desktop
%{prefix}/share/services/tdefile_font.desktop
%{prefix}/share/services/tdefontviewpart.desktop
%{prefix}/share/services/tdeshorturifilter.desktop
%{prefix}/share/services/kuriikwsfilter.desktop
%{prefix}/share/services/kurisearchfilter.desktop
%{prefix}/share/services/localdomainurifilter.desktop
%{prefix}/share/icons/hicolor/*/apps/kcmcolors.png
%{prefix}/share/icons/hicolor/*/apps/kcmcomponentchooser.png
%{prefix}/share/icons/hicolor/*/apps/kcmdesktop.png
%{prefix}/share/icons/hicolor/*/apps/kcmdesktopbehavior.png
%{prefix}/share/icons/hicolor/*/apps/kcmkdnssd.png
%{prefix}/share/icons/hicolor/*/apps/kcmlaunch.png
%{prefix}/share/icons/hicolor/*/apps/kcmmedia.png
%{prefix}/share/icons/hicolor/*/apps/kcmmouse.png
%{prefix}/share/icons/hicolor/*/apps/kcmnetpref.png
%{prefix}/share/icons/hicolor/*/apps/kcmnic.png
%{prefix}/share/icons/hicolor/*/apps/kcmperformance.png
%{prefix}/share/icons/hicolor/*/apps/kcmprivacy.png
%{prefix}/share/icons/hicolor/*/apps/kcmtaskbar.png
%{prefix}/share/icons/hicolor/*/apps/kcmcgi.png
%{prefix}/share/icons/hicolor/*/apps/kcmcrypto.png
%{prefix}/share/icons/hicolor/*/apps/kcmhistory.png
%{prefix}/share/icons/hicolor/*/apps/kcmjoystick.png
%{prefix}/share/icons/hicolor/*/apps/kcmkded.png
%{prefix}/share/icons/hicolor/*/apps/kcmkhtml_filter.png
%{prefix}/share/icons/hicolor/*/apps/kcmsmserver.png
%{prefix}/share/icons/hicolor/*/apps/kcmspellchecking.png
%{prefix}/share/doc/tde/HTML/en/tdefontview/

# tdehwtray
%{prefix}/bin/tdehwdevicetray
%{prefix}/share/applications/tde/tdehwdevicetray.desktop
%{prefix}/share/autostart/tdehwdevicetray-autostart.desktop

# tdesyndaemon
%{prefix}/bin/tdesyndaemon
%{prefix}/share/applications/tde/touchpad.desktop
%{prefix}/share/apps/tdeconf_update/remote_folder_icon.upd
%{prefix}/share/apps/tdeconf_update/remote_folder_icon_upd.sh
%{prefix}/share/icons/crystalsvg/*/devices/input-touchpad.png
%{prefix}/share/icons/crystalsvg/scalable/devices/input-touchpad.svg
%{prefix}/share/services/kded/khotkeys.desktop

# The following features are not compiled under RHEL 5 and older
%if %{with tderandrtray}
%{prefix}/bin/tderandrtray
%{prefix}/%{_lib}/trinity/kcm_displayconfig.la
%{prefix}/%{_lib}/trinity/kcm_displayconfig.so
%{prefix}/%{_lib}/trinity/kcm_iccconfig.la
%{prefix}/%{_lib}/trinity/kcm_iccconfig.so
%{prefix}/%{_lib}/trinity/kcm_randr.la
%{prefix}/%{_lib}/trinity/kcm_randr.so
%{prefix}/share/applications/tde/displayconfig.desktop
%{prefix}/share/applications/tde/iccconfig.desktop
%{prefix}/share/applications/tde/tderandrtray.desktop
%{prefix}/share/applnk/.hidden/randr.desktop
%{prefix}/share/autostart/tderandrtray-autostart.desktop
%{prefix}/share/doc/tde/HTML/en/tderandrtray/
%endif

##########

%package -n trinity-kcontrol-devel
Summary:	Development files for kcontrol
Group:		Development/Libraries/Other
Requires:	trinity-kcontrol = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kcontrol-devel
%{summary}.

%files -n trinity-kcontrol-devel
%defattr(-,root,root,-)
%{prefix}/%{_lib}/libtdefontinst.la
%{prefix}/%{_lib}/libtdefontinst.so

##########

%package bin
Summary:	Core binaries for the TDE base module
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	pam

Provides:	tdebase-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdebase-bin < %{?epoch:%{epoch}:}%{version}-%{release}

%description bin
This package contains miscellaneous programs needed by other
TDE applications, particularly those in the TDE base module.

%files bin
%defattr(-,root,root,-)
%{prefix}/bin/krootbacking
%{?with_tsak:%{prefix}/bin/tsak}
%{?with_libconfig:%{prefix}/bin/compton-tde}
%{prefix}/bin/tdedebugdialog
%{prefix}/bin/kreadconfig
%{prefix}/bin/kwriteconfig
%{prefix}/bin/kstart
%config(noreplace) %{_sysconfdir}/trinity/kxkb_groups
%{prefix}/bin/drkonqi
%{prefix}/bin/crashtest
%{prefix}/bin/kapplymousetheme
%{prefix}/bin/kblankscrn.kss
%{prefix}/bin/kcminit
%{prefix}/bin/kcminit_startup
%{prefix}/bin/kdcop
%{prefix}/bin/tdesu
%attr(0755,root,root) %{prefix}/bin/tdesud
%{prefix}/bin/kdialog
%{prefix}/bin/khotkeys
%{prefix}/bin/knetattach
%{prefix}/bin/krandom.kss
%{prefix}/bin/ksystraycmd
%{prefix}/bin/kxkb
%{prefix}/bin/tde_license_info
%{prefix}/bin/tde_show_license_info
%dir %{prefix}/%{_lib}/tdeconf_update_bin
%{prefix}/%{_lib}/tdeconf_update_bin/khotkeys_update
%{prefix}/%{_lib}/trinity/kcminit.la
%{prefix}/%{_lib}/trinity/kcminit.so
%{prefix}/%{_lib}/trinity/kcminit_startup.la
%{prefix}/%{_lib}/trinity/kcminit_startup.so
%{prefix}/%{_lib}/trinity/kcm_keyboard.la
%{prefix}/%{_lib}/trinity/kcm_keyboard.so
%{prefix}/%{_lib}/trinity/kcm_khotkeys.la
%{prefix}/%{_lib}/trinity/kcm_khotkeys.so
%{prefix}/%{_lib}/trinity/kded_khotkeys.la
%{prefix}/%{_lib}/trinity/kded_khotkeys.so
%{prefix}/%{_lib}/trinity/kgreet_classic.la
%{prefix}/%{_lib}/trinity/kgreet_classic.so
%{prefix}/%{_lib}/trinity/kgreet_winbind.la
%{prefix}/%{_lib}/trinity/kgreet_winbind.so
%{prefix}/%{_lib}/trinity/khotkeys.la
%{prefix}/%{_lib}/trinity/khotkeys.so
%{prefix}/%{_lib}/trinity/khotkeys_arts.la
%{prefix}/%{_lib}/trinity/khotkeys_arts.so
%{prefix}/%{_lib}/trinity/kxkb.la
%{prefix}/%{_lib}/trinity/kxkb.so
%{prefix}/%{_lib}/libtdeinit_kcminit.la
%{prefix}/%{_lib}/libtdeinit_kcminit.so
%{prefix}/%{_lib}/libtdeinit_kcminit_startup.la
%{prefix}/%{_lib}/libtdeinit_kcminit_startup.so
%{prefix}/%{_lib}/libtdeinit_khotkeys.la
%{prefix}/%{_lib}/libtdeinit_khotkeys.so
%{prefix}/%{_lib}/libtdeinit_kxkb.la
%{prefix}/%{_lib}/libtdeinit_kxkb.so
%{prefix}/%{_lib}/libkhotkeys_shared.so.*
%{prefix}/share/applications/tde/kdcop.desktop
%{prefix}/share/applications/tde/keyboard.desktop
%{prefix}/share/applications/tde/keyboard_layout.desktop
%{prefix}/share/applications/tde/khotkeys.desktop
%{prefix}/share/applications/tde/knetattach.desktop
%{prefix}/share/applnk/System/ScreenSavers/
%{prefix}/share/apps/drkonqi/
%{prefix}/share/apps/tdeconf_update/khotkeys_32b1_update.upd
%{prefix}/share/apps/tdeconf_update/khotkeys_printscreen.upd
%{prefix}/share/apps/tdeconf_update/konqueror_gestures_trinity21_update.upd
%{prefix}/share/apps/kdcop/
%{prefix}/share/apps/khotkeys/
%{prefix}/share/autostart/tde_license_info.desktop
%{prefix}/share/services/kxkb.desktop
%config(noreplace) %{_sysconfdir}/pam.d/kcheckpass-trinity
%config(noreplace) %{_sysconfdir}/pam.d/tdescreensaver-trinity
%{prefix}/share/doc/tde/HTML/en/kdcop/
%{prefix}/share/doc/tde/HTML/en/tdedebugdialog//
%{prefix}/share/doc/tde/HTML/en/tdesu/
%{prefix}/share/doc/tde/HTML/en/knetattach/
%{prefix}/share/doc/tde/HTML/en/kxkb/
%{prefix}/share/man/man1/drkonqi.1*
%{prefix}/share/man/man1/kblankscrn.kss.1*
%{prefix}/share/man/man1/kcheckpass.1*
%{prefix}/share/man/man1/kcminit.1*
%{prefix}/share/man/man1/kdcop.1*
%{prefix}/share/man/man1/kdialog.1*
%{prefix}/share/man/man1/khotkeys.1*
%{prefix}/share/man/man1/knetattach.1*
%{prefix}/share/man/man1/krandom.kss.1*
%{prefix}/share/man/man1/kreadconfig.1*
%{prefix}/share/man/man1/kstart.1*
%{prefix}/share/man/man1/ksystraycmd.1*
%{prefix}/share/man/man1/kwriteconfig.1*
%{prefix}/share/man/man1/kxkb.1*
%{prefix}/share/man/man1/tdedebugdialog.1*
%{prefix}/share/man/man1/tdesu.1*

# SETUID binaries
# Some setuid binaries need special care
%{?with_tsak:%attr(4511,root,root) %{prefix}/bin/tdmtsak}
%attr(4755,root,root) %{prefix}/bin/kcheckpass
%{?with_kbdledsync:%attr(4755,root,root) %{prefix}/bin/tdekbdledsync}

%package bin-devel
Summary:	Development files for core binaries for the TDE base module
Group:		Development/Libraries/Other
Requires:	%{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

Obsoletes:	tdebase-bin-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-bin-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description bin-devel
This package contains the development files for core binaries for 
the TDE base module

%files bin-devel
%defattr(-,root,root,-)
%{prefix}/%{_lib}/libkhotkeys_shared.la
%{prefix}/%{_lib}/libkhotkeys_shared.so

##########

%package data
Summary:	Shared data files for the TDE base module
Group:		System/GUI/Other
Requires:	%{name}-runtime-data-common = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	tdebase-data < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description data
This package contains the architecture-independent shared data files
needed for a basic TDE desktop installation.

%files data
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/tdeshorturifilterrc
%{prefix}/share/applnk/.hidden/battery.desktop
%{prefix}/share/applnk/.hidden/bwarning.desktop
%{prefix}/share/applnk/.hidden/cwarning.desktop
%{prefix}/share/applnk/.hidden/.directory
%{prefix}/share/applnk/.hidden/email.desktop
%{prefix}/share/applnk/.hidden/kcmkonq.desktop
%{prefix}/share/applnk/.hidden/kcmkxmlrpcd.desktop
%{prefix}/share/applnk/.hidden/konqhtml.desktop
%{prefix}/share/applnk/.hidden/passwords.desktop
%{prefix}/share/applnk/.hidden/power.desktop
%{prefix}/share/applnk/.hidden/socks.desktop
%{prefix}/share/applnk/.hidden/userinfo.desktop
%{prefix}/share/applnk/.hidden/virtualdesktops.desktop
%{prefix}/share/apps/kaccess/
%{prefix}/share/apps/kcmcss/
%{prefix}/share/apps/kcminput/
%{prefix}/share/apps/kcmkeys/
%{prefix}/share/apps/kcmlocale/
%{prefix}/share/apps/tdeconf_update/convertShortcuts.pl
%{prefix}/share/apps/tdeconf_update/tdeaccel.upd
%{prefix}/share/apps/tdeconf_update/kcmdisplayrc.upd
%{prefix}/share/apps/tdeconf_update/kuriikwsfilter.upd
%{prefix}/share/apps/tdeconf_update/mouse_cursor_theme.upd
%{prefix}/share/apps/tdeconf_update/socks.upd
%{prefix}/share/apps/kcontrol/
%{prefix}/share/apps/tdedisplay/
%{prefix}/share/apps/tdefontview/
%{prefix}/share/apps/kthememanager/
%{prefix}/share/icons/crystalsvg/*/apps/access.png
%{prefix}/share/icons/crystalsvg/*/apps/acroread.png
%{prefix}/share/icons/crystalsvg/*/apps/applixware.png
%{prefix}/share/icons/crystalsvg/*/apps/arts.png
%{prefix}/share/icons/crystalsvg/*/apps/background.png
%{prefix}/share/icons/crystalsvg/*/apps/bell.png
%{prefix}/share/icons/crystalsvg/*/apps/cache.png
%{prefix}/share/icons/crystalsvg/*/apps/clanbomber.png
%{prefix}/share/icons/crystalsvg/*/apps/clock.png
%{prefix}/share/icons/crystalsvg/*/apps/colors.png
%{prefix}/share/icons/crystalsvg/*/apps/date.png
%{prefix}/share/icons/crystalsvg/*/apps/email.png
%{prefix}/share/icons/crystalsvg/*/apps/energy.png
%{prefix}/share/icons/crystalsvg/*/apps/energy_star.png
%{prefix}/share/icons/crystalsvg/*/apps/filetypes.png
%{prefix}/share/icons/crystalsvg/*/apps/fonts.png
%{prefix}/share/icons/crystalsvg/*/apps/gimp.png
%{prefix}/share/icons/crystalsvg/*/apps/help_index.png
%{prefix}/share/icons/crystalsvg/*/apps/hwinfo.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmdevices.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmdf.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmkwm.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmmemory.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmpartitions.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmpci.png
%{prefix}/share/icons/crystalsvg/*/apps/kcontrol.png
%{prefix}/share/icons/crystalsvg/*/apps/tdmconfig.png
%{prefix}/share/icons/crystalsvg/*/apps/key_bindings.png
%{prefix}/share/icons/crystalsvg/*/apps/kfm_home.png
%{prefix}/share/icons/crystalsvg/*/apps/tdescreensaver.png
%{prefix}/share/icons/crystalsvg/*/apps/kthememgr.png
%{prefix}/share/icons/crystalsvg/*/apps/licq.png
%{prefix}/share/icons/crystalsvg/*/apps/linuxconf.png
%{prefix}/share/icons/crystalsvg/*/apps/locale.png
%{prefix}/share/icons/crystalsvg/*/categories/preferences-desktop.png
%{prefix}/share/icons/crystalsvg/*/apps/multimedia.png
%{prefix}/share/icons/crystalsvg/*/apps/netscape.png
%{prefix}/share/icons/crystalsvg/*/apps/package_applications.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-development.png
%{prefix}/share/icons/crystalsvg/*/apps/package_favourite.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-games.png
%{prefix}/share/icons/crystalsvg/*/apps/package_games_kids.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-multimedia.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-internet.png
%{prefix}/share/icons/crystalsvg/*/apps/package.png
%{prefix}/share/icons/crystalsvg/*/apps/package_settings.png
%{prefix}/share/icons/crystalsvg/*/apps/package_toys.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-utilities.png
%{prefix}/share/icons/crystalsvg/*/apps/penguin.png
%{prefix}/share/icons/crystalsvg/*/categories/preferences-desktop-personal.png
%{prefix}/share/icons/crystalsvg/*/apps/phppg.png
%{prefix}/share/icons/crystalsvg/*/apps/package_games_logic.png
%{prefix}/share/icons/crystalsvg/*/apps/proxy.png
%{prefix}/share/icons/crystalsvg/*/apps/pysol.png
%{prefix}/share/icons/crystalsvg/*/apps/randr.png
%{prefix}/share/icons/crystalsvg/*/apps/samba.png
%{prefix}/share/icons/crystalsvg/*/apps/staroffice.png
%{prefix}/share/icons/crystalsvg/*/apps/stylesheet.png
%{prefix}/share/icons/crystalsvg/*/apps/terminal.png
%{prefix}/share/icons/crystalsvg/*/apps/tux.png
%{prefix}/share/icons/crystalsvg/*/apps/wp.png
%{prefix}/share/icons/crystalsvg/*/apps/xclock.png
%{prefix}/share/icons/crystalsvg/*/apps/xfmail.png
%{prefix}/share/icons/crystalsvg/*/apps/xmag.png
%{prefix}/share/icons/crystalsvg/*/apps/xpaint.png
%{prefix}/share/icons/crystalsvg/scalable/apps/access.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/acroread.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/aim.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/aktion.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/antivirus.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/applixware.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/arts.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/background.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/bell.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/browser.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/cache.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/camera.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/clanbomber.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/clock.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/colors.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/core.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/date.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/display.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/download_manager.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/email.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/energy.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/error.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/fifteenpieces.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/filetypes.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/fonts.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/galeon.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/gnome_apps.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/hardware.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/hwinfo.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/ieee1394.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/kcmdevices.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/kcmkwm.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/kcmx.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/locale.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/my_mac.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/netscape.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/openoffice.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/package_development.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/package_games_kids.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/package_toys.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/penguin.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/personal.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/quicktime.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/realplayer.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/samba.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/shell.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/staroffice.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/stylesheet.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/terminal.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/tux.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/wine.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/x.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/xapp.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/xcalc.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/xchat.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/xclock.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/xeyes.svgz
%{prefix}/share/icons/crystalsvg/scalable/apps/xpaint.svgz
%{prefix}/share/icons/crystalsvg/*/devices/laptop.png
%{prefix}/share/icons/crystalsvg/*/devices/laptop.svgz
%{prefix}/share/icons/crystalsvg/*/actions/newfont.png
%{prefix}/share/icons/crystalsvg/*/apps/abiword.png
%{prefix}/share/icons/crystalsvg/*/apps/agent.png
%{prefix}/share/icons/crystalsvg/*/apps/alevt.png
%{prefix}/share/icons/crystalsvg/*/apps/assistant.png
%{prefix}/share/icons/crystalsvg/*/apps/blender.png
%{prefix}/share/icons/crystalsvg/*/apps/bluefish.png
%{prefix}/share/icons/crystalsvg/*/apps/cookie.png
%{prefix}/share/icons/crystalsvg/*/apps/designer.png
%{prefix}/share/icons/crystalsvg/*/apps/dia.png
%{prefix}/share/icons/crystalsvg/*/apps/dlgedit.png
%{prefix}/share/icons/crystalsvg/*/apps/eclipse.png
%{prefix}/share/icons/crystalsvg/*/apps/edu_languages.png
%{prefix}/share/icons/crystalsvg/*/apps/edu_mathematics.png
%{prefix}/share/icons/crystalsvg/*/apps/edu_miscellaneous.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-science.png
%{prefix}/share/icons/crystalsvg/*/apps/emacs.png
%{prefix}/share/icons/crystalsvg/*/apps/enhanced_browsing.png
%{prefix}/share/icons/crystalsvg/*/apps/evolution.png
%{prefix}/share/icons/crystalsvg/*/apps/fifteenpieces.png
%{prefix}/share/icons/crystalsvg/*/apps/gabber.png
%{prefix}/share/icons/crystalsvg/*/apps/gaim.png
%{prefix}/share/icons/crystalsvg/*/apps/gnome_apps.png
%{prefix}/share/icons/crystalsvg/*/apps/gnomemeeting.png
%{prefix}/share/icons/crystalsvg/*/apps/gnucash.png
%{prefix}/share/icons/crystalsvg/*/apps/gnumeric.png
%{prefix}/share/icons/crystalsvg/*/apps/gv.png
%{prefix}/share/icons/crystalsvg/*/apps/gvim.png
%{prefix}/share/icons/crystalsvg/*/apps/icons.png
%{prefix}/share/icons/crystalsvg/*/apps/iconthemes.png
%{prefix}/share/icons/crystalsvg/*/apps/ieee1394.png
%{prefix}/share/icons/crystalsvg/*/categories/preferences-desktop-peripherals.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmkicker.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmmidi.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmprocessor.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmscsi.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmsound.png
%{prefix}/share/icons/crystalsvg/*/categories/preferences-system.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmx.png
%{prefix}/share/icons/crystalsvg/*/apps/keyboard.png
%{prefix}/share/icons/crystalsvg/*/apps/keyboard_layout.png
%{prefix}/share/icons/crystalsvg/*/apps/knotify.png
%{prefix}/share/icons/crystalsvg/*/apps/kvirc.png
%{prefix}/share/icons/crystalsvg/*/apps/linguist.png
%{prefix}/share/icons/crystalsvg/*/apps/lyx.png
%{prefix}/share/icons/crystalsvg/*/apps/mac.png
%{prefix}/share/icons/crystalsvg/*/apps/mathematica.png
%{prefix}/share/icons/crystalsvg/*/apps/nedit.png
%{prefix}/share/icons/crystalsvg/*/apps/opera.png
%{prefix}/share/icons/crystalsvg/*/apps/package_application.png
%{prefix}/share/icons/crystalsvg/*/apps/package_editors.png
%{prefix}/share/icons/crystalsvg/*/apps/package_edutainment.png
%{prefix}/share/icons/crystalsvg/*/apps/package_games_arcade.png
%{prefix}/share/icons/crystalsvg/*/apps/package_games_board.png
%{prefix}/share/icons/crystalsvg/*/apps/package_games_card.png
%{prefix}/share/icons/crystalsvg/*/apps/package_games_strategy.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-graphics.png
%{prefix}/share/icons/crystalsvg/*/apps/package_system.png
%{prefix}/share/icons/crystalsvg/*/categories/applications-office.png
%{prefix}/share/icons/crystalsvg/*/apps/pan.png
%{prefix}/share/icons/crystalsvg/*/apps/panel_settings.png
%{prefix}/share/icons/crystalsvg/*/apps/plan.png
%{prefix}/share/icons/crystalsvg/*/apps/planner.png
%{prefix}/share/icons/crystalsvg/*/apps/pybliographic.png
%{prefix}/share/icons/crystalsvg/*/apps/realplayer.png
%{prefix}/share/icons/crystalsvg/*/apps/remote.png
%{prefix}/share/icons/crystalsvg/*/apps/scribus.png
%{prefix}/share/icons/crystalsvg/*/apps/sodipodi.png
%{prefix}/share/icons/crystalsvg/*/apps/style.png
%{prefix}/share/icons/crystalsvg/*/apps/usb.png
%{prefix}/share/icons/crystalsvg/*/apps/vnc.png
%{prefix}/share/icons/crystalsvg/*/apps/wabi.png
%{prefix}/share/icons/crystalsvg/*/apps/wine.png
%{prefix}/share/icons/crystalsvg/*/apps/xcalc.png
%{prefix}/share/icons/crystalsvg/*/apps/xchat.png
%{prefix}/share/icons/crystalsvg/*/apps/xclipboard.png
%{prefix}/share/icons/crystalsvg/*/apps/xconsole.png
%{prefix}/share/icons/crystalsvg/*/apps/xedit.png
%{prefix}/share/icons/crystalsvg/*/apps/xemacs.png
%{prefix}/share/icons/crystalsvg/*/apps/xeyes.png
%{prefix}/share/icons/crystalsvg/*/apps/xfig.png
%{prefix}/share/icons/crystalsvg/*/apps/xload.png
%{prefix}/share/icons/crystalsvg/*/apps/xmms.png
%{prefix}/share/icons/crystalsvg/*/apps/xosview.png
%{prefix}/share/icons/crystalsvg/*/apps/xv.png
%{prefix}/share/icons/crystalsvg/*/apps/galeon.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmdrkonqi.png
%{prefix}/share/icons/crystalsvg/*/apps/pinguin.png
%{prefix}/share/icons/crystalsvg/*/apps/x.png
%{prefix}/share/icons/crystalsvg/*/apps/xapp.png
%{prefix}/share/icons/crystalsvg/*/apps/xawtv.png
%{prefix}/share/icons/crystalsvg/*/apps/kcmopengl.png
%{prefix}/share/icons/crystalsvg/*/apps/wmaker_apps.png
%{prefix}/share/icons/crystalsvg/*/apps/qtella.png
%{prefix}/share/services/searchproviders
%{prefix}/share/services/useragentstrings/
%{prefix}/share/servicetypes/searchprovider.desktop
%{prefix}/share/servicetypes/uasprovider.desktop
%exclude %{prefix}/share/sounds/pop.wav
%{prefix}/share/sounds/
%{prefix}/share/wallpapers/*

# XDG directories information
%dir %{_sysconfdir}/xdg/menus/applications-merged
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/tde-essential.menu
%config(noreplace) %{_sysconfdir}/xdg/menus/tde-screensavers.menu
%config(noreplace) %{_sysconfdir}/xdg/menus/tde-settings.menu

%{prefix}/share/doc/tde/HTML/en/kcontrol/
%exclude %{prefix}/share/doc/tde/HTML/en/kcontrol/kcmkonsole/


%package tdeio-plugins
Summary:	Core I/O slaves for TDE
Group:		System/GUI/Other
Requires:	trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	cyrus-sasl
Requires:	psmisc

Obsoletes:	tdebase-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-tdebase-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdebase-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This package includes the base tdeioslaves. They include, amongst many
others, file, http, and ftp.

It also includes the media tdeioslave, which handles removable devices,
and which works best with udev, udisks and pmount. Media
also extends the functionality of many other tdeioslaves. To use this
service, please make sure that your user is a member of the plugdev
group.

%files tdeio-plugins
%defattr(-,root,root,-)
%{prefix}/bin/tdeio_media_mounthelper
%{prefix}/bin/ktrash
%{prefix}/%{_lib}/trinity/cursorthumbnail.la
%{prefix}/%{_lib}/trinity/cursorthumbnail.so
%{prefix}/%{_lib}/trinity/djvuthumbnail.la
%{prefix}/%{_lib}/trinity/djvuthumbnail.so
%{prefix}/%{_lib}/trinity/htmlthumbnail.la
%{prefix}/%{_lib}/trinity/htmlthumbnail.so
%{prefix}/%{_lib}/trinity/imagethumbnail.la
%{prefix}/%{_lib}/trinity/imagethumbnail.so
%{prefix}/%{_lib}/trinity/kcm_cgi.la
%{prefix}/%{_lib}/trinity/kcm_cgi.so
%{prefix}/%{_lib}/trinity/kcm_media.la
%{prefix}/%{_lib}/trinity/kcm_media.so
%{prefix}/%{_lib}/trinity/kcm_trash.la
%{prefix}/%{_lib}/trinity/kcm_trash.so
%{prefix}/%{_lib}/trinity/kded_homedirnotify.la
%{prefix}/%{_lib}/trinity/kded_homedirnotify.so
%{prefix}/%{_lib}/trinity/kded_mediamanager.la
%{prefix}/%{_lib}/trinity/kded_mediamanager.so
%{prefix}/%{_lib}/trinity/kded_medianotifier.la
%{prefix}/%{_lib}/trinity/kded_medianotifier.so
%{prefix}/%{_lib}/trinity/kded_remotedirnotify.la
%{prefix}/%{_lib}/trinity/kded_remotedirnotify.so
%{prefix}/%{_lib}/trinity/kded_systemdirnotify.la
%{prefix}/%{_lib}/trinity/kded_systemdirnotify.so
%{prefix}/%{_lib}/trinity/tdefile_media.la
%{prefix}/%{_lib}/trinity/tdefile_media.so
%{prefix}/%{_lib}/trinity/tdefile_trash.la
%{prefix}/%{_lib}/trinity/tdefile_trash.so
%{prefix}/%{_lib}/trinity/tdeio_about.la
%{prefix}/%{_lib}/trinity/tdeio_about.so
%{prefix}/%{_lib}/trinity/tdeio_cgi.la
%{prefix}/%{_lib}/trinity/tdeio_cgi.so
%{prefix}/%{_lib}/trinity/tdeio_filter.la
%{prefix}/%{_lib}/trinity/tdeio_filter.so
%{prefix}/%{_lib}/trinity/tdeio_finger.la
%{prefix}/%{_lib}/trinity/tdeio_finger.so
%{prefix}/%{_lib}/trinity/tdeio_fish.la
%{prefix}/%{_lib}/trinity/tdeio_fish.so
%{prefix}/%{_lib}/trinity/tdeio_floppy.la
%{prefix}/%{_lib}/trinity/tdeio_floppy.so
%{prefix}/%{_lib}/trinity/tdeio_home.la
%{prefix}/%{_lib}/trinity/tdeio_home.so
%{prefix}/%{_lib}/trinity/tdeio_info.la
%{prefix}/%{_lib}/trinity/tdeio_info.so
%{prefix}/%{_lib}/trinity/tdeio_mac.la
%{prefix}/%{_lib}/trinity/tdeio_mac.so
%{prefix}/%{_lib}/trinity/tdeio_man.la
%{prefix}/%{_lib}/trinity/tdeio_man.so
%{prefix}/%{_lib}/trinity/tdeio_media.la
%{prefix}/%{_lib}/trinity/tdeio_media.so
%{prefix}/%{_lib}/trinity/tdeio_nfs.la
%{prefix}/%{_lib}/trinity/tdeio_nfs.so
%{prefix}/%{_lib}/trinity/tdeio_remote.la
%{prefix}/%{_lib}/trinity/tdeio_remote.so
%{prefix}/%{_lib}/trinity/tdeio_settings.la
%{prefix}/%{_lib}/trinity/tdeio_settings.so
%if %{with ssh}
%{prefix}/%{_lib}/trinity/tdeio_sftp.la
%{prefix}/%{_lib}/trinity/tdeio_sftp.so
%endif
%{prefix}/%{_lib}/trinity/tdeio_system.la
%{prefix}/%{_lib}/trinity/tdeio_system.so
%{prefix}/%{_lib}/trinity/tdeio_tar.la
%{prefix}/%{_lib}/trinity/tdeio_tar.so
%{prefix}/%{_lib}/trinity/tdeio_thumbnail.la
%{prefix}/%{_lib}/trinity/tdeio_thumbnail.so
%{prefix}/%{_lib}/trinity/tdeio_trash.la
%{prefix}/%{_lib}/trinity/tdeio_trash.so
%{prefix}/%{_lib}/trinity/libkmanpart.la
%{prefix}/%{_lib}/trinity/libkmanpart.so
%{prefix}/%{_lib}/trinity/textthumbnail.la
%{prefix}/%{_lib}/trinity/textthumbnail.so
%{prefix}/share/applications/tde/kcmcgi.desktop
%{prefix}/share/applications/tde/kcmtrash.desktop
%{prefix}/share/apps/tdeio_finger/
%{prefix}/share/apps/tdeio_info/
%{prefix}/share/apps/tdeio_man/
%{prefix}/share/apps/systemview/
%{prefix}/share/autostart/mediabackend.desktop
%{prefix}/share/config.kcfg/mediamanagersettings.kcfg
%{prefix}/share/mimelnk/application/x-smb-server.desktop
%{prefix}/share/mimelnk/inode/system_directory.desktop
%{prefix}/share/mimelnk/media/*.desktop
%{prefix}/share/services/about.protocol
%{prefix}/share/services/applications.protocol
%{prefix}/share/services/ar.protocol
%{prefix}/share/services/bzip.protocol
%{prefix}/share/services/bzip2.protocol
%{prefix}/share/services/cgi.protocol
%{prefix}/share/services/cursorthumbnail.desktop
%{prefix}/share/services/djvuthumbnail.desktop
%{prefix}/share/services/finger.protocol
%{prefix}/share/services/fish.protocol
%{prefix}/share/services/floppy.protocol
%{prefix}/share/services/gzip.protocol
%{prefix}/share/services/home.protocol
%{prefix}/share/services/htmlthumbnail.desktop
%{prefix}/share/services/imagethumbnail.desktop
%{prefix}/share/services/info.protocol
%{prefix}/share/services/kded/homedirnotify.desktop
%{prefix}/share/services/kded/mediamanager.desktop
%{prefix}/share/services/kded/medianotifier.desktop
%{prefix}/share/services/kded/remotedirnotify.desktop
%{prefix}/share/services/kded/systemdirnotify.desktop
%{prefix}/share/services/tdefile_media.desktop
%{prefix}/share/services/tdefile_trash_system.desktop
%{prefix}/share/services/lzma.protocol
%{prefix}/share/services/kmanpart.desktop
%{prefix}/share/services/mac.protocol
%{prefix}/share/services/man.protocol
%{prefix}/share/services/media.protocol
%{prefix}/share/services/nfs.protocol
%{prefix}/share/services/nxfish.protocol
%{prefix}/share/services/programs.protocol
%{prefix}/share/services/remote.protocol
%{prefix}/share/services/settings.protocol
%{?with_ssh:%{prefix}/share/services/sftp.protocol}
%{prefix}/share/services/system.protocol
%{prefix}/share/services/tar.protocol
%{prefix}/share/services/textthumbnail.desktop
%{prefix}/share/services/thumbnail.protocol
%{prefix}/share/services/trash.protocol
%{prefix}/share/services/xz.protocol
%{prefix}/share/services/zip.protocol
%{prefix}/share/servicetypes/thumbcreator.desktop
%{prefix}/share/services/tdefile_trash.desktop
%{prefix}/share/doc/tde/HTML/en/tdeioslave/
%{prefix}/share/man/man1/ktrash.1*
%{prefix}/share/man/man1/tdeio_media_mounthelper.1*
%if %{with openexr}
%{prefix}/%{_lib}/trinity/exrthumbnail.la
%{prefix}/%{_lib}/trinity/exrthumbnail.so
%{prefix}/share/services/exrthumbnail.desktop
%endif

# HWManager
%{prefix}/%{_lib}/trinity/media_propsdlgplugin.la
%{prefix}/%{_lib}/trinity/media_propsdlgplugin.so
%{prefix}/share/services/media_propsdlgplugin.desktop

%{prefix}/%{_lib}/trinity/ktrashpropsdlgplugin.la
%{prefix}/%{_lib}/trinity/ktrashpropsdlgplugin.so
%{prefix}/share/services/ktrashpropsdlgplugin.desktop

##########

%package -n trinity-tdepasswd
Summary:	Password changer for TDE
Group:		System/GUI/Other

Obsoletes:	trinity-kdepasswd < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdepasswd = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdepasswd
This is a simple application which allows users to change their
system passwords.

%files -n trinity-tdepasswd
%defattr(-,root,root,-)
%{prefix}/bin/tdepasswd
%{prefix}/%{_lib}/trinity/kcm_useraccount.la
%{prefix}/%{_lib}/trinity/kcm_useraccount.so
%{prefix}/share/applications/tde/kcm_useraccount.desktop
%{prefix}/share/applications/tde/tdepasswd.desktop
%{prefix}/share/config.kcfg/kcm_useraccount.kcfg
%{prefix}/share/config.kcfg/kcm_useraccount_pass.kcfg
%{prefix}/share/doc/tde/HTML/en/tdepasswd/
%{_datadir}/faces/Apple.png
%{_datadir}/faces/BeachBall.png
%{_datadir}/faces/Blowfish.png
%{_datadir}/faces/Bug.png
%{_datadir}/faces/Butterfly.png
%{_datadir}/faces/Car.png
%{_datadir}/faces/Cow.png 
%{_datadir}/faces/Daemon.png
%{_datadir}/faces/Dog.png
%{_datadir}/faces/Elephant.png
%{_datadir}/faces/Flower.png
%{_datadir}/faces/Frog.png
%{_datadir}/faces/Ghost.png
%{_datadir}/faces/Guitar.png
%{_datadir}/faces/Heart.png
%{_datadir}/faces/Konqui.png
%{_datadir}/faces/Lion.png
%{_datadir}/faces/Monkey.png
%{_datadir}/faces/Penguin.png
%{_datadir}/faces/Pig.png
%{_datadir}/faces/Rabbit.png
%{_datadir}/faces/Ring.png
%{_datadir}/faces/Scream.png
%{_datadir}/faces/Shark.png
%{_datadir}/faces/Splash.png
%{_datadir}/faces/Star.png
%{_datadir}/faces/Teddybear.png
%{_datadir}/faces/Turtle.png
%{prefix}/share/man/man1/tdepasswd.1*

##########

%package -n trinity-tdeprint
Summary:	Print system for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	psutils

%description -n trinity-tdeprint
This package contains the TDE printing subsystem. It can use CUPS,
lpd-ng or the traditional lpd. It also includes support for fax and
pdf printing.

Installation of smbclient will make you able to use smb shared printers.

%files -n trinity-tdeprint
%defattr(-,root,root,-)
%{prefix}/bin/tdeprintfax
%{prefix}/bin/kjobviewer
%{prefix}/bin/kprinter
%{prefix}/%{_lib}/trinity/kcm_printmgr.la
%{prefix}/%{_lib}/trinity/kcm_printmgr.so
%{prefix}/%{_lib}/trinity/tdeio_print.la
%{prefix}/%{_lib}/trinity/tdeio_print.so
%{prefix}/%{_lib}/trinity/kjobviewer.la
%{prefix}/%{_lib}/trinity/kjobviewer.so
%{prefix}/%{_lib}/trinity/kprinter.la
%{prefix}/%{_lib}/trinity/kprinter.so
%{prefix}/%{_lib}/trinity/libtdeprint_part.la
%{prefix}/%{_lib}/trinity/libtdeprint_part.so
%{prefix}/%{_lib}/libtdeinit_kjobviewer.la
%{prefix}/%{_lib}/libtdeinit_kjobviewer.so
%{prefix}/%{_lib}/libtdeinit_kprinter.la
%{prefix}/%{_lib}/libtdeinit_kprinter.so
%{prefix}/share/applications/tde/tdeprintfax.desktop
%{prefix}/share/applications/tde/kjobviewer.desktop
%{prefix}/share/applications/tde/printers.desktop
%{prefix}/share/apps/tdeprint/
%{prefix}/share/apps/tdeprintfax/
%{prefix}/share/apps/kjobviewer/
%{prefix}/share/apps/tdeprint_part/
%{prefix}/share/autostart/kjobviewer-autostart.desktop
%{prefix}/share/icons/hicolor/*/apps/tdeprintfax.png
%{prefix}/share/icons/hicolor/*/apps/kjobviewer.png
%{prefix}/share/icons/hicolor/*/apps/printmgr.png
%{prefix}/share/icons/hicolor/scalable/apps/tdeprintfax.svgz
%{prefix}/share/icons/hicolor/scalable/apps/kjobviewer.svgz
%{prefix}/share/icons/hicolor/scalable/apps/printmgr.svgz
%{prefix}/share/mimelnk/print/class.desktop
%{prefix}/share/mimelnk/print/driver.desktop
%{prefix}/share/mimelnk/print/folder.desktop
%{prefix}/share/mimelnk/print/jobs.desktop
%{prefix}/share/mimelnk/print/manager.desktop
%{prefix}/share/mimelnk/print/printer.desktop
%{prefix}/share/mimelnk/print/printermodel.desktop
%{prefix}/share/services/tdeprint_part.desktop
%{prefix}/share/services/print.protocol
%{prefix}/share/services/printdb.protocol
%{prefix}/share/doc/tde/HTML/en/tdeprint/
%{prefix}/share/doc/tde/HTML/en/tdeprintfax/
%{prefix}/share/doc/tde/HTML/en/kjobviewer/
%{prefix}/share/man/man1/kjobviewer.1*
%{prefix}/share/man/man1/kprinter.1*
%{prefix}/share/man/man1/tdeprintfax.1*

##########

%package -n trinity-kdesktop
Summary:	Miscellaneous binaries and files for the TDE desktop
Group:		System/GUI/Other
Requires:	%{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	eject
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
Requires:	xdg-utils
%endif

%description -n trinity-kdesktop
This package contains miscellaneous binaries and files integral to
the TDE desktop.

%files -n trinity-kdesktop
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kdesktop_custom_menu1
%config(noreplace) %{_sysconfdir}/trinity/kdesktop_custom_menu2
%{prefix}/bin/kcheckrunning
%{prefix}/bin/tdeeject
%{prefix}/bin/kdesktop
%{prefix}/bin/kdesktop_lock
%{prefix}/bin/kwebdesktop
%{prefix}/%{_lib}/trinity/kdesktop.la
%{prefix}/%{_lib}/trinity/kdesktop.so
%{prefix}/%{_lib}/libtdeinit_kdesktop.la
%{prefix}/%{_lib}/libtdeinit_kdesktop.so
%{prefix}/share/apps/kdesktop/
%{prefix}/share/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%{prefix}/share/autostart/kdesktop.desktop
%{prefix}/share/config.kcfg/kdesktop.kcfg
%{prefix}/share/config.kcfg/tdelaunch.kcfg
%{prefix}/share/config.kcfg/kwebdesktop.kcfg
%{prefix}/share/icons/crystalsvg/*/apps/error.png

##########

%package -n trinity-kdesktop-devel
Summary:	Development files for kdesktop
Group:		Development/Libraries/Other
Requires:	trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kdesktop-devel
This package contains the development files for kdesktop.

%files -n trinity-kdesktop-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/KBackgroundIface.h
%{prefix}/include/tde/KDesktopIface.h
%{prefix}/include/tde/KScreensaverIface.h

##########

%package -n trinity-tdm
Summary:	X Display manager for TDE
Group:		System/GUI/Other
Requires:	%{name}-bin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	pam
Requires:	logrotate

# Provides the global Xsession script (/etc/X11/xinit/Xsession or /etc/X11/Xsession)
Requires:	xinitrc
Provides:	dm
Provides:	tdm

%description -n trinity-tdm
TDM manages a collection of X servers, which may be on the local host or
remote machines. It provides services similar to those provided by init,
getty, and login on character-based terminals: prompting for login name and
password, authenticating the user, and running a session. tdm supports XDMCP
(X Display Manager Control Protocol) and can also be used to run a chooser
process which presents the user with a menu of possible hosts that offer
XDMCP display management.

A collection of icons to associate with individual users is included with
TDE, but as part of the tdepasswd package.

The menu package will help to provide TDM with a list of window managers
that can be launched, if the window manager does not register with TDM
already. Most users won't need this.

%files -n trinity-tdm
%defattr(-,root,root,-)
%{prefix}/%{_lib}/trinity/kgreet_pam.la
%{prefix}/%{_lib}/trinity/kgreet_pam.so
%{prefix}/bin/gentdmconf
%{prefix}/bin/tdm
%{prefix}/bin/tdm_config
%{prefix}/bin/tdmctl
%{prefix}/bin/tdm_greet
%{prefix}/bin/krootimage
%dir %{prefix}/share/apps/tdm
%dir %{prefix}/share/apps/tdm/pics
%{prefix}/share/apps/tdm/pics/tdelogo.png
%{prefix}/share/apps/tdm/pics/shutdown.jpg
%{prefix}/share/apps/tdm/pics/users
%dir %{prefix}/share/apps/tdm/sessions
%{prefix}/share/apps/tdm/sessions/*.desktop
%{prefix}/share/apps/tdm/themes/
%config(noreplace) %{_sysconfdir}/trinity/tdm
%{prefix}/share/doc/tde/HTML/en/tdm/
%config(noreplace) %{_sysconfdir}/pam.d/tdm-trinity
%config(noreplace) %{_sysconfdir}/pam.d/tdm-trinity-np
%{prefix}/share/man/man1/gentdmconf.1*
%{prefix}/share/man/man1/krootimage.1*
%{prefix}/share/man/man1/tdm.1*
%{prefix}/share/man/man1/tdmctl.1*
%{prefix}/share/man/man1/tdm_config.1*
%{prefix}/share/man/man1/tdm_greet.1*
%{prefix}/bin/tdecryptocardwatcher

# XDG user faces
%dir %{_datadir}/faces
%{_datadir}/faces/default1.png
%{_datadir}/faces/default2.png
%{_datadir}/faces/default3.png
%{_datadir}/faces/default4.png
%{_datadir}/faces/root1.png

# Distribution specific stuff
%{?with_systemd:%{_unitdir}/tdm.service}
%{_datadir}/xsessions/tde.desktop

%{_sysconfdir}/X11/wmsession.d/45TDE
%{_datadir}/X11/dm.d/45TDE.conf

# Logrotate configuration
%config %{_sysconfdir}/logrotate.d/trinity-tdm

%pre -n trinity-tdm
# Make sure that TDM configuration files are now under '/etc/trinity/tdm'
if [ -d "%{prefix}/share/config/tdm" ] && [ ! -L "%{prefix}/share/config/tdm" ]; then
  if [ -d "%{_sysconfdir}/trinity/tdm" ]; then
    # If there is already something under '/etc/trinity/tdm', simply delete old configuration
    echo "Deleting TDM configuration under '%{prefix}/share/config/tdm'"
    rm -rf "%{prefix}/share/config/tdm"
  else
    # Else, move '/opt/trinity/share/config/tdm' to '/etc/trinity/tdm'
    if [ ! -d "%{_sysconfdir}/trinity" ]; then
      mkdir -p "%{_sysconfdir}/trinity"
    fi
    echo "Migrating TDM configuration from '%{prefix}/share/config/tdm' to '%{_sysconfdir}/trinity/tdm'"
    mv -f "%{prefix}/share/config/tdm" "%{_sysconfdir}/trinity/tdm.migr"
  fi
fi

# Remove actual directory before creating a symlink
if [ ! -L "%{prefix}/share/apps/tdm/pics/users" ] && [ -d "%{prefix}/share/apps/tdm/pics/users" ] ; then
  [ -d "%{_datadir}/faces" ] || mkdir -p "%{_datadir}/faces"
  cp -f "%{prefix}/share/apps/tdm/pics/users/"* "%{_datadir}/faces"
  rm -rf "%{prefix}/share/apps/tdm/pics/users"
fi

%post -n trinity-tdm
%make_session

# Sets default user icon in TDM
if [ ! -r "%{prefix}/share/apps/tdm/faces/.default.face.icon" ]; then
  [ -d "%{prefix}/share/apps/tdm/faces" ] || mkdir -p "%{prefix}/share/apps/tdm/faces"
  cp -f "%{prefix}/share/apps/tdm/pics/users/default2.png" "%{prefix}/share/apps/tdm/faces/.default.face.icon"
fi

# Sets default language for TDM
if [ "$1" = "1" ]; then
  if [ -n "${LANG}" ] && [ "${LANG}" != "C" ]; then
    sed -i "%{_sysconfdir}/trinity/tdm/tdmrc" -e "s|^#*Language=.*|Language=${LANG}|"
  fi
fi

%posttrans -n trinity-tdm
# Make sure that TDM configuration files are now under '/etc/trinity/tdm'
if [ -d "%{_sysconfdir}/trinity/tdm.migr" ] && [ -d "%{_sysconfdir}/trinity/tdm" ]; then
  mv -f "%{_sysconfdir}/trinity/tdm.migr/"* "%{_sysconfdir}/trinity/tdm/"
  rmdir "%{_sysconfdir}/trinity/tdm.migr/"
fi

%postun -n trinity-tdm
%make_session

%package -n trinity-tdm-devel
Summary:	Development files for tdm
Group:		Development/Libraries/Other
Requires:	trinity-tdm = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

%description -n trinity-tdm-devel
This package contains the development files for TDM.

%files -n trinity-tdm-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/kgreeterplugin.h

##########

%package -n trinity-kfind
Summary:	File-find utility for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kfind
kfind can be used to find files and directories on your
workstations.

%files -n trinity-kfind
%defattr(-,root,root,-)
%{prefix}/bin/kfind
%{prefix}/%{_lib}/trinity/libkfindpart.la
%{prefix}/%{_lib}/trinity/libkfindpart.so
%{prefix}/share/applications/tde/Kfind.desktop
%{prefix}/share/apps/kfindpart/
%{prefix}/share/icons/hicolor/*/apps/kfind.png
%{prefix}/share/services/kfindpart.desktop
%{prefix}/share/servicetypes/findpart.desktop
%{prefix}/share/doc/tde/HTML/en/kfind/
%{prefix}/share/man/man1/kfind.1*

##########

%package -n trinity-khelpcenter
Summary:	Help center for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	htdig

%description -n trinity-khelpcenter
The TDE Help Center provides documentation on how to use the TDE desktop.

The htdig package is needed to build a searchable archive of TDE
documentation.

%files -n trinity-khelpcenter
%defattr(-,root,root,-)
%{prefix}/bin/khc_docbookdig.pl
%{prefix}/bin/khc_htdig.pl
%{prefix}/bin/khc_htsearch.pl
%{prefix}/bin/khc_indexbuilder
%{prefix}/bin/khc_mansearch.pl
%{prefix}/bin/khelpcenter
%{prefix}/%{_lib}/trinity/khelpcenter.la
%{prefix}/%{_lib}/trinity/khelpcenter.so
%{prefix}/%{_lib}/libtdeinit_khelpcenter.la
%{prefix}/%{_lib}/libtdeinit_khelpcenter.so
%{prefix}/share/applications/tde/Help.desktop
%{prefix}/share/apps/khelpcenter/
%{prefix}/share/config.kcfg/khelpcenter.kcfg
%{prefix}/share/icons/hicolor/*/apps/khelpcenter.*
%{prefix}/share/services/khelpcenter.desktop
%{prefix}/share/doc/tde/HTML/en/khelpcenter/

##########

%package -n trinity-kicker
Summary:	Desktop panel for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kicker
Kicker provides the TDE panel on you desktop. It can be used as a
program launcher and can load plugins to provide additional
functionality.

%files -n trinity-kicker
%defattr(-,root,root,-)
%{prefix}/bin/appletproxy
%{prefix}/bin/extensionproxy
%{prefix}/bin/kasbar
%{prefix}/bin/kicker
%{prefix}/%{_lib}/tdeconf_update_bin/kicker-3.4-reverseLayout
%{prefix}/%{_lib}/trinity/appletproxy.la
%{prefix}/%{_lib}/trinity/appletproxy.so
%{prefix}/%{_lib}/trinity/clock_panelapplet.la
%{prefix}/%{_lib}/trinity/clock_panelapplet.so
%{prefix}/%{_lib}/trinity/dockbar_panelextension.la
%{prefix}/%{_lib}/trinity/dockbar_panelextension.so
%{prefix}/%{_lib}/trinity/extensionproxy.la
%{prefix}/%{_lib}/trinity/extensionproxy.so
%{prefix}/%{_lib}/trinity/kasbar_panelextension.la
%{prefix}/%{_lib}/trinity/kasbar_panelextension.so
%{prefix}/%{_lib}/trinity/kicker.la
%{prefix}/%{_lib}/trinity/kickermenu_find.la
%{prefix}/%{_lib}/trinity/kickermenu_find.so
%{prefix}/%{_lib}/trinity/kickermenu_kate.so
%{prefix}/%{_lib}/trinity/kickermenu_kate.la
%{prefix}/%{_lib}/trinity/kickermenu_tdeprint.la
%{prefix}/%{_lib}/trinity/kickermenu_tdeprint.so
%{prefix}/%{_lib}/trinity/kickermenu_konqueror.la
%{prefix}/%{_lib}/trinity/kickermenu_konqueror.so
%{prefix}/%{_lib}/trinity/kickermenu_konsole.la
%{prefix}/%{_lib}/trinity/kickermenu_konsole.so
%{prefix}/%{_lib}/trinity/kickermenu_prefmenu.la
%{prefix}/%{_lib}/trinity/kickermenu_prefmenu.so
%{prefix}/%{_lib}/trinity/kickermenu_recentdocs.la
%{prefix}/%{_lib}/trinity/kickermenu_recentdocs.so
%{prefix}/%{_lib}/trinity/kickermenu_remotemenu.la
%{prefix}/%{_lib}/trinity/kickermenu_remotemenu.so
%{prefix}/%{_lib}/trinity/kickermenu_systemmenu.la
%{prefix}/%{_lib}/trinity/kickermenu_systemmenu.so
%{prefix}/%{_lib}/trinity/kicker.so
%{prefix}/%{_lib}/trinity/launcher_panelapplet.la
%{prefix}/%{_lib}/trinity/launcher_panelapplet.so
%{prefix}/%{_lib}/trinity/lockout_panelapplet.la
%{prefix}/%{_lib}/trinity/lockout_panelapplet.so
%{prefix}/%{_lib}/trinity/media_panelapplet.la
%{prefix}/%{_lib}/trinity/media_panelapplet.so
%{prefix}/%{_lib}/trinity/menu_panelapplet.la
%{prefix}/%{_lib}/trinity/menu_panelapplet.so
%{prefix}/%{_lib}/trinity/minipager_panelapplet.la
%{prefix}/%{_lib}/trinity/minipager_panelapplet.so
%{prefix}/%{_lib}/trinity/naughty_panelapplet.la
%{prefix}/%{_lib}/trinity/naughty_panelapplet.so
%{prefix}/%{_lib}/trinity/run_panelapplet.la
%{prefix}/%{_lib}/trinity/run_panelapplet.so
%{prefix}/%{_lib}/trinity/sidebar_panelextension.la
%{prefix}/%{_lib}/trinity/sidebar_panelextension.so
%{prefix}/%{_lib}/trinity/systemtray_panelapplet.la
%{prefix}/%{_lib}/trinity/systemtray_panelapplet.so
%{prefix}/%{_lib}/trinity/taskbar_panelapplet.la
%{prefix}/%{_lib}/trinity/taskbar_panelapplet.so
%{prefix}/%{_lib}/trinity/taskbar_panelextension.la
%{prefix}/%{_lib}/trinity/taskbar_panelextension.so
%{prefix}/%{_lib}/trinity/trash_panelapplet.la
%{prefix}/%{_lib}/trinity/trash_panelapplet.so
%{prefix}/%{_lib}/libkasbar.so.*
%{prefix}/%{_lib}/libtdeinit_appletproxy.la
%{prefix}/%{_lib}/libtdeinit_appletproxy.so
%{prefix}/%{_lib}/libtdeinit_extensionproxy.la
%{prefix}/%{_lib}/libtdeinit_extensionproxy.so
%{prefix}/%{_lib}/libtdeinit_kicker.la
%{prefix}/%{_lib}/libtdeinit_kicker.so
%{prefix}/%{_lib}/libkickermain.so.*
%{prefix}/%{_lib}/libtaskbar.so.*
%{prefix}/%{_lib}/libtaskmanager.so.*
%{prefix}/%{_lib}/libkickoffsearch_interfaces.so.*
%{prefix}/share/applications/tde/kcmkicker.desktop
%{prefix}/share/applnk/.hidden/kicker_config_arrangement.desktop
%{prefix}/share/applnk/.hidden/kicker_config_hiding.desktop
%{prefix}/share/applnk/.hidden/kicker_config_menus.desktop
%{prefix}/share/apps/clockapplet/
%{prefix}/share/apps/tdeconf_update/kicker-3.1-properSizeSetting.pl
%{prefix}/share/apps/tdeconf_update/kicker-3.5-taskbarEnums.pl
%{prefix}/share/apps/tdeconf_update/kickerrc.upd
%{prefix}/share/apps/kicker/
%exclude %{prefix}/share/apps/kicker/applets/klipper.desktop
%exclude %{prefix}/share/apps/kicker/applets/ksysguardapplet.desktop
%{prefix}/share/apps/naughtyapplet/
%{prefix}/share/autostart/panel.desktop
%{prefix}/share/config.kcfg/kickerSettings.kcfg
%{prefix}/share/config.kcfg/launcherapplet.kcfg
%{prefix}/share/config.kcfg/pagersettings.kcfg
%{prefix}/share/config.kcfg/taskbar.kcfg
%{prefix}/share/icons/crystalsvg/*/apps/systemtray.png
%{prefix}/share/icons/crystalsvg/*/apps/taskbar.png
%{prefix}/share/icons/crystalsvg/*/apps/kbinaryclock.png
%{prefix}/share/icons/crystalsvg/*/apps/kdisknav.png
%{prefix}/share/icons/crystalsvg/*/apps/kicker.png
%{prefix}/share/icons/crystalsvg/*/apps/panel.png
%{prefix}/share/icons/crystalsvg/*/apps/runprocesscatcher.png
%{prefix}/share/icons/crystalsvg/*/apps/kbinaryclock.svgz
%{prefix}/share/icons/crystalsvg/*/apps/systemtray.svgz
%{prefix}/share/servicetypes/kickoffsearchplugin.desktop
%{prefix}/share/doc/tde/HTML/en/kicker/
%{prefix}/share/man/man1/appletproxy.1*
%{prefix}/share/man/man1/extensionproxy.1*
%{prefix}/share/man/man1/kasbar.1*
%{prefix}/share/man/man1/kicker.1*

##########

%package -n trinity-kicker-devel
Summary:	Development files for kicker
Group:		Development/Libraries/Other
Requires:	trinity-kicker = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

%description -n trinity-kicker-devel
This package contains the development files for kicker.

%files -n trinity-kicker-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/kickoff-search-plugin.h
%{prefix}/include/tde/kickoffsearchinterface.h
%{prefix}/%{_lib}/libkasbar.la
%{prefix}/%{_lib}/libkasbar.so
%{prefix}/%{_lib}/libkickermain.la
%{prefix}/%{_lib}/libkickermain.so
%{prefix}/%{_lib}/libkickoffsearch_interfaces.la
%{prefix}/%{_lib}/libkickoffsearch_interfaces.so
%{prefix}/%{_lib}/libtaskbar.la
%{prefix}/%{_lib}/libtaskbar.so
%{prefix}/%{_lib}/libtaskmanager.la
%{prefix}/%{_lib}/libtaskmanager.so

##########

%package -n trinity-klipper
Summary:	Clipboard utility for Trinity
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-klipper
klipper provides standard clipboard functions (cut and paste, history
saving) plus additional features, like the ability to offer actions to 
take dependent on the clipboard contents. For example, it can launch a 
web browser if the clipboard contains a URL.

%files -n trinity-klipper
%defattr(-,root,root,-)
%{prefix}/bin/klipper
%config(noreplace) %{_sysconfdir}/trinity/klipperrc
%{prefix}/%{_lib}/trinity/klipper.la
%{prefix}/%{_lib}/trinity/klipper.so
%{prefix}/%{_lib}/trinity/klipper_panelapplet.la
%{prefix}/%{_lib}/trinity/klipper_panelapplet.so
%{prefix}/%{_lib}/libtdeinit_klipper.la
%{prefix}/%{_lib}/libtdeinit_klipper.so
%{prefix}/share/applications/tde/klipper.desktop
%{prefix}/share/apps/tdeconf_update/klipper-1-2.pl
%{prefix}/share/apps/tdeconf_update/klipper-trinity1.sh
%{prefix}/share/apps/tdeconf_update/klipperrc.upd
%{prefix}/share/apps/tdeconf_update/klippershortcuts.upd
%{prefix}/share/apps/kicker/applets/klipper.desktop
%{prefix}/share/autostart/klipper.desktop
%{prefix}/share/icons/hicolor/*/apps/klipper.*
%{prefix}/share/doc/tde/HTML/en/klipper/

##########

%package -n trinity-kmenuedit
Summary:	Menu editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kmenuedit
The TDE menu editor allows you to make customisations to the TDE menu
structure.

%files -n trinity-kmenuedit
%defattr(-,root,root,-)
%{prefix}/bin/kcontroledit
%{prefix}/bin/kmenuedit
%{prefix}/%{_lib}/trinity/kcontroledit.la
%{prefix}/%{_lib}/trinity/kcontroledit.so
%{prefix}/%{_lib}/trinity/kmenuedit.la
%{prefix}/%{_lib}/trinity/kmenuedit.so
%{prefix}/%{_lib}/libtdeinit_kcontroledit.la
%{prefix}/%{_lib}/libtdeinit_kcontroledit.so
%{prefix}/%{_lib}/libtdeinit_kmenuedit.la
%{prefix}/%{_lib}/libtdeinit_kmenuedit.so
%{prefix}/share/applications/tde/kmenuedit.desktop
%{prefix}/share/applnk/System/kmenuedit.desktop
%{prefix}/share/apps/kcontroledit/
%{prefix}/share/apps/kmenuedit/
%{prefix}/share/doc/tde/HTML/en/kmenuedit/
%{prefix}/share/man/man1/kmenuedit.1*

##########

%package -n trinity-konqueror
Summary:	TDE's advanced file manager, web browser and document viewer
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kcontrol = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kdesktop = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kfind = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konqueror
Konqueror is the file manager for the Trinity Desktop Environment.
It supports basic file management on local UNIX filesystems,
from simple cut/copy and paste operations to advanced remote
and local network file browsing.

It is also the canvas for all the latest TDE technology,
from KIO slaves (which provide mechanisms for file access) to
component embedding via the KParts object interface, and it
is one of the most customizable applications available.

Konqueror is an Open Source web browser with HTML4.0 compliance,
supporting Java applets, JavaScript, CSS1 and (partially) CSS2,
as well as Netscape plugins (for example, Flash or RealVideo plugins).

It is a universal viewing application, capable of embedding
read-only viewing components in itself to view documents without
ever launching another application.

%files -n trinity-konqueror
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/konqsidebartng.rc
%{prefix}/bin/kbookmarkmerger
%{prefix}/bin/keditbookmarks
%{prefix}/bin/kfmclient
%{prefix}/bin/konqueror
%{prefix}/%{_lib}/trinity/kcm_history.la
%{prefix}/%{_lib}/trinity/kcm_history.so
%{prefix}/%{_lib}/trinity/kded_konqy_preloader.la
%{prefix}/%{_lib}/trinity/kded_konqy_preloader.so
%{prefix}/%{_lib}/trinity/keditbookmarks.la
%{prefix}/%{_lib}/trinity/keditbookmarks.so
%{prefix}/%{_lib}/trinity/kfmclient.la
%{prefix}/%{_lib}/trinity/kfmclient.so
%{prefix}/%{_lib}/trinity/konq_aboutpage.la
%{prefix}/%{_lib}/trinity/konq_aboutpage.so
%{prefix}/%{_lib}/trinity/konq_iconview.la
%{prefix}/%{_lib}/trinity/konq_iconview.so
%{prefix}/%{_lib}/trinity/konq_listview.la
%{prefix}/%{_lib}/trinity/konq_listview.so
%{prefix}/%{_lib}/trinity/konq_remoteencoding.la
%{prefix}/%{_lib}/trinity/konq_remoteencoding.so
%{prefix}/%{_lib}/trinity/konq_shellcmdplugin.la
%{prefix}/%{_lib}/trinity/konq_shellcmdplugin.so
%{prefix}/%{_lib}/trinity/konq_sidebar.la
%{prefix}/%{_lib}/trinity/konq_sidebar.so
%{prefix}/%{_lib}/trinity/konq_sidebartree_bookmarks.la
%{prefix}/%{_lib}/trinity/konq_sidebartree_bookmarks.so
%{prefix}/%{_lib}/trinity/konq_sidebartree_dirtree.la
%{prefix}/%{_lib}/trinity/konq_sidebartree_dirtree.so
%{prefix}/%{_lib}/trinity/konq_sidebartree_history.la
%{prefix}/%{_lib}/trinity/konq_sidebartree_history.so
%{prefix}/%{_lib}/trinity/konqsidebar_tree.la
%{prefix}/%{_lib}/trinity/konqsidebar_tree.so
%{prefix}/%{_lib}/trinity/konqsidebar_web.la
%{prefix}/%{_lib}/trinity/konqsidebar_web.so
%{prefix}/%{_lib}/trinity/konqueror.la
%{prefix}/%{_lib}/trinity/konqueror.so
%{prefix}/%{_lib}/trinity/libtdehtmlkttsdplugin.la
%{prefix}/%{_lib}/trinity/libtdehtmlkttsdplugin.so
%{prefix}/%{_lib}/libtdeinit_keditbookmarks.la
%{prefix}/%{_lib}/libtdeinit_keditbookmarks.so
%{prefix}/%{_lib}/libtdeinit_kfmclient.la
%{prefix}/%{_lib}/libtdeinit_kfmclient.so
%{prefix}/%{_lib}/libtdeinit_konqueror.la
%{prefix}/%{_lib}/libtdeinit_konqueror.so
%{prefix}/%{_lib}/libkonqsidebarplugin.so.*
%{prefix}/share/applications/tde/Home.desktop
%{prefix}/share/applications/tde/kcmhistory.desktop
%{prefix}/share/applications/tde/kfmclient.desktop
%{prefix}/share/applications/tde/kfmclient_dir.desktop
%{prefix}/share/applications/tde/kfmclient_html.desktop
%{prefix}/share/applications/tde/kfmclient_war.desktop
%{prefix}/share/applications/tde/tdehtml_filter.desktop
%{prefix}/share/applications/tde/konqbrowser.desktop
%{prefix}/share/applications/tde/konquerorsu.desktop
%{prefix}/share/applnk/.hidden/konqfilemgr.desktop
%{prefix}/share/applnk/Internet/keditbookmarks.desktop
%{prefix}/share/applnk/konqueror.desktop
%{prefix}/share/apps/tdeconf_update/kfmclient_3_2.upd
%{prefix}/share/apps/tdeconf_update/kfmclient_3_2_update.sh
%{prefix}/share/apps/tdeconf_update/konqsidebartng.upd
%{prefix}/share/apps/tdeconf_update/move_konqsidebartng_entries.sh
%{prefix}/share/apps/keditbookmarks/
%{prefix}/share/apps/tdehtml/kpartplugins/
%{prefix}/share/apps/konqiconview/
%{prefix}/share/apps/konqlistview/
%exclude %{prefix}/share/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{prefix}/share/apps/konqsidebartng/
%{prefix}/share/apps/konqueror/about/
%dir %{prefix}/share/apps/konqueror/dirtree
%dir %{prefix}/share/apps/konqueror/dirtree/remote
%{prefix}/share/apps/konqueror/icons/
%{prefix}/share/apps/konqueror/konq-simplebrowser.rc
%{prefix}/share/apps/konqueror/konqueror.rc
%{prefix}/share/apps/konqueror/pics/indicator_connect.png
%{prefix}/share/apps/konqueror/pics/indicator_empty.png
%{prefix}/share/apps/konqueror/pics/indicator_noconnect.png
%{prefix}/share/apps/konqueror/pics/indicator_viewactive.png
%{prefix}/share/apps/konqueror/profiles/
%exclude %{prefix}/share/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%exclude %{prefix}/share/apps/konqueror/servicemenus/installfont.desktop
%{prefix}/share/apps/konqueror/servicemenus/*.desktop
%ghost %{_sysconfdir}/alternatives/media_safelyremove.desktop
%{prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase
%{prefix}/share/apps/konqueror/tiles/
%{prefix}/share/autostart/konqy_preload.desktop
%{prefix}/share/config.kcfg/keditbookmarks.kcfg
%{prefix}/share/config.kcfg/konq_listview.kcfg
%{prefix}/share/config.kcfg/konqueror.kcfg
%{prefix}/share/icons/crystalsvg/*/apps/keditbookmarks.png
%{prefix}/share/icons/crystalsvg/*/apps/kfm_home.svgz
%{prefix}/share/icons/hicolor/*/apps/kfm.png
%{prefix}/share/icons/hicolor/*/apps/konqueror.*
%{prefix}/share/services/kded/konqy_preloader.desktop
%{prefix}/share/services/konq_*.desktop
%{prefix}/share/servicetypes/konqaboutpage.desktop
%{prefix}/share/doc/tde/HTML/en/konqueror/
%{prefix}/share/doc/tde/HTML/en/keditbookmarks/
%{prefix}/share/man/man1/keditbookmarks.1*
%{prefix}/share/man/man1/kfmclient.1*
%{prefix}/share/man/man1/konqueror.1*

%post -n trinity-konqueror
if [ $1 -eq 1 ]; then
  update-alternatives --install \
    %{prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop \
    media_safelyremove.desktop_konqueror \
    %{prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase \
    10 || :
fi

%preun -n trinity-konqueror
if [ $1 -eq 0 ]; then
  update-alternatives --remove \
    media_safelyremove.desktop_konqueror \
    %{prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase || :
fi

##########

%package -n trinity-konqueror-devel
Summary:	Development files for konqueror
Group:		Development/Libraries/Other
Requires:	trinity-konqueror = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konqueror-devel
This package contains the development files for konqueror.

%files -n trinity-konqueror-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/konqsidebarplugin.h
%{prefix}/include/tde/KonquerorIface.h
%{prefix}/%{_lib}/libkonqsidebarplugin.la
%{prefix}/%{_lib}/libkonqsidebarplugin.so

##########

%package -n trinity-konqueror-nsplugins
Summary:	Netscape plugin support for Konqueror
Group:		System/GUI/Other
Requires:	trinity-konqueror = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konqueror-nsplugins
This package includes support for Netscape plugins in Konqueror.

%files -n trinity-konqueror-nsplugins
%defattr(-,root,root,-)
%{prefix}/bin/nspluginscan
%{prefix}/bin/nspluginviewer
%{prefix}/%{_lib}/trinity/kcm_nsplugins.la
%{prefix}/%{_lib}/trinity/kcm_nsplugins.so
%{prefix}/%{_lib}/trinity/libnsplugin.la
%{prefix}/%{_lib}/trinity/libnsplugin.so
%{prefix}/share/applications/tde/tdehtml_plugins.desktop
%{prefix}/share/apps/plugin/nspluginpart.rc

##########

%package -n trinity-konsole
Summary:	X terminal emulator for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-konsole
Konsole is an X terminal emulation which provides a command-line interface
(CLI) while using the graphical Trinity Desktop Environment. Konsole helps to
better organize user's desktop by containing multiple sessions in a single
window (a less cluttered desktop).

Its advanced features include a simple configuration and the ability to use
multiple terminal shells in a single window

Using Konsole, a user can open:
* Linux console sessions
* Midnight Commander file manager sessions
* Shell sessions
* Root consoles sessions

%files -n trinity-konsole
%defattr(-,root,root,-)
%{prefix}/bin/konsole
%{prefix}/bin/terminalhere
%{prefix}/%{_lib}/trinity/kcm_konsole.la
%{prefix}/%{_lib}/trinity/kcm_konsole.so
%{prefix}/%{_lib}/trinity/kded_kwrited.la
%{prefix}/%{_lib}/trinity/kded_kwrited.so
%{prefix}/%{_lib}/trinity/konsole.la
%{prefix}/%{_lib}/trinity/konsole.so
%{prefix}/%{_lib}/trinity/libkonsolepart.la
%{prefix}/%{_lib}/trinity/libkonsolepart.so
%{prefix}/%{_lib}/libtdeinit_konsole.la
%{prefix}/%{_lib}/libtdeinit_konsole.so
%{prefix}/share/applications/tde/konsole.desktop
%{prefix}/share/applications/tde/konsolesu.desktop
%{prefix}/share/applnk/.hidden/kcmkonsole.desktop
%{prefix}/share/apps/tdeconf_update/konsole.upd
%{prefix}/share/apps/tdeconf_update/schemaStrip.pl
%{prefix}/share/apps/konsole/
%{prefix}/share/icons/hicolor/*/apps/konsole.*
%{prefix}/share/mimelnk/application/x-konsole.desktop
%{prefix}/share/services/kded/kwrited.desktop
%{prefix}/share/services/konsolepart.desktop
%{prefix}/share/services/konsole-script.desktop
%{prefix}/share/services/kwrited.desktop
%{prefix}/share/servicetypes/terminalemulator.desktop
%{prefix}/share/doc/tde/HTML/en/konsole/
%{prefix}/share/doc/tde/HTML/en/kcontrol/kcmkonsole/
%config %{_sysconfdir}/fonts/conf.d/99-konsole.conf
%{prefix}/share/man/man1/konsole.1*

##########

%package -n trinity-kpager
Summary:	Desktop pager for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kpager
This package contains TDE's desktop pager, which displays your virtual
desktops iconically in a window, along with icons of any running
applications. It is used to switch between applications or desktops.

%files -n trinity-kpager
%defattr(-,root,root,-)
%{prefix}/bin/kpager
%{prefix}/share/applications/tde/kpager.desktop
%{prefix}/share/applnk/Utilities/kpager.desktop
%{prefix}/share/icons/hicolor/*/apps/kpager.png
%{prefix}/share/doc/tde/HTML/en/kpager/
%{prefix}/share/man/man1/kpager.1*

##########

%package -n trinity-kpersonalizer
Summary:	Installation personalizer for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kpersonalizer
TDE Personalizer is the application that configures the TDE desktop for you.
It's a very useful wizard that allows you to quickly change the TDE desktop to
suit your own needs. When you run TDE for the first time, KPersonalizer is
automatically started. KPersonalizer can also be called later.

%files -n trinity-kpersonalizer
%defattr(-,root,root,-)
%{prefix}/bin/kpersonalizer
%{prefix}/share/applications/tde/kpersonalizer.desktop
%{prefix}/share/applnk/System/kpersonalizer.desktop
%{prefix}/share/apps/kpersonalizer/
%{prefix}/share/icons/crystalsvg/*/apps/kpersonalizer.png
%{prefix}/share/man/man1/kpersonalizer.1*

##########

%package -n trinity-ksmserver
Summary:	Session manager for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-twin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	xmessage
Requires:	xprop

%description -n trinity-ksmserver
This package contains the TDE session manager. It is responsible for
restoring your TDE session on login. It is also needed to properly
start a TDE session. It registers TDE with X display managers, and
provides the 'starttde' command, for starting an X session with TDE
from the console.

If you are running TDE for the first time for a certain user,
kpersonalizer is used to help with setup. If it is not present,
TDE will start, but many good defaults will not be set.

%files -n trinity-ksmserver
%defattr(-,root,root,-)
%{prefix}/bin/ksmserver
%{prefix}/bin/starttde
%{prefix}/bin/migratekde3
%{prefix}/bin/r14-xdg-update
%{prefix}/bin/tdeinit_displayconfig
%{prefix}/bin/tdeinit_phase1
%{prefix}/%{_lib}/trinity/ksmserver.la
%{prefix}/%{_lib}/trinity/ksmserver.so
%{prefix}/%{_lib}/libtdeinit_ksmserver.la
%{prefix}/%{_lib}/libtdeinit_ksmserver.so
%{prefix}/share/apps/tdeconf_update/ksmserver.upd
%{prefix}/share/apps/tdeconf_update/move_session_config.sh
%{prefix}/share/apps/ksmserver/
%{prefix}/share/man/man1/starttde.1*


##########

%package -n trinity-ksplash
Summary:	The TDE splash screen
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksplash
This package includes the TDE Splash screen, which is seen when
a TDE session is launched.

%files -n trinity-ksplash
%defattr(-,root,root,-)
%{prefix}/bin/ksplash
%{prefix}/bin/ksplashsimple
%{prefix}/%{_lib}/trinity/kcm_ksplashthemes.la
%{prefix}/%{_lib}/trinity/kcm_ksplashthemes.so
%{prefix}/%{_lib}/trinity/ksplashdefault.la
%{prefix}/%{_lib}/trinity/ksplashdefault.so
%{prefix}/%{_lib}/trinity/ksplashunified.la
%{prefix}/%{_lib}/trinity/ksplashunified.so
%{prefix}/%{_lib}/trinity/ksplashredmond.la
%{prefix}/%{_lib}/trinity/ksplashredmond.so
%{prefix}/%{_lib}/trinity/ksplashstandard.la
%{prefix}/%{_lib}/trinity/ksplashstandard.so
%{prefix}/%{_lib}/libksplashthemes.so.*
%{prefix}/share/applications/tde/ksplashthememgr.desktop
%{prefix}/share/apps/ksplash
%{prefix}/share/services/ksplashdefault.desktop
%{prefix}/share/services/ksplash.desktop
%{prefix}/share/services/ksplashunified.desktop
%{prefix}/share/services/ksplashredmond.desktop
%{prefix}/share/services/ksplashstandard.desktop
%{prefix}/share/servicetypes/ksplashplugins.desktop
%{prefix}/share/doc/tde/HTML/en/ksplashml/

##########

%package -n trinity-ksplash-devel
Summary:	Development files for ksplash
Group:		Development/Libraries/Other
Requires:	trinity-ksplash = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksplash-devel
This package contains the development files for ksplash.

%files -n trinity-ksplash-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/ksplash/
%{prefix}/%{_lib}/libksplashthemes.la
%{prefix}/%{_lib}/libksplashthemes.so

##########

%package -n trinity-ksysguard
Summary:	System guard for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-ksysguardd = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksysguard
TDE System Guard allows you to monitor various statistics about your
computer.

%files -n trinity-ksysguard
%defattr(-,root,root,-)
%{prefix}/bin/kpm
%{prefix}/bin/ksysguard
%{prefix}/%{_lib}/trinity/sysguard_panelapplet.la
%{prefix}/%{_lib}/trinity/sysguard_panelapplet.so
%{prefix}/%{_lib}/libksgrd.so.*
%{prefix}/share/applications/tde/ksysguard.desktop
%{prefix}/share/apps/kicker/applets/ksysguardapplet.desktop
%{prefix}/share/apps/ksysguard/
%{prefix}/share/icons/crystalsvg/*/apps/ksysguard.png
%{prefix}/share/mimelnk/application/x-ksysguard.desktop
%{prefix}/share/doc/tde/HTML/en/ksysguard/

##########

%package -n trinity-ksysguard-devel
Summary:	Development files for ksysguard
Group:		Development/Libraries/Other
Requires:	trinity-ksysguard = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksysguard-devel
This package contains the development files for ksysguard.

%files -n trinity-ksysguard-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/ksgrd/
%{prefix}/%{_lib}/libksgrd.la
%{prefix}/%{_lib}/libksgrd.so

##########

%package -n trinity-ksysguardd
Summary:	System guard daemon for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ksysguardd
TDE System Guard Daemon is the daemon part of ksysguard. The daemon can
be installed on a remote machine to enable ksysguard on another machine
to monitor it through the daemon running there.

%files -n trinity-ksysguardd
%defattr(-,root,root,-)
%{prefix}/bin/ksysguardd
%config(noreplace) %{_sysconfdir}/trinity/ksysguarddrc

##########

%package -n trinity-ktip
Summary:	Useful tips for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ktip
ktip provides many useful tips on using TDE when you log in.

%files -n trinity-ktip
%defattr(-,root,root,-)
%{prefix}/bin/ktip
%{prefix}/share/applications/tde/ktip.desktop
%{prefix}/share/applnk/Toys/ktip.desktop
%{prefix}/share/apps/tdewizard/
%{prefix}/share/autostart/ktip.desktop
%{prefix}/share/icons/hicolor/*/apps/ktip.*

##########

%package -n trinity-twin
Summary:	The TDE window manager
Group:		System/GUI/Other
Requires:	%{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-twin
This package contains the default X window manager for TDE.

%files -n trinity-twin
%defattr(-,root,root,-)
%{prefix}/bin/twin
%{prefix}/bin/twin_killer_helper
%{prefix}/bin/twin_resumer_helper
%{prefix}/bin/twin_rules_dialog
%{prefix}/%{_lib}/tdeconf_update_bin/twin_update_default_rules
%{prefix}/%{_lib}/tdeconf_update_bin/twin_update_window_settings
%{prefix}/%{_lib}/trinity/kcm_twin*.la
%{prefix}/%{_lib}/trinity/kcm_twin*.so
%{prefix}/%{_lib}/trinity/twin*.la
%{prefix}/%{_lib}/trinity/twin*.so
%{prefix}/%{_lib}/libtdecorations.so.*
%{prefix}/%{_lib}/libtdeinit_twin_rules_dialog.la
%{prefix}/%{_lib}/libtdeinit_twin_rules_dialog.so
%{prefix}/%{_lib}/libtdeinit_twin.la
%{prefix}/%{_lib}/libtdeinit_twin.so
%{prefix}/share/applications/tde/showdesktop.desktop
%{prefix}/share/applications/tde/twindecoration.desktop
%{prefix}/share/applications/tde/twinoptions.desktop
%{prefix}/share/applications/tde/twinrules.desktop
%{prefix}/share/applnk/.hidden/twinactions.desktop
%{prefix}/share/applnk/.hidden/twinactiveborders.desktop
%{prefix}/share/applnk/.hidden/twinadvanced.desktop
%{prefix}/share/applnk/.hidden/twinfocus.desktop
%{prefix}/share/applnk/.hidden/twinmoving.desktop
%{prefix}/share/applnk/.hidden/twintranslucency.desktop
%{prefix}/share/apps/tdeconf_update/twin3_plugin.pl
%{prefix}/share/apps/tdeconf_update/twin3_plugin.upd
%{prefix}/share/apps/tdeconf_update/twin_focus1.sh
%{prefix}/share/apps/tdeconf_update/twin_focus1.upd
%{prefix}/share/apps/tdeconf_update/twin_focus2.sh
%{prefix}/share/apps/tdeconf_update/twin_focus2.upd
%{prefix}/share/apps/tdeconf_update/twin_fsp_workarounds_1.upd
%{prefix}/share/apps/tdeconf_update/twiniconify.upd
%{prefix}/share/apps/tdeconf_update/twinsticky.upd
%{prefix}/share/apps/tdeconf_update/twin.upd
%{prefix}/share/apps/tdeconf_update/twinupdatewindowsettings.upd
%{prefix}/share/apps/tdeconf_update/pluginlibFix.pl
%{prefix}/share/apps/twin/
%{prefix}/share/config.kcfg/twin.kcfg
%{prefix}/share/icons/crystalsvg/*/apps/twin.png
%{prefix}/share/doc/tde/HTML/en/kompmgr/

##########

%package -n trinity-twin-devel
Summary:	Development files for twin
Group:		Development/Libraries/Other
Requires:	trinity-twin = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-twin-devel
This package contains the development files for twin.

%files -n trinity-twin-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/twin/
%{prefix}/include/tde/kcommondecoration.h
%{prefix}/include/tde/kdecoration.h
%{prefix}/include/tde/kdecoration_p.h
%{prefix}/include/tde/kdecoration_plugins_p.h
%{prefix}/include/tde/kdecorationfactory.h
%{prefix}/include/tde/KWinInterface.h
%{prefix}/%{_lib}/libtdecorations.la
%{prefix}/%{_lib}/libtdecorations.so

##########

%package -n trinity-libkonq
Summary:	Core libraries for Konqueror
Group:		System/GUI/Other

%description -n trinity-libkonq
These libraries are used by several TDE applications, most notably
Konqueror and the kdesktop package.

%files -n trinity-libkonq
%defattr(-,root,root,-)
%{prefix}/%{_lib}/trinity/kded_favicons.la
%{prefix}/%{_lib}/trinity/kded_favicons.so
%{prefix}/%{_lib}/trinity/konq_sound.la
%{prefix}/%{_lib}/trinity/konq_sound.so
%{prefix}/%{_lib}/libkonq.so.*
%{prefix}/share/apps/kbookmark/
%{prefix}/share/apps/tdeconf_update/favicons.upd
%{prefix}/share/apps/tdeconf_update/move_favicons.sh
%dir %{prefix}/share/apps/konqueror/pics
%{prefix}/share/apps/konqueror/pics/arrow_bottomleft.png
%{prefix}/share/apps/konqueror/pics/arrow_bottomright.png
%{prefix}/share/apps/konqueror/pics/arrow_topleft.png
%{prefix}/share/apps/konqueror/pics/arrow_topright.png
%{prefix}/share/apps/konqueror/pics/thumbnailfont_7x4.png
%{prefix}/share/services/kded/favicons.desktop
%{prefix}/share/servicetypes/konqpopupmenuplugin.desktop

##########

%package libtqt3-integration
Summary:	Integration library between TQt3 and TDE
Group:		System/GUI/Other

Obsoletes:	tdebase-libtqt3-integration < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdebase-libtqt3-integration = %{?epoch:%{epoch}:}%{version}-%{release}

%description libtqt3-integration
These libraries allow you to use TDE dialogs in native TQt3 applications.

%files libtqt3-integration
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/integration/
%{prefix}/%{_lib}/trinity/kded_tdeintegration.la
%{prefix}/%{_lib}/trinity/kded_tdeintegration.so
%{prefix}/share/services/kded/tdeintegration.desktop

##########

%package -n trinity-libkonq-devel
Summary:	Development files for Konqueror's core libraries
Group:		Development/Libraries/Other
Requires:	trinity-libkonq = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_xtst:Requires: pkgconfig(xtst)}

%description -n trinity-libkonq-devel
This package contains headers and other development files for the core
Konqueror libraries.

%files -n trinity-libkonq-devel
%defattr(-,root,root,-)
%{prefix}/include/tde/tdefileivi.h
%{prefix}/include/tde/kivdirectoryoverlay.h
%{prefix}/include/tde/kivfreespaceoverlay.h
%{prefix}/include/tde/knewmenu.h
%{prefix}/include/tde/konqbookmarkmanager.h
%{prefix}/include/tde/konq_*.h
%{prefix}/include/tde/libkonq_export.h
%{prefix}/%{_lib}/libkonq.la
%{prefix}/%{_lib}/libkonq.so

##########

%package tdeio-smb-plugin
Summary:	Windows Connection Module for TDE
Group:		System/GUI/Other

%description tdeio-smb-plugin
This package provides the "smb://" protocol, to connect to and from
Windows and Samba shares.

%files tdeio-smb-plugin
%defattr(-,root,root)
%{prefix}/%{_lib}/trinity/kcm_samba.la
%{prefix}/%{_lib}/trinity/kcm_samba.so
%{prefix}/%{_lib}/trinity/tdeio_smb.la
%{prefix}/%{_lib}/trinity/tdeio_smb.so
%{prefix}/share/services/smb.protocol
%{prefix}/share/apps/konqueror/dirtree/remote/smb-network.desktop
%dir %{prefix}/share/apps/remoteview
%{prefix}/share/apps/remoteview/smb-network.desktop
%{prefix}/share/mimelnk/application/x-smb-workgroup.desktop

%prep -a
# Applies an optional distro-specific graphical theme
%if "%{?tde_bg}" != ""
# TDM Background
%__sed -i "tdm/kfrontend/gentdmconf.c" \
	-e 's|"Wallpaper=isadora.png\n"|"Wallpaper=%{tde_bg}\n"|'

# TDE user default background
%__sed -i "kpersonalizer/keyecandypage.cpp" \
	-e 's|#define DEFAULT_WALLPAPER "isadora.png"|#define DEFAULT_WALLPAPER "%{tde_bg}"|'
%__sed -i "starttde" \
	-e 's|%{prefix}/share/wallpapers/Trinity-lineart.svg.desktop|%{tde_bg}|' \
	-e 's|Wallpaper=Trinity-lineart.svg|Wallpaper=%{tde_bg}|'
%endif

# TDE default directory and icon in startup script
%__sed -i "starttde" \
	-e "s|/opt/trinity|%{prefix}|g"

# Sets default TDE menu icon
%if "%{tde_starticon}" != ""
%__sed -i "kicker/libkicker/kickerSettings.kcfg" \
	-e "s|QString(\"kmenu\")|QString(\"%{tde_starticon}\")|"
%endif


# Reboot command location may vary on some distributions
if [ -x "/usr/bin/reboot" ]; then
  POWEROFF="/usr/bin/poweroff"
  REBOOT="/usr/bin/reboot"
elif [ -x "/usr/sbin/reboot" ]; then
  POWEROFF="/usr/sbin/poweroff"
  REBOOT="/usr/sbin/reboot"
fi
if [ -n "${REBOOT}" ]; then
  %__sed -i \
    "doc/tdm/tdmrc-ref.docbook" \
    "kcontrol/tdm/tdm-shut.cpp" \
    "tdm/config.def" \
  -e "s|/sbin/poweroff|${POWEROFF}|g" \
  -e "s|/sbin/reboot|${REBOOT}|g"
fi

# Update icons for some control center modules
%__sed -i "kcontrol/componentchooser/componentchooser.desktop"        -e "s|^Icon=.*|Icon=kcmcomponentchooser|"
%__sed -i "kcontrol/taskbar/kcmtaskbar.desktop"                       -e "s|^Icon=.*|Icon=kcmtaskbar|"
%__sed -i "kcontrol/nics/nic.desktop"                                 -e "s|^Icon=.*|Icon=kcmnic|"
%__sed -i "kcontrol/input/mouse.desktop"                              -e "s|^Icon=.*|Icon=kcmmouse|"
%__sed -i "kcontrol/smserver/kcmsmserver.desktop"                     -e "s|^Icon=.*|Icon=kcmsmserver|"
%__sed -i "kcontrol/kded/kcmkded.desktop"                             -e "s|^Icon=.*|Icon=kcmkded|"
%__sed -i "kcontrol/konq/desktop.desktop"                             -e "s|^Icon=.*|Icon=kcmdesktop|"
%__sed -i "kcontrol/konq/desktopbehavior.desktop"                     -e "s|^Icon=.*|Icon=kcmdesktopbehavior|"
%__sed -i "kcontrol/privacy/privacy.desktop"                          -e "s|^Icon=.*|Icon=kcmprivacy|"
%__sed -i "kcontrol/crypto/crypto.desktop"                            -e "s|^Icon=.*|Icon=kcmcrypto|"
%__sed -i "kcontrol/tdeio/netpref.desktop"                            -e "s|^Icon=.*|Icon=kcmnetpref|"
%__sed -i "kcontrol/konqhtml/tdehtml_filter.desktop"                  -e "s|^Icon=.*|Icon=kcmkhtml_filter|"
%__sed -i "kcontrol/joystick/joystick.desktop"                        -e "s|^Icon=.*|Icon=kcmjoystick|"
%__sed -i "kcontrol/colors/colors.desktop"                            -e "s|^Icon=.*|Icon=kcmcolors|"
%__sed -i "kcontrol/performance/kcmperformance.desktop"               -e "s|^Icon=.*|Icon=kcmperformance|"
%__sed -i "kcontrol/launch/kcmlaunch.desktop"                         -e "s|^Icon=.*|Icon=kcmlaunch|"
%__sed -i "kcontrol/dnssd/kcm_tdednssd.desktop"                       -e "s|^Icon=.*|Icon=kcmkdnssd|"
%__sed -i "kcontrol/spellchecking/spellchecking.desktop"              -e "s|^Icon=.*|Icon=kcmspellchecking|"
%__sed -i "konqueror/sidebar/trees/history_module/kcmhistory.desktop" -e "s|^Icon=.*|Icon=kcmhistory|"
%__sed -i "tdeioslave/cgi/kcmcgi/kcmcgi.desktop"                      -e "s|^Icon=.*|Icon=kcmcgi|"
%__sed -i "tdeioslave/media/tdecmodule/media.desktop"                 -e "s|^Icon=.*|Icon=kcmmedia|" 


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"

%install -p
# Symlinks 'usb.ids' (Use system-provided version, not TDE provided version)
%__mkdir_p %{?buildroot}%{prefix}/share/apps/
%__ln_s -f "/usr/share/hwdata/usb.ids" "%{?buildroot}%{prefix}/share/apps/usb.ids"

# Console font to fontconfig
%__mkdir_p "%{buildroot}%{_sysconfdir}/fonts/conf.d"
cat <<EOF >"%{buildroot}%{_sysconfdir}/fonts/conf.d/99-konsole.conf"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <!-- Font directory list -->
  <dir>%{prefix}/share/apps/konsole/fonts</dir>
</fontconfig>
EOF

# logrotate configuration
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat << EOF > "%{buildroot}%{_sysconfdir}/logrotate.d/trinity-tdm"
/var/log/tdm.log {
    weekly
    notifempty
    missingok
    nocompress
}
EOF

# Adds missing icons in 'hicolor' theme
# These icons are copied from 'crystalsvg' theme, provided by 'tdelibs'.
%__mkdir_p "%{?buildroot}%{prefix}/share/icons/hicolor/"{16x16,22x22,32x32,48x48,64x64,128x128}"/apps/"
pushd "%{?buildroot}%{prefix}/share/icons"
for i in {16,32,48,64,128};    do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/mimetypes/application-vnd.tde.misc.png  hicolor/"$i"x"$i"/apps/kcmcomponentchooser.png  ;done
for i in {16,22,32,48,128};    do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/launch.png                      hicolor/"$i"x"$i"/apps/kcmperformance.png       ;done
for i in 16;                   do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/services.png                    hicolor/"$i"x"$i"/apps/kcmkded.png              ;done
for i in {16,22,32,48};        do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/system-log-out.png              hicolor/"$i"x"$i"/apps/kcmsmserver.png          ;done
for i in {16,22,32};           do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/tools-check-spelling.png        hicolor/"$i"x"$i"/apps/kcmspellchecking.png     ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/places/desktop.png                      hicolor/"$i"x"$i"/apps/kcmdesktopbehavior.png   ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/places/desktop.png                      hicolor/"$i"x"$i"/apps/kcmdesktop.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/kmenu.png                          hicolor/"$i"x"$i"/apps/kcmtaskbar.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/mimetypes/application-x-kcsrc.png       hicolor/"$i"x"$i"/apps/kcmcolors.png            ;done
for i in {16,22,32,48,128};    do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/launch.png                      hicolor/"$i"x"$i"/apps/kcmlaunch.png            ;done
for i in {16,22,32};           do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/filter.png                      hicolor/"$i"x"$i"/apps/kcmkhtml_filter.png      ;done
for i in {16,22,32};           do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/system-run.png                  hicolor/"$i"x"$i"/apps/kcmcgi.png               ;done
for i in {16,22};              do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/history.png                     hicolor/"$i"x"$i"/apps/kcmhistory.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/places/network.png                      hicolor/"$i"x"$i"/apps/kcmnetpref.png           ;done
for i in {16,32,48,64,128};    do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/blockdevice.png                 hicolor/"$i"x"$i"/apps/kcmkdnssd.png            ;done
for i in {16,22,32,48,64};     do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/input-joystick.png              hicolor/"$i"x"$i"/apps/kcmjoystick.png          ;done
for i in {16,32,48,64,128};    do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/input-mouse.png                 hicolor/"$i"x"$i"/apps/kcmmouse.png             ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/devices/computer.png                    hicolor/"$i"x"$i"/apps/kcmmedia.png             ;done
for i in {16,22,32};           do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/encrypted.png                   hicolor/"$i"x"$i"/apps/kcmcrypto.png            ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/places/trashcan_empty.png               hicolor/"$i"x"$i"/apps/kcmprivacy.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{prefix}/share/icons/crystalsvg/"$i"x"$i"/places/network.png                      hicolor/"$i"x"$i"/apps/kcmnic.png               ;done
popd

# PAM configuration files (except openSUSE)
%__install -D -m 644 "%{SOURCE2}" "%{?buildroot}%{_sysconfdir}/pam.d/tdm-trinity"
%__install -D -m 644 "%{SOURCE3}" "%{?buildroot}%{_sysconfdir}/pam.d/tdm-trinity-np"
%__install -D -m 644 "%{SOURCE4}" "%{?buildroot}%{_sysconfdir}/pam.d/kcheckpass-trinity"
%__install -D -m 644 "%{SOURCE5}" "%{?buildroot}%{_sysconfdir}/pam.d/tdescreensaver-trinity"

%install -a
# Makes 'media_safelyremove.desktop' an alternative.
# This allows the use of 'tdeio-umountwrapper' package.
%__mv -f "%{buildroot}%{prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop" "%{buildroot}%{prefix}/share/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase"
%__mkdir_p "%{buildroot}%{_sysconfdir}/alternatives"

# Adds a GDM/KDM/XDM session called 'TDE'
%__install -D -m 644 \
	"%{?buildroot}%{prefix}/share/apps/tdm/sessions/tde.desktop" \
	"%{?buildroot}%{_datadir}/xsessions/tde.desktop"

# Move faces icon to XDG directory '/usr/share/faces'
if [ ! -d "%{?buildroot}%{_datadir}/faces" ]; then
  %__mkdir_p "%{?buildroot}%{_datadir}/faces"
  %__mv -f "%{?buildroot}%{prefix}/share/apps/tdm/pics/users/"* "%{?buildroot}%{_datadir}/faces" 2>/dev/null
  rmdir "%{?buildroot}%{prefix}/share/apps/tdm/pics/users"
fi
%__ln_s "%{_datadir}/faces" "%{?buildroot}%{prefix}/share/apps/tdm/pics/users"

%__install -d -m 755 %{?buildroot}%{_sysconfdir}/X11/wmsession.d
cat <<EOF >"%{?buildroot}%{_sysconfdir}/X11/wmsession.d/45TDE"
NAME=TDE
ICON=kde-wmsession.xpm
DESC=The Trinity Desktop Environment
EXEC=%{prefix}/bin/starttde
SCRIPT:
exec %{prefix}/bin/starttde
EOF

%__install -d -m 755 %{?buildroot}%{_datadir}/X11/dm.d
cat <<EOF >"%{?buildroot}%{_datadir}/X11/dm.d/45TDE.conf"
NAME=TDM
DESCRIPTION=TDM (Trinity Display Manager)
PACKAGE=trinity-tdm
EXEC=%{prefix}/bin/tdm
EOF

# TDM configuration
%__sed -i "s/^#*MinShowUID=.*\b/MinShowUID=1000/" "%{buildroot}%{_sysconfdir}/trinity/tdm/tdmrc"

# Icons from TDE Control Center should only be displayed in TDE
for i in %{?buildroot}%{prefix}/share/applications/tde/*.desktop ; do
  if grep -q "^Categories=.*X-TDE-settings" "${i}"; then
    if ! grep -q "OnlyShowIn=TDE" "${i}" ; then
      echo "OnlyShowIn=TDE;" >>"${i}"
    fi
  fi
done

# Other apps that should stay in TDE
for i in ksysguard tde-kcontrol tdefontview showdesktop; do
  echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{prefix}/share/applications/tde/${i}.desktop"
done

# Remove setuid bit on some binaries.
%{?with_tsak:chmod 0511 "%{?buildroot}%{prefix}/bin/tdmtsak"}
chmod 0755 "%{?buildroot}%{prefix}/bin/kcheckpass"
%{?with_kbdledsync:chmod 0755 "%{?buildroot}%{prefix}/bin/tdekbdledsync"}

# Fix permissions on shell scripts
chmod 0755 "%{?buildroot}%{prefix}/share/apps/tdeconf_update/move_session_config.sh"
chmod 0755 "%{?buildroot}%{prefix}/share/doc/tde/HTML/en/khelpcenter/glossary/checkxrefs"

# Links duplicate files
%fdupes "%{?buildroot}%{prefix}/share"

# fix desktop icon names per XDG spec
mv %{?buildroot}/%{prefix}/share/apps/kdesktop/Desktop/My_Computer %{buildroot}/%{prefix}/share/apps/kdesktop/Desktop/My_Computer.desktop
mv %{?buildroot}/%{prefix}/share/apps/kdesktop/Desktop/My_Documents %{buildroot}/%{prefix}/share/apps/kdesktop/Desktop/My_Documents.desktop
mv %{?buildroot}/%{prefix}/share/apps/kdesktop/Desktop/My_Network_Places %{buildroot}/%{prefix}/share/apps/kdesktop/Desktop/My_Network_Places.desktop
mv %{?buildroot}/%{prefix}/share/apps/kdesktop/Desktop/Printers %{buildroot}/%{prefix}/share/apps/kdesktop/Desktop/Printers.desktop
mv %{?buildroot}/%{prefix}/share/apps/kdesktop/Desktop/Trash %{buildroot}/%{prefix}/share/apps/kdesktop/Desktop/Trash.desktop
mv %{?buildroot}/%{prefix}/share/apps/kdesktop/Desktop/Web_Browser %{buildroot}/%{prefix}/share/apps/kdesktop/Desktop/Web_Browser.desktop

# Removes obsolete Beagle-related files
%__rm -f %{?buildroot}%{prefix}/bin/khc_beagle_index.pl
%__rm -f %{?buildroot}%{prefix}/bin/khc_beagle_search.pl

# Remove conflicting doc
%__rm -rf "%{?buildroot}%{prefix}/share/doc/tde/HTML/en/tdeioslave/gopher"

# Removes tderandrtray documentation, if not built.
%{!?with_tderandrtray:%__rm -rf "%{?buildroot}%{prefix}/share/doc/tde/HTML/en/tderandrtray"}

